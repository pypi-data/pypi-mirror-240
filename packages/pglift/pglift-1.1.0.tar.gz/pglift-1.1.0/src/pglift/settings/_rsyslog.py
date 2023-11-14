from pathlib import Path
from typing import Annotated

from pydantic import Field

from .base import BaseModel, ConfigPath


class Settings(BaseModel):
    """Settings for rsyslog."""

    configdir: Annotated[Path, ConfigPath] = Field(
        default=Path("rsyslog"), description="rsyslog config directory"
    )
