from pathlib import Path
from typing import Annotated

from pydantic import Field

from .base import BaseModel, LogPath, RunPath


class Settings(BaseModel):
    """Settings for pglift's command-line interface."""

    logpath: Annotated[Path, LogPath] = Field(
        default=Path(),
        description="Directory where temporary log files from command executions will be stored",
        title="CLI log directory",
    )

    log_format: str = Field(
        default="%(asctime)s %(levelname)-8s %(name)s - %(message)s",
        description="Format for log messages when written to a file",
    )

    date_format: str = Field(
        default="%Y-%m-%d %H:%M:%S",
        description="Date format in log messages when written to a file",
    )

    lock_file: Annotated[Path, RunPath] = Field(
        default=Path(".pglift.lock"),
        description="Path to lock file dedicated to pglift",
    )
