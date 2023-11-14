# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import contextvars
import json
import multiprocessing
import os
import shutil
import threading
import time
from contextlib import contextmanager
from datetime import timedelta
from pathlib import Path
from typing import Callable, Dict, List

from promptflow._internal import (
    ConnectionManager,
    DefaultRunStorage,
    ErrorResponse,
    ExceptionPresenter,
    JsonSerializedPromptflowException,
    OperationContext,
    set_context,
    transpose,
)
from promptflow._legacy._run_status_helper import (
    mark_runs_as_failed_in_runhistory,
    mark_runs_as_failed_in_storage_and_runhistory,
)
from promptflow.contracts.flow import FlowInputAssignment
from promptflow.contracts.run_info import Status
from promptflow.executor.batch_engine import BatchEngine
from promptflow.executor.flow_executor import FlowExecutor
from promptflow.runtime._errors import FlowFileNotFound, StorageAuthenticationError, UserAuthenticationError
from promptflow.runtime.constants import LINE_NUMBER_KEY, ComputeType, PromptflowEdition
from promptflow.runtime.contracts._errors import InvalidRunMode, SubmissionDataDeserializeError
from promptflow.runtime.contracts.runtime import (
    BulkRunRequestV2,
    FlowRequestV2,
    FlowSourceType,
    SingleNodeRequestV2,
    SubmissionRequestBaseV2,
    SubmitFlowRequest,
)
from promptflow.runtime.utils._run_history_client import RunHistoryClient
from promptflow.runtime.utils._str_utils import join_stripped
from promptflow.runtime.utils._utils import get_runtime_version
from promptflow.runtime.utils.internal_logger_utils import (
    FileType,
    SystemLogContext,
    close_telemetry_log_handler,
    reset_telemetry_log_handler,
    system_logger,
)
from promptflow.runtime.utils.mlflow_helper import MlflowHelper
from promptflow.runtime.utils.retry_utils import retry
from promptflow.runtime.utils.thread_utils import timeout
from promptflow.runtime.utils.timer import Timer

from ._errors import DataInputsNotfound, FlowRunTimeoutError, UnexpectedFlowSourceType, UnexpectedOutputSubDir
from .connections import (
    build_connection_dict,
    get_used_connection_names_from_environment_variables,
    update_environment_variables_with_connections,
)
from .data import prepare_data
from .run_tracker_adapter import RunTrackerAdapter
from .runtime_config import RuntimeConfig, load_runtime_config
from .utils import log_runtime_pf_version, logger, multi_processing_exception_wrapper
from .utils._flow_source_helper import fill_working_dir
from .utils._run_status_helper import mark_run_v2_as_failed_in_runhistory

STATUS_CHECKER_INTERVAL = 20  # seconds
MONITOR_REQUEST_TIMEOUT = 10  # seconds
SYNC_SUBMISSION_TIMEOUT = 330  # seconds
WAIT_SUBPROCESS_EXCEPTION_TIMEOUT = 10  # seconds
BULKRUN_SUBMISSION_TIMEOUT = timedelta(days=10).total_seconds()


