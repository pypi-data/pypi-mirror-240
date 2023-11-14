import json
import os
from datetime import datetime

from promptflow._internal import ErrorResponse, bulk_logger
from promptflow.contracts.run_info import FlowRunInfo
from promptflow.contracts.run_info import Status as PromptflowRunStatus
from promptflow.exceptions import ErrorTarget, SystemErrorException, UserErrorException
from promptflow.runtime._errors import FailedToGetHostCreds, InvalidClientAuthentication, to_string
from promptflow.runtime.utils import logger
from promptflow.runtime.utils._debug_log_helper import generate_safe_error_stacktrace
from promptflow.runtime.utils._utils import is_in_ci_pipeline
from promptflow.runtime.utils.retry_utils import retry
from promptflow.runtime.utils.timer import Timer

try:
    import mlflow
    from azure.core.exceptions import ClientAuthenticationError
    from mlflow.entities.run import Run as MlflowRun
    from mlflow.entities.run_status import RunStatus as MlflowRunStatus
    from mlflow.exceptions import RestException
    from mlflow.protos.databricks_pb2 import RESOURCE_DOES_NOT_EXIST, ErrorCode
    from mlflow.tracking import MlflowClient
    from mlflow.utils.rest_utils import http_request
except ImportError as e:
    msg = f"Please install azure-related packages, currently got {str(e)}"
    raise UserErrorException(message=msg, target=ErrorTarget.AZURE_RUN_STORAGE)

RunStatusMapping = {
    PromptflowRunStatus.Completed.value: MlflowRunStatus.to_string(MlflowRunStatus.FINISHED),
    PromptflowRunStatus.Failed.value: MlflowRunStatus.to_string(MlflowRunStatus.FAILED),
    PromptflowRunStatus.Canceled.value: MlflowRunStatus.to_string(MlflowRunStatus.KILLED),
}


