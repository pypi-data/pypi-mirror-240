"""Entities for local promptflow runtime which will store."""

from dataclasses import dataclass, field

from promptflow._internal import PRIMARY_KEY


@dataclass
class SecretRecords:
    """"""

    RowKey: str = field(metadata={PRIMARY_KEY: True})  # Secret Key
    secret: str  # secret value