class PromptFlowRuntime:
    """PromptFlow runtime."""

    _instance = None

    def __init__(self, config: RuntimeConfig):
        self.config = config

    def execute_flow(self, request: SubmissionRequestBaseV2, execute_flow_func: Callable):
        if self.config.execution.execute_in_process:
            result = execute_flow_func(self.config, request)
        else:
            result = execute_flow_request_multiprocessing(self.config, request, execute_flow_func)
        return result

    def execute(self, request: SubmitFlowRequest):
        """execute a flow."""
        # init in main process, so it can be cached
        from promptflow._legacy.runtime import execute_request, execute_request_multiprocessing

        self.config.init_from_request(request.workspace_msi_token_for_storage_resource)

        if self.config.execution.execute_in_process:
            result = execute_request(self.config, request)
        else:
            result = execute_request_multiprocessing(self.config, request)
        return result

    def mark_flow_runs_as_failed(self, flow_request: SubmitFlowRequest, payload: dict, ex: Exception):
        try:
            code = None
            if isinstance(ex, JsonSerializedPromptflowException):
                error_dict = json.loads(ex.message)
                code = ErrorResponse.from_error_dict(error_dict).innermost_error_code
                logger.info(f"JsonSerializedPromptflowException inner most error code is:{code}.")
            else:
                code = ErrorResponse.from_exception(ex).innermost_error_code
                logger.info(f"Exception innermost_error_code is:{code}.")

            if code == SubmissionDataDeserializeError.__name__ or code == InvalidRunMode.__name__:
                logger.warning(
                    "For SubmissionDataDeserializeError and InvalidRunMode, cannot get the variant run ids, "
                    + "eval run id and bulk test run id, so do nothing."
                )
            elif code == StorageAuthenticationError.__name__:
                logger.info("For StorageAuthenticationError, only mark job as failed in run history.")
                mark_runs_as_failed_in_runhistory(self.config, flow_request, payload, ex)
            elif code == UserAuthenticationError.__name__:
                logger.warning(
                    "For UserAuthenticationError, cannot update run status in both run history "
                    + "and table/blob storage, so do nothing."
                )
            else:
                logger.info("For other error, try to mark job as failed in both run history and table/blob storage.")
                mark_runs_as_failed_in_storage_and_runhistory(self.config, flow_request, payload, ex)
        except Exception as exception:
            logger.warning(
                "Hit exception when mark flow runs as failed: \n%s", ExceptionPresenter.create(exception).to_dict()
            )

    def mark_flow_runs_v2_as_failed(self, flow_request: BulkRunRequestV2, payload: dict, ex: Exception):
        try:
            code = None
            if isinstance(ex, JsonSerializedPromptflowException):
                error_dict = json.loads(ex.message)
                code = ErrorResponse.from_error_dict(error_dict).innermost_error_code
                logger.info(f"JsonSerializedPromptflowException inner most error code is:{code}.")
            else:
                code = ErrorResponse.from_exception(ex).innermost_error_code
                logger.info(f"Exception innermost_error_code is:{code}.")

            if flow_request:
                flow_run_id = flow_request.flow_run_id
            else:
                flow_run_id = payload.get("flow_run_id", "")
            if code == UserAuthenticationError.__name__:
                logger.warning("For UserAuthenticationError, cannot update run status in run history, so do nothing.")
            else:
                logger.info("For other error, try to mark job as failed in run history.")
                mark_run_v2_as_failed_in_runhistory(self.config, flow_run_id, ex)
        except Exception as exception:
            logger.warning(
                "Hit exception when mark flow runs v2 as failed: \n%s", ExceptionPresenter.create(exception).to_dict()
            )

    def init_storage(self):
        """Create tables for local storage (community edition)."""
        from promptflow._legacy.runtime_utils import create_tables_for_community_edition

        if self.config.deployment.edition != PromptflowEdition.COMMUNITY:
            return
        create_tables_for_community_edition(self.config)
        logger.info("Finished creating tables for community edition.")

    def update_operation_context(self, request):
        """Update operation context."""
        # Get the request id from the headers
        req_id = request.headers.get("x-ms-client-request-id") or request.headers.get("x-request-id")

        # Get the user agent from the headers and append the runtime version
        user_agent = request.headers.get("User-Agent", "")
        runtime_user_agent = join_stripped(f"promptflow-runtime/{get_runtime_version()}", user_agent)

        # Get the operation context instance and set its attributes
        operation_context = OperationContext.get_instance()
        operation_context.user_agent = runtime_user_agent
        operation_context.request_id = req_id
        operation_context.runtime_version = get_runtime_version()

        # Update operation context with deployment information
        deployment_dict = self.config.deployment.to_logsafe_dict()
        operation_context.update(deployment_dict)

    @classmethod
    def get_instance(cls):
        """get singleton instance."""
        if cls._instance is None:
            cls._instance = PromptFlowRuntime(load_runtime_config())
        return cls._instance

    @classmethod
    def init(cls, config: RuntimeConfig):
        """init runtime with config."""

        cls._instance = PromptFlowRuntime(config)


def set_environment_variables(env_vars: dict):
    """set environment variables."""
    if env_vars:
        for key, value in env_vars.items():
            os.environ[key] = value