class MlflowHelper:
    ERROR_EVENT_NAME = "Microsoft.MachineLearning.Run.Error"
    ERROR_MESSAGE_SET_MULTIPLE_TERMINAL_STATUS = "Cannot set run to multiple terminal states"
    RUN_HISTORY_TOTAL_TOKENS_PROPERTY_NAME = "azureml.promptflow.total_tokens"

    def __init__(self, mlflow_tracking_uri):
        """Set mlflow tracking uri to target uri"""
        self.enable_usage_in_ci_pipeline_if_needed()
        if isinstance(mlflow_tracking_uri, str) and mlflow_tracking_uri.startswith("azureml:"):
            logger.info(f"Setting mlflow tracking uri to {mlflow_tracking_uri!r}")
            mlflow.set_tracking_uri(mlflow_tracking_uri)
        else:
            message = (
                f"Mlflow tracking uri must be a string that starts with 'azureml:', "
                f"got {mlflow_tracking_uri!r} with type {type(mlflow_tracking_uri)!r}."
            )
            raise UserErrorException(message=message, target=ErrorTarget.AZURE_RUN_STORAGE)

        self.client = MlflowClient()
        self.api_call_cred = self.get_api_call_cred()

    def get_api_call_cred(self):
        try:
            # modify client cred to be used in run history api call
            api_call_cred = self.get_host_creds()
            api_call_cred.host = api_call_cred.host.replace("mlflow/v2.0", "mlflow/v1.0").replace(
                "mlflow/v1.0", "history/v1.0"
            )

            return api_call_cred
        except ClientAuthenticationError as ex:
            raise InvalidClientAuthentication(
                message="Failed to get mlflow credential", target=ErrorTarget.RUNTIME
            ) from ex
        except Exception as e:
            ex_message = to_string(e)
            error_message = f"Failed to get host creds with error {ex_message}."
            logger.error(error_message)
            raise FailedToGetHostCreds(
                message=error_message,
                target=ErrorTarget.AZURE_RUN_STORAGE,
            ) from e

    # mlflow client get credential may return ClientAuthenticationError transiently even with correct credential
    @retry(ClientAuthenticationError, tries=5, delay=0.5, backoff=1, logger=logger)
    def get_host_creds(self):
        return self.client._tracking_client.store.get_host_creds()

    def enable_usage_in_ci_pipeline_if_needed(self):
        if is_in_ci_pipeline():
            # this is to enable mlflow use CI SP client credential
            # Refer to: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-use-mlflow-configure-tracking?view=azureml-api-2&tabs=python%2Cmlflow#configure-authentication  # noqa: E501
            os.environ["AZURE_TENANT_ID"] = os.environ.get("tenantId")
            os.environ["AZURE_CLIENT_ID"] = os.environ.get("servicePrincipalId")
            os.environ["AZURE_CLIENT_SECRET"] = os.environ.get("servicePrincipalKey")

    def start_run(self, run_id: str, create_if_not_exist: bool = False):
        try:
            logger.info(
                f"Starting the aml run {run_id!r}...",
            )
            mlflow.start_run(run_id=run_id)
        except Exception as e:
            msg = str(e)
            if (
                create_if_not_exist
                and isinstance(e, RestException)
                and e.error_code == ErrorCode.Name(RESOURCE_DOES_NOT_EXIST)
            ):
                logger.warning(f"Run {run_id!r} not found, will create a new run with this run id.")
                self.create_run(run_id=run_id)
                return
            raise SystemErrorException(
                f"Failed to start root run {run_id!r} in workspace through mlflow: {msg}",
                target=ErrorTarget.AZURE_RUN_STORAGE,
                error=e,
            )

    def create_run(self, run_id: str, start_after_created=True, backoff_factor=None):
        """Create a run with specified run id"""
        endpoint = "/experiments/{}/runs/{}".format("Default", run_id)
        json_obj = {"runId": run_id}
        response = http_request(
            host_creds=self.api_call_cred,
            endpoint=endpoint,
            method="PATCH",
            json=json_obj,
            backoff_factor=backoff_factor,
        )

        if response.status_code == 401:
            logger.info(f"Original credential is expired, get a new credential and create the run {run_id!r} again...")
            self.api_call_cred = self.get_api_call_cred()
            response = http_request(
                host_creds=self.api_call_cred,
                endpoint=endpoint,
                method="PATCH",
                json=json_obj,
                backoff_factor=backoff_factor,
            )

        if response.status_code == 200:
            if start_after_created:
                try:
                    mlflow.start_run(run_id=run_id)
                except Exception as e:
                    raise SystemErrorException(
                        f"A new run {run_id!r} is created but failed to start it: {str(e)}",
                        target=ErrorTarget.AZURE_RUN_STORAGE,
                    )
        else:
            raise SystemErrorException(
                f"Failed to create run {run_id!r}: {response.text}",
                target=ErrorTarget.AZURE_RUN_STORAGE,
            )

    def _end_aml_root_run(self, run_info: FlowRunInfo, ex: Exception = None) -> None:
        """Update root run to end status"""
        # if error detected, write error info to run history
        error_response = self._get_error_response_dict(run_info, ex=ex)
        if error_response:
            current_run = mlflow.active_run()
            self.write_error_message(mlflow_run=current_run, error_response=error_response)

        # end the aml run here
        self.end_run(run_id=run_info.run_id, status=run_info.status.value)

    def end_run(self, run_id: str, status: str):
        """Update root run to end status"""
        if status not in RunStatusMapping:
            raise SystemErrorException(
                message="Trying to end a workspace root run with non-terminated status.",
                target=ErrorTarget.AZURE_RUN_STORAGE,
            )
        mlflow_status = RunStatusMapping[status]

        try:
            logger.info(
                f"Ending the aml run {run_id!r} with status {status!r}...",
            )
            mlflow.end_run(status=mlflow_status)
        except Exception as e:
            if isinstance(e, RestException) and self.ERROR_MESSAGE_SET_MULTIPLE_TERMINAL_STATUS in e.message:
                logger.warning(f"Failed to set run {run_id!r} to {status!r} since it is already ended.")
                return
            raise SystemErrorException(
                f"Failed to end root run {run_id!r} in workspace through mlflow: {str(e)}",
                target=ErrorTarget.AZURE_RUN_STORAGE,
                error=e,
            )

    def _get_error_response_dict(self, run_info: FlowRunInfo, ex: Exception) -> dict:
        """Get the error response dict from run info error or exception"""
        result = None
        run_info_error = run_info.error
        if run_info_error and isinstance(run_info_error, dict) and len(run_info_error) > 0:
            result = ErrorResponse.from_error_dict(run_info_error).to_dict()
        elif ex:
            result = ErrorResponse.from_exception(ex).to_dict()
        return result

    def get_run(self, run_id: str):
        return mlflow.get_run(run_id=run_id)

    def active_run(self):
        """Get current active run"""
        return mlflow.active_run()

    def write_error_message(self, mlflow_run: MlflowRun, error_response: dict):
        """Write error message to run history with specified exception info"""
        run_id = mlflow_run.info.run_id
        experiment_id = mlflow_run.info.experiment_id
        logger.warning(f"[{run_id}] Run failed. Execution stackTrace: {generate_safe_error_stacktrace(error_response)}")

        error_event = {
            "timestamp": datetime.utcnow().isoformat(),
            "name": self.ERROR_EVENT_NAME,
            "data": {
                "errorResponse": error_response,
            },
        }

        endpoint = "/experimentids/{}/runs/{}/events".format(experiment_id, run_id)
        response = http_request(
            host_creds=self.api_call_cred,
            endpoint=endpoint,
            method="POST",
            json=error_event,
        )

        if response.status_code == 401:
            logger.info(
                f"Original credential is expired, get a new credential "
                f"and write error message for run {run_id!r} again..."
            )
            self.api_call_cred = self.get_api_call_cred()
            response = http_request(
                host_creds=self.api_call_cred,
                endpoint=endpoint,
                method="POST",
                json=error_event,
            )

        if response.status_code != 200:
            message = (
                f"Failed to write error message to run history for run {run_id!r}, response status code: "
                f"{response.status_code!r}, response message: {response.text!r}"
            )
            logger.warning(message)

    def update_run_history_properties(self, run_info: FlowRunInfo):
        current_run = mlflow.active_run()
        if not current_run:
            # warning when there is no active aml run, not raise exception in case the issue is from mlflow itself.
            logger.warning("No active aml run found, make sure run tracker has started a aml run")
            return

        # current_run.info.run_id == run_info.run_id in this context
        run_id = current_run.info.run_id
        # run_info does not have experiment_id, so we get from current_run from mflow
        experiment_id = current_run.info.experiment_id

        properties = {
            # Write total_tokens into RH (RunDto.Properties), For example, "azureml.promptflow.total_tokens": "12"
            # System_metrics["total_tokens"] is integer. We write 0 if this metrics not exist
            self.RUN_HISTORY_TOTAL_TOKENS_PROPERTY_NAME: run_info.system_metrics.get("total_tokens", 0),
            # Add instance_results.jsonl path to run properties. Which is required by UI feature.
            "_azureml.evaluate_artifacts": '[{"path": "instance_results.jsonl", "type": "table"}]',
        }

        with Timer(bulk_logger, "Upload RH properties for run " + run_id):
            endpoint = "/experimentids/{}/runs/{}".format(experiment_id, run_id)
            json_obj = {"runId": run_id, "properties": properties}
            response = http_request(
                host_creds=self.api_call_cred,
                endpoint=endpoint,
                method="PATCH",
                json=json_obj,
            )

            if response.status_code == 401:
                logger.info(
                    f"Original credential is expired, get a new credential "
                    f"and write run properties for run {run_id!r} again..."
                )
                self.api_call_cred = self.get_api_call_cred()
                response = http_request(
                    host_creds=self.api_call_cred,
                    endpoint=endpoint,
                    method="PATCH",
                    json=json_obj,
                )

            if response.status_code == 200:
                logger.info(f"Successfully write run properties {json.dumps(properties)} with run id '{run_id}'")
            else:
                logger.warning(
                    f"Failed to write run properties {json.dumps(properties)} with run id {run_id}. "
                    f"Code: {response.status_code}, text: {response.text}"
                )

    def upload_metrics_to_run_history(self, run_info: FlowRunInfo):
        """Upload metrics to run history via mlflow"""
        metrics = run_info.metrics
        if isinstance(metrics, dict) and len(metrics) > 0:
            # There should be a root aml run that was created by MT when we try to log metrics for.
            # Run tracker will start this aml run when executing the flow run and here we should get the active run.
            current_run = mlflow.active_run()
            if not current_run:
                # warning when there is no active aml run, not raise exception in case the issue is from mlflow itself.
                logger.warning(
                    "No active aml run found, make sure run tracker has started a aml run to log metrics for."
                )
                return

            # start to log metrics to aml run
            # TODO: Refine the logic here since log_metric logic should handled in runtime bulk api instead of here
            from promptflow._legacy.metric_reconstruction import reconstruct_metrics_dict

            with Timer(bulk_logger, "Upload metrics for run " + run_info.run_id):
                try:
                    new_metrics = reconstruct_metrics_dict(metrics)
                    for metric_name, value in new_metrics.items():
                        # use mlflow api to upload refined metric
                        mlflow.log_metric(metric_name, value)
                except Exception as e:
                    logger.warning(f"Failed to upload metrics to workspace: {str(e)}")
        elif metrics is not None:
            logger.warning(f"Metrics should be a dict but got a {type(metrics)!r} with content {metrics!r}")

    def persist_status_summary(self, metrics: dict, flow_run_id: str):
        """Upload status summary metrics to run history via mlflow"""
        if isinstance(metrics, dict) and len(metrics) > 0:
            # There should be a root aml run that was created by MT when we try to log metrics for.
            # Run tracker will start this aml run when executing the flow run and here we should get the active run.
            current_run = mlflow.active_run()
            if not current_run:
                # warning when there is no active aml run, not raise exception in case the issue is from mlflow itself.
                logger.warning(
                    "No active aml run found, make sure run tracker has started a aml run to log metrics for."
                )
                return

            # start to log metrics to aml run
            with Timer(bulk_logger, "Upload status summary metrics for run " + flow_run_id):
                try:
                    for metric_name, value in metrics.items():
                        # use mlflow api to status summary inner metric
                        mlflow.log_metric(metric_name, value)
                except Exception as e:
                    logger.warning(f"Failed to upload status summary metrics to workspace: {str(e)}")
        elif metrics is not None:
            logger.warning(f"Metrics should be a dict but got a {type(metrics)!r} with content {metrics!r}")
