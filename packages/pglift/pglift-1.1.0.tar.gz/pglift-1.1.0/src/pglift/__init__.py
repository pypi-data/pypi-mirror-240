from __future__ import annotations

import sys
from functools import cache
from importlib import metadata
from typing import Any, Callable, Final, TypeVar, overload

import pluggy

from . import pm, settings

__all__ = ["hookimpl"]

# Declare type for hookimpl on our side until a version (> 1.0.0) is
# available.

F = TypeVar("F", bound=Callable[..., Any])


@overload
def hookimpl(__func: F) -> F:
    ...


@overload
def hookimpl(**kwargs: Any) -> Callable[[F], F]:
    ...


def hookimpl(*args: Any, **kwargs: Any) -> Any:
    return pluggy.HookimplMarker(__name__)(*args, **kwargs)


def version() -> str:
    return metadata.version(__name__)


@cache
def plugin_manager(s: settings.Settings) -> pm.PluginManager:
    return pm.PluginManager.get(s)


execpath: Final = (
    sys.executable
    if getattr(sys, "frozen", False)
    else f"{sys.executable} -m {__name__}"
)