def execute_flow_request_multiprocessing_impl(
    execute_flow_func: Callable,
    config: RuntimeConfig,
    parent_pid: int,
    request: SubmissionRequestBaseV2,
    return_dict,
    exception_queue,
    context_dict: Dict,
):
    """execute flow request V2 in a child process.
    the child process should execute inside multi_processing_exception_wrapper to avoide exception issue.
    """
    # Always use "fork" method to start subprocess when executing.
    multiprocessing.set_start_method("fork", force=True)
    operation_context = OperationContext.get_instance()
    operation_context.update(context_dict)
    with multi_processing_exception_wrapper(exception_queue):
        # set log context here;
        # otherwise the previously set context-local log handlers/filters will be lost
        # because this method is invoked in another process.
        with reset_and_close_logger(), get_log_context_from_v2_request(request):
            logger.info("[%s--%s] Start processing flowV2......", parent_pid, os.getpid())
            log_runtime_pf_version(logger)
            result = execute_flow_func(config, request)
            return_dict["result"] = result


def get_multiprocessing_context(region: str) -> "multiprocessing.context.BaseContext":
    # TODO: Use spawn in all regions.
    regions_to_use_spawn_context = ["eastus2euap", "centraluseuap"]
    if region in regions_to_use_spawn_context:
        # Use "spawn" method to start child process (in linux system the default method is "fork").
        # By using "spawn" method, the child process is started with a fresh python interpreter,
        # so that all the packages will be imported again.
        # This is because package version in current environment might change (because pip install is executed)
        # after runtime is started. We need to use the freshly-installed package to start execution.
        logger.info(f"Use spawn method to start child process. Region: {region}")
        return multiprocessing.get_context("spawn")
    else:
        logger.info(f"Use default method to start child process. Region: {region}")
        return multiprocessing.get_context()


def execute_flow_request_multiprocessing(config: RuntimeConfig, request: SubmissionRequestBaseV2, execute_flow_func):
    """execute request in a child process."""
    pid = os.getpid()
    mp = get_multiprocessing_context(config.get_region())
    manager = mp.Manager()
    return_dict = manager.dict()
    context_dict = OperationContext.get_instance().get_context_dict()
    exception_queue = mp.Queue()
    # TODO: change to support streaming output
    p = mp.Process(
        target=execute_flow_request_multiprocessing_impl,
        args=(
            execute_flow_func,
            config,
            pid,
            request,
            return_dict,
            exception_queue,
            context_dict,
        ),
    )
    p.start()

    if isinstance(request, BulkRunRequestV2):
        logger.info("Starting to check process %s status for run %s", p.pid, request.flow_run_id)
        start_thread_to_monitor_request_V2_handler_process(
            config=config,
            request=request,
            process=p,
        )
        p.join(timeout=BULKRUN_SUBMISSION_TIMEOUT)

        if p.is_alive():
            logger.error(f"[{p.pid}] Stop bulkrun subprocess for exceeding {BULKRUN_SUBMISSION_TIMEOUT} seconds.")
            p.terminate()
            p.join()
            raise FlowRunTimeoutError(BULKRUN_SUBMISSION_TIMEOUT)
    else:
        # MT timeout 300s for sync submission.
        # Timeout longer than MT to avoid exception thrown early
        p.join(timeout=SYNC_SUBMISSION_TIMEOUT)

        if p.is_alive():
            logger.error(f"[{p.pid}] Stop flow subprocess for exceeding {SYNC_SUBMISSION_TIMEOUT} seconds.")
            p.terminate()
            p.join()
            raise FlowRunTimeoutError(SYNC_SUBMISSION_TIMEOUT)
    logger.info("Process %s finished", p.pid)
    # when p is killed by signal, exitcode will be negative without exception
    if p.exitcode and p.exitcode > 0:
        exception = None
        try:
            exception = exception_queue.get(timeout=WAIT_SUBPROCESS_EXCEPTION_TIMEOUT)
        except Exception:
            pass
        # JsonSerializedPromptflowException will be raised here
        # no need to change to PromptflowException since it will be handled in app.handle_exception
        # we can unify the exception when we decide to expose executor.execute as an public API
        if exception is not None:
            raise exception
    result = return_dict.get("result", {})

    logger.info("[%s] Child process finished!", pid)
    return result


