from pathlib import Path
from typing import Annotated, Literal, Optional, Union

from pydantic import Field, FilePath

from .base import BaseModel, ConfigPath, DataPath, LogPath, RunPath, ServerCert


class HostRepository(BaseModel):
    """Remote repository host for pgBackRest."""

    host: str = Field(description="Host name of the remote repository.")
    host_port: Optional[int] = Field(
        default=None,
        description="Port to connect to the remote repository.",
    )
    host_config: Optional[Path] = Field(
        default=None,
        description="pgBackRest configuration file path on the remote repository.",
    )


class TLSHostRepository(HostRepository):
    mode: Literal["host-tls"]
    cn: str = Field(description="Certificate Common Name of the remote repository.")
    certificate: ServerCert = Field(
        description="TLS certificate files for the pgBackRest server on site."
    )
    port: int = Field(default=8432, description="Port for the TLS server on site.")
    pid_file: Annotated[Path, RunPath] = Field(
        default=Path("pgbackrest.pid"),
        description="Path to which pgbackrest server process PID will be written.",
    )


class SSHHostRepository(HostRepository):
    mode: Literal["host-ssh"]
    host_user: Optional[str] = Field(
        default=None,
        description="Name of the user that will be used for operations on the repository host.",
    )
    cmd_ssh: Optional[Path] = Field(
        default=None,
        description="SSH client command. Use a specific SSH client command when an alternate is desired or the ssh command is not in $PATH.",
    )


class Retention(BaseModel):
    """Retention settings."""

    archive: int = 2
    diff: int = 3
    full: int = 2


class PathRepository(BaseModel):
    """Remote repository (path) for pgBackRest."""

    mode: Literal["path"]
    path: Annotated[Path, DataPath] = Field(
        description="Base directory path where backups and WAL archives are stored.",
    )
    retention: Retention = Field(default=Retention(), description="Retention options.")


class Settings(BaseModel):
    """Settings for pgBackRest."""

    execpath: FilePath = Field(
        default=Path("/usr/bin/pgbackrest"),
        description="Path to the pbBackRest executable.",
    )

    configpath: Annotated[Path, ConfigPath] = Field(
        default=Path("pgbackrest"),
        description="Base path for pgBackRest configuration files.",
    )

    repository: Union[TLSHostRepository, SSHHostRepository, PathRepository] = Field(
        description="Repository definition, either as a (local) path-repository or as a host-repository.",
        discriminator="mode",
    )

    logpath: Annotated[Path, LogPath] = Field(
        default=Path("pgbackrest"),
        description="Path where log files are stored.",
    )

    spoolpath: Annotated[Path, DataPath] = Field(
        default=Path("pgbackrest/spool"),
        description="Spool path.",
    )

    lockpath: Annotated[Path, RunPath] = Field(
        default=Path("pgbackrest/lock"),
        description="Path where lock files are stored.",
    )
