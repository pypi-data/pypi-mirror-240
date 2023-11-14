import enum
from decimal import Decimal
from typing import ClassVar, Optional

import psycopg.conninfo
from pydantic import Field, SecretStr, validator

from ..types import AnsibleConfig, AutoStrEnum, CLIConfig, Manifest


class WALSenderState(AutoStrEnum):
    startup = enum.auto()
    catchup = enum.auto()
    streaming = enum.auto()
    backup = enum.auto()
    stopping = enum.auto()


@enum.unique
class StandbyState(AutoStrEnum):
    """Instance standby status"""

    demoted = enum.auto()
    promoted = enum.auto()


class Standby(Manifest):
    """Standby information."""

    _cli_config: ClassVar[dict[str, CLIConfig]] = {
        "primary_conninfo": {"name": "for"},
        "status": {"hide": True},
        "replication_lag": {"hide": True},
        "wal_sender_state": {"hide": True},
    }
    _ansible_config: ClassVar[dict[str, AnsibleConfig]] = {
        "replication_lag": {"hide": True},
        "wal_sender_state": {"hide": True},
    }

    primary_conninfo: str = Field(
        description="DSN of primary for streaming replication.", readOnly=True
    )
    password: Optional[SecretStr] = Field(
        default=None,
        description="Password for the replication user.",
        exclude=True,
        readOnly=True,
    )
    status: StandbyState = Field(
        default=StandbyState.demoted,
        description="Instance standby state.",
        writeOnly=True,
        exclude=True,
    )
    slot: Optional[str] = Field(
        description="Replication slot name. Must exist on primary.", readOnly=True
    )
    replication_lag: Optional[Decimal] = Field(
        default=None, description="Replication lag.", readOnly=True
    )
    wal_sender_state: Optional[WALSenderState] = Field(
        default=None,
        description="State of the WAL sender process (on primary) this standby is connected to.",
        readOnly=True,
    )

    @validator("primary_conninfo")
    def __validate_primary_conninfo_(cls, value: str) -> str:
        """Validate 'primary_conninfo' field.

        >>> Standby.parse_obj({"primary_conninfo": "host=localhost"})  # doctest: +ELLIPSIS
        Standby(primary_conninfo='host=localhost', password=None, ...)
        >>> Standby.parse_obj({"primary_conninfo": "hello"})
        Traceback (most recent call last):
            ...
        pydantic.error_wrappers.ValidationError: 1 validation error for Standby
        primary_conninfo
          missing "=" after "hello" in connection info string
         (type=value_error)
        >>> Standby.parse_obj({"primary_conninfo": "host=localhost password=xx"})
        Traceback (most recent call last):
            ...
        pydantic.error_wrappers.ValidationError: 1 validation error for Standby
        primary_conninfo
          connection string must not contain a password (type=value_error)
        """
        try:
            conninfo = psycopg.conninfo.conninfo_to_dict(value)
        except psycopg.ProgrammingError as e:
            raise ValueError(str(e)) from e
        if "password" in conninfo:
            raise ValueError("connection string must not contain a password")
        return value

    @property
    def full_primary_conninfo(self) -> str:
        """Connection string to the primary, including password.

        >>> s = Standby.parse_obj({"primary_conninfo": "host=primary port=5444", "password": "qwerty"})
        >>> s.full_primary_conninfo
        'host=primary port=5444 password=qwerty'
        """
        kw = {}
        if self.password:
            kw["password"] = self.password.get_secret_value()
        return psycopg.conninfo.make_conninfo(self.primary_conninfo, **kw)