def parse_inputs_and_other_nodes_outputs(inputs_from_payload: Dict):
    updated_node_inputs = {}
    other_nodes_outputs = {}
    for k, v in inputs_from_payload.items():
        if FlowInputAssignment.is_flow_input(k):
            updated_k: str = FlowInputAssignment.deserialize(k).value
            # Flow input.
            updated_node_inputs.update({updated_k: v})
        else:
            # Put other node's output in result.
            node_name = SingleNodeRequestV2.get_node_name_from_node_inputs_key(k)
            other_nodes_outputs.update({node_name: v})
    return updated_node_inputs, other_nodes_outputs


def execute_node_request(config: RuntimeConfig, request: SingleNodeRequestV2):
    origin_wd = os.getcwd()
    working_dir = None
    try:
        set_environment_variables(request.environment_variables)
        connection_names = get_used_connection_names_from_environment_variables()
        built_connections = build_connection_dict(
            connection_names=connection_names,
            subscription_id=config.deployment.subscription_id,
            resource_group=config.deployment.resource_group,
            workspace_name=config.deployment.workspace_name,
        )
        update_environment_variables_with_connections(built_connections)
        if request.flow_source.flow_source_type != FlowSourceType.AzureFileShare:
            raise UnexpectedFlowSourceType(message_format="Node request should be from Azure File Share")
        working_dir = fill_working_dir(
            config.deployment.compute_type,
            request.flow_source.flow_source_info,
            request.flow_run_id,
            request.flow_source.flow_dag_file,
        )
        # Node run doesn't need to set storage.
        dag_file = request.flow_source.flow_dag_file

        node_inputs, other_nodes_outputs = parse_inputs_and_other_nodes_outputs(request.inputs)
        os.chdir(working_dir)
        output_sub_dir = request.output_sub_dir
        if output_sub_dir is None:
            logger.warning(
                "The node request is missing the 'output_sub_dir' field, which is not as expected. Files generated"
                "during execution will be saved to the current flow directory. Please update your client to the latest"
                "version."
            )
            output_sub_dir = "."
        if Path(output_sub_dir).is_absolute():
            raise UnexpectedOutputSubDir(
                message_format="Node test output sub directory '{output_sub_dir}' must be a relative path,"
                "not an absolute path.",
                output_sub_dir=output_sub_dir,
            )
        result = FlowExecutor.load_and_exec_node(
            flow_file=dag_file,
            node_name=request.node_name,
            output_sub_dir=output_sub_dir,
            flow_inputs=node_inputs,
            dependency_nodes_outputs=other_nodes_outputs,
            connections=request.connections,
            working_dir=working_dir,
            raise_ex=False,
        )
        from promptflow._internal import serialize

        return {
            "node_runs": [serialize(result)],
        }
    finally:
        os.chdir(origin_wd)
        # post process: clean up and restore working dir
        # note: no need to clean environment variables, because they are only set in child process
        if working_dir and not config.execution.debug:
            # remove working dir if not debug mode
            if (
                config.deployment.compute_type == ComputeType.COMPUTE_INSTANCE
                and request.flow_source is not None
                and request.flow_source.flow_source_type == FlowSourceType.AzureFileShare
            ):
                # Don't remove working dir when it is CI mounting dir
                pass
            else:
                logger.info("Cleanup working dir %s", working_dir)
                shutil.rmtree(working_dir, ignore_errors=True)


