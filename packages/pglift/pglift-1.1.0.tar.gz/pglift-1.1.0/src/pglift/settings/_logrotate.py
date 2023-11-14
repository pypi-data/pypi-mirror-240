from pathlib import Path
from typing import Annotated

from pydantic import Field

from .base import BaseModel, ConfigPath


class Settings(BaseModel):
    """Settings for logrotate."""

    configdir: Annotated[Path, ConfigPath] = Field(
        default=Path("logrotate.d"), description="Logrotate config directory"
    )