def execute_flow_request(config: RuntimeConfig, request: FlowRequestV2):
    origin_wd = os.getcwd()
    working_dir = None
    try:
        set_environment_variables(request.environment_variables)
        connection_names = get_used_connection_names_from_environment_variables()
        built_connections = build_connection_dict(
            connection_names=connection_names,
            subscription_id=config.deployment.subscription_id,
            resource_group=config.deployment.resource_group,
            workspace_name=config.deployment.workspace_name,
        )
        update_environment_variables_with_connections(built_connections)
        if request.flow_source.flow_source_type != FlowSourceType.AzureFileShare:
            raise UnexpectedFlowSourceType(message_format="Flow request should be from Azure File Share")
        working_dir = fill_working_dir(
            config.deployment.compute_type,
            request.flow_source.flow_source_info,
            request.flow_run_id,
            request.flow_source.flow_dag_file,
        )
        # Flow run doesn't need to set storage.
        os.chdir(working_dir)
        flow_id, run_id = request.flow_id, request.flow_run_id
        dag_file = request.flow_source.flow_dag_file
        output_sub_dir = request.output_sub_dir
        if output_sub_dir is None:
            logger.warning(
                "The flow request is missing the 'output_sub_dir' field, which is not as expected. Files generated"
                "during execution will be saved to the current flow directory. Please update your client to the latest"
                "version."
            )
            output_sub_dir = "."
        if Path(output_sub_dir).is_absolute():
            raise UnexpectedOutputSubDir(
                message_format="Flow test output sub directory '{output_sub_dir}' must be a relative path,"
                "not an absolute path.",
                output_sub_dir=output_sub_dir,
            )
        storage = DefaultRunStorage(base_dir=working_dir, sub_dir=Path(output_sub_dir))
        flow_executor = FlowExecutor.create(
            dag_file, request.connections, Path(working_dir), storage=storage, raise_ex=False
        )
        run_tracker = flow_executor._run_tracker
        run_tracker._activate_in_context()
        run_info = run_tracker.start_flow_run(flow_id, run_id, run_id)
        try:
            line_result = flow_executor.exec_line(inputs=request.inputs, index=0, run_id=run_id)
            # TODO: Refine the logic here, avoid returning runs from run_tracker,
            # We should better return the result from line_result and aggregation result.
            flow_executor._add_line_results([line_result])
            if flow_executor.has_aggregation_node:
                inputs_list = {k: [v] for k, v in request.inputs.items()}
                aggregation_inputs_list = {k: [v] for k, v in line_result.aggregation_inputs.items()}
                aggregate_result = flow_executor.exec_aggregation(inputs_list, aggregation_inputs_list, run_id=run_id)
                run_info.metrics = aggregate_result.metrics
            run_tracker.end_run(run_id, result=[])
        except Exception as e:  # We init flow executor with raise_ex=False, so usually, there is no exception.
            logger.exception(f"Run {run_id} failed. Exception: {{customer_content}}", extra={"customer_content": e})
            run_tracker.end_run(run_id, ex=e)
        finally:
            run_tracker._deactivate_in_context()
        return run_tracker.collect_all_run_infos_as_dicts()
    finally:
        os.chdir(origin_wd)
        # post process: clean up and restore working dir
        # note: no need to clean environment variables, because they are only set in child process
        if working_dir and not config.execution.debug:
            # remove working dir if not debug mode
            if (
                config.deployment.compute_type == ComputeType.COMPUTE_INSTANCE
                and request.flow_source is not None
                and request.flow_source.flow_source_type == FlowSourceType.AzureFileShare
            ):
                # Don't remove working dir when it is CI mounting dir
                pass
            else:
                logger.info("Cleanup working dir %s", working_dir)
                shutil.rmtree(working_dir, ignore_errors=True)


def execute_bulk_run_request(config: RuntimeConfig, request: BulkRunRequestV2):
    origin_wd = os.getcwd()
    working_dir = None
    try:
        set_environment_variables(request.environment_variables)
        connection_names = get_used_connection_names_from_environment_variables()
        built_connections = build_connection_dict(
            connection_names=connection_names,
            subscription_id=config.deployment.subscription_id,
            resource_group=config.deployment.resource_group,
            workspace_name=config.deployment.workspace_name,
        )
        update_environment_variables_with_connections(built_connections)
        run_id = request.flow_run_id

        working_dir = Path(f"requests/{run_id}").resolve()
        output_dir = working_dir / ".flow_outputs"
        run_storage = config.get_run_storage(
            workspace_access_token=None,
            azure_storage_setting=request.azure_storage_setting,
            run_mode=request.get_run_mode(),
            output_dir=output_dir,
        )
        run_history_client = config.get_run_history_client()
        mlflow_tracking_uri = config.set_mlflow_tracking_uri()
        mlflow_helper = MlflowHelper(mlflow_tracking_uri=mlflow_tracking_uri)
        root_run_info = None
        run_tracker_adapter = None
        try:
            # Start to download folder.
            working_dir.mkdir(parents=True, exist_ok=True)
            output_dir.mkdir(exist_ok=True)
            if request.flow_source.flow_source_type != FlowSourceType.Snapshot:
                raise UnexpectedFlowSourceType(message_format="Bulk run request data should be from Snapshot.")
            snapshot_client = config.get_snapshot_client()
            snapshot_client.download_snapshot(request.flow_source.flow_source_info.snapshot_id, working_dir)

            # For bulk run, PFS should always assign data_inputs, otherwise it is one system error.
            if not request.data_inputs:
                raise DataInputsNotfound(message_format="Data inputs not found in bulk run request.")
            # Start to download inputs.
            input_dicts = {}
            for input_key, input_url in request.data_inputs.items():
                with Timer(logger, "Resolve data from url"):
                    # resolve data uri to local data
                    local_path = prepare_data(
                        input_url, destination=working_dir / "inputs" / input_key, runtime_config=config
                    )
                    input_dicts[input_key] = local_path

            os.chdir(working_dir)

            # Need to create FlowExecutor after source downloaded.
            dag_file = request.flow_source.flow_dag_file
            flow_executor = FlowExecutor.create(
                dag_file,
                request.connections,
                working_dir,
                storage=run_storage,
                raise_ex=False,
            )
            run_tracker = flow_executor._run_tracker
            run_tracker._activate_in_context()

            run_tracker_adapter = RunTrackerAdapter(
                run_tracker, mlflow_helper, run_history_client, request.get_run_mode()
            )
            root_run_info = run_tracker_adapter.start_root_flow_run(flow_id=request.flow_id, root_run_id=run_id)

            bulk_result = BatchEngine(flow_executor=flow_executor).run(
                input_dirs=input_dicts, inputs_mapping=request.inputs_mapping, output_dir=output_dir, run_id=run_id
            )

            output_keys = list(flow_executor._flow.outputs.keys())
            output_keys.append(LINE_NUMBER_KEY)
            output_results = transpose(bulk_result.outputs, keys=output_keys)

            # Patch output_results to run_info, but debug_asset/output_asset will use the data in output_dir
            run_tracker_adapter.end_root_flow_run(run_id, result=output_results)
        except FileNotFoundError as e:
            raise FlowFileNotFound("Cannot find flow file. Error message={e.message}") from e
        except Exception as e:
            if run_tracker_adapter:
                logger.exception(f"Run {run_id} failed. Exception: {{customer_content}}", extra={"customer_content": e})
                run_tracker_adapter.end_root_flow_run(run_id, ex=e)
            else:
                # If failed to initialize run tracker,
                # raise exception to let runtime mark_flow_runs_v2_as_failed to handle.
                raise
        finally:
            if run_tracker_adapter and root_run_info:
                status_summary = run_tracker.get_status_summary(run_id)
                run_tracker_adapter.persist_status_summary(status_summary, run_id)
                # persist_status_summary should be called before update_flow_run_info
                # which may invoke mlflow.end_run() to end the run.
                run_tracker_adapter.root_run_postprocess(root_run_info)
                run_tracker_adapter.update_flow_run_info(root_run_info)
                run_tracker._deactivate_in_context()
        # bulk submit is async api, not need result, this result is for debug/test purpose.
        return run_tracker.collect_all_run_infos_as_dicts()
    finally:
        os.chdir(origin_wd)
        # post process: clean up and restore working dir
        # note: no need to clean environment variables, because they are only set in child process
        if working_dir and not config.execution.debug:
            # remove working dir if not debug mode
            shutil.rmtree(working_dir, ignore_errors=True)


def get_credential_list_for_v2_request(req: SubmissionRequestBaseV2) -> List[str]:
    credential_list = ConnectionManager(req.connections).get_secret_list()
    if req.app_insights_instrumentation_key:
        credential_list.append(req.app_insights_instrumentation_key)
    return credential_list


def get_log_context_from_v2_request(request: SubmissionRequestBaseV2) -> SystemLogContext:
    # Add root_flow_run_id and run_mode into logger's custom dimensions.
    run_mode = request.get_run_mode()
    custom_dimensions = {
        "root_flow_run_id": request.flow_run_id,
        "run_mode": run_mode.name if run_mode is not None else "",
    }
    edition = OperationContext.get_instance().get("edition", PromptflowEdition.COMMUNITY)
    file_type = FileType.Blob if edition == PromptflowEdition.ENTERPRISE else FileType.Local
    return SystemLogContext(
        file_path=request.log_path,
        run_mode=run_mode,
        credential_list=get_credential_list_for_v2_request(request),
        file_type=file_type,
        custom_dimensions=custom_dimensions,
        app_insights_instrumentation_key=request.app_insights_instrumentation_key,
        input_logger=logger,
    )


def start_thread_to_monitor_request_V2_handler_process(
    config: RuntimeConfig, request: SubmissionRequestBaseV2, process
):
    """Start a thread to monitor V2 request handler process.
    When request cancel is received, it will
    1. terminate the request handler process.
    2. mark the run as canceled.
    """

    def terminate_process():
        if process.is_alive():
            process.terminate()
            system_logger.info("Successfully terminated process with pid %s", process.pid)
        else:
            system_logger.info("Process already terminated")
        return True

    # add timeout & retry to avoid request stuck issue
    @retry(TimeoutError, tries=3)
    @timeout(timeout_seconds=MONITOR_REQUEST_TIMEOUT)
    def get_runhistory_client_from_config_with_retry() -> RunHistoryClient:
        return config.get_run_history_client()

    @retry(TimeoutError, tries=3)
    @timeout(timeout_seconds=MONITOR_REQUEST_TIMEOUT)
    def get_run_status_with_retry(runhistory_client: RunHistoryClient, run_id: str):
        run_info = runhistory_client.get_run(run_id=run_id)
        return run_info.get("status", "")

    @retry(TimeoutError, tries=10)
    @timeout(timeout_seconds=MONITOR_REQUEST_TIMEOUT)
    def cancel_run_with_retry(runhistory_client: RunHistoryClient, run_id):
        return runhistory_client.update_run_status(run_id=run_id, run_status=Status.Canceled)

    def monitor_run_status(run_id: str, terminate_process, context: contextvars.Context):
        try:
            runhistory_client = get_runhistory_client_from_config_with_retry()
            set_context(context)
            logger.info("Start checking run status for run %s", run_id)
            while True:
                # keep monitoring to make sure long running process can be terminated
                time.sleep(STATUS_CHECKER_INTERVAL)

                run_status = get_run_status_with_retry(runhistory_client=runhistory_client, run_id=run_id)
                if run_status is None:
                    logger.info("Run %s not found, end execution monitoring", run_id)
                    return
                system_logger.info("Run %s is in progress, Execution status: %s", run_id, run_status)
                if run_status in [Status.Canceled.value, Status.CancelRequested.value]:
                    logger.info("Cancel requested for run %s", run_id)
                    try:
                        # terminate the process gracefully
                        terminated = terminate_process()
                        if not terminated:
                            continue
                        logger.info("Updating status for run %s", run_id)
                        cancel_run_with_retry(runhistory_client=runhistory_client, run_id=run_id)
                        logger.info("Successfully canceled run %s", run_id)
                        # mark the run as canceled
                        return
                    except Exception as e:
                        logger.error("Failed to kill process for run %s due to %s", run_id, e, exc_info=True)
                        return
                elif Status.is_terminated(run_status):
                    logger.debug("Run %s is in terminate status %s", run_id, run_status)
                    return
        except Exception as e:
            system_logger.warning("Failed to monitor run status for run %s due to %s", run_id, e, exc_info=True)

    run_id = request.flow_run_id
    # cancel the parent run(run_id) as well as all its child runs
    thread = threading.Thread(
        name="monitor_bulk_run_status",
        target=monitor_run_status,
        kwargs={
            "run_id": run_id,
            "terminate_process": terminate_process,
            "context": contextvars.copy_context(),
        },
        daemon=True,
    )
    thread.start()


@contextmanager
def reset_and_close_logger():
    """
    In child process, reset telemetry handler,
    because the previous thread in parent process won't work in this process.
    After, close handler otherwise logs will be lost.
    """
    reset_telemetry_log_handler(logger)
    try:
        yield
    finally:
        close_telemetry_log_handler(logger)
