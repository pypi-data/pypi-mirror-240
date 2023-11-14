from __future__ import annotations

import functools
import logging
import os
import pwd
import subprocess
from typing import Any, Callable, Literal

from typing_extensions import TypeAlias

from .. import cmd, exceptions, util
from ..ctx import Context
from ..settings import Settings, _systemd
from ..types import CompletedProcess

logger = logging.getLogger(__name__)


def template(name: str) -> str:
    return util.template("systemd", name)


def executeas(settings: Settings) -> str:
    """Return User/Group options for systemd unit depending on settings."""
    assert settings.systemd
    if settings.systemd.user:
        return ""
    user, group = settings.sysuser
    return "\n".join([f"User={user}", f"Group={group}"])


def environment(value: dict[str, Any]) -> str:
    """Format Environment options to be inserted in a systemd unit.

    >>> print(environment({"foo": "bar", "active": 1}))
    Environment="active=1"
    Environment="foo=bar"
    >>> environment({})
    ''
    """
    return "\n".join([f'Environment="{k}={v}"' for k, v in sorted(value.items())])


Action: TypeAlias = Literal[
    "daemon-reload",
    "disable",
    "enable",
    "is-active",
    "is-enabled",
    "reload",
    "restart",
    "show",
    "show-environment",
    "start",
    "status",
    "stop",
]


def systemctl_cmd(
    settings: _systemd.Settings, action: Action, *options: str, unit: str | None
) -> list[str]:
    sflag = "--user" if settings.user else "--system"
    cmd_args = [str(settings.systemctl), sflag] + list(options) + [action]
    if unit is not None:
        cmd_args.append(unit)
    if settings.sudo:
        cmd_args.insert(0, "sudo")
    return cmd_args


@functools.cache
def systemctl_env(settings: _systemd.Settings) -> dict[str, str]:
    """Return additional environment variables suitable to run systemctl --user commands.

    To run systemctl --user there must be login session for the current user
    and both XDG_RUNTIME_DIR and DBUS_SESSION_BUS_ADDRESS must be set.
    In some cases like using sudo through ansible, we might not have access to
    required environment variables.

    First check session exists and get XDG_RUNTIME_DIR using `loginctl show-user`. If this is not a
    lingering session display a warning message

    Then if DBUS_SESSION_BUS_ADDRESS is not set, get it by running `systemctl
    --user show-environment`.
    """
    if not settings.user:
        return {}
    user = pwd.getpwuid(os.getuid()).pw_name
    proc = cmd.run(
        [
            "loginctl",
            "show-user",
            user,
            "--value",
            "--property",
            "RuntimePath",
            "--property",
            "Linger",
        ],
        check=True,
    )
    env = {}
    rpath, linger = proc.stdout.splitlines()
    if linger == "no":
        logger.warning(
            "systemd lingering for user %s is not enabled, "
            "pglift services won't start automatically at boot",
            user,
        )
    if "XDG_RUNTIME_DIR" not in os.environ:
        env["XDG_RUNTIME_DIR"] = rpath
    if "DBUS_SESSION_BUS_ADDRESS" not in os.environ:
        proc = cmd.run(
            ["systemctl", "--user", "show-environment"],
            env=os.environ | env,
            check=True,
        )
        for line in proc.stdout.splitlines():
            if line.startswith("DBUS_SESSION_BUS_ADDRESS="):
                env["DBUS_SESSION_BUS_ADDRESS"] = line.split("=", 1)[1]
                break
        else:
            raise exceptions.SystemError(
                "could not find expected DBUS_SESSION_BUS_ADDRESS "
                "in `systemctl --user show-environment` output"
            )
    return env


def systemctl(
    settings: _systemd.Settings,
    action: Action,
    *options: str,
    unit: str | None,
    check: bool = True,
) -> CompletedProcess:
    env = systemctl_env(settings)
    return cmd.run(
        systemctl_cmd(settings, action, *options, unit=unit),
        env=os.environ | env,
        check=check,
    )


def install(name: str, content: str, settings: _systemd.Settings) -> None:
    path = settings.unit_path / name
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text() != content:
        if path.exists():
            raise exceptions.FileExistsError(f"{path} exists, not overwriting")
        path.write_text(content)
        logger.info("installed %s systemd unit at %s", name, path)


def uninstall(name: str, settings: _systemd.Settings) -> None:
    path = settings.unit_path / name
    logger.info("removing %s systemd unit (%s)", name, path)
    path.unlink(missing_ok=True)


def installed(name: str, settings: _systemd.Settings) -> bool:
    return (settings.unit_path / name).exists()


def daemon_reload(systemd_settings: _systemd.Settings) -> None:
    systemctl(systemd_settings, "daemon-reload", unit=None)


def is_enabled(ctx: Context, unit: str) -> bool:
    assert ctx.settings.systemd is not None
    r = systemctl(ctx.settings.systemd, "is-enabled", "--quiet", unit=unit, check=False)
    return r.returncode == 0


def enable(ctx: Context, unit: str) -> None:
    if is_enabled(ctx, unit):
        logger.debug("systemd unit %s already enabled, 'enable' action skipped", unit)
        return
    assert ctx.settings.systemd is not None
    systemctl(ctx.settings.systemd, "enable", unit=unit)


def disable(ctx: Context, unit: str, *, now: bool = True) -> None:
    if not is_enabled(ctx, unit):
        logger.debug("systemd unit %s not enabled, 'disable' action skipped", unit)
        return
    assert ctx.settings.systemd is not None
    systemctl(ctx.settings.systemd, "disable", *(("--now",) if now else ()), unit=unit)


F = Callable[["Context", str], None]


def log_status(fn: F) -> F:
    @functools.wraps(fn)
    def wrapper(ctx: Context, unit: str) -> None:
        try:
            return fn(ctx, unit)
        except (subprocess.CalledProcessError, SystemExit):
            # Ansible runner would call sys.exit(1), hence SystemExit.
            logger.error(status(ctx, unit))
            raise

    return wrapper


def status(ctx: Context, unit: str) -> str:
    assert ctx.settings.systemd is not None
    proc = systemctl(
        ctx.settings.systemd,
        "status",
        "--full",
        "--lines=100",
        "status",
        unit=unit,
        check=False,
    )
    # https://www.freedesktop.org/software/systemd/man/systemctl.html#Exit%20status
    if proc.returncode not in (0, 1, 2, 3, 4):
        raise exceptions.CommandError(
            proc.returncode, proc.args, proc.stdout, proc.stderr
        )
    return proc.stdout


@log_status
def start(ctx: Context, unit: str) -> None:
    assert ctx.settings.systemd is not None
    systemctl(ctx.settings.systemd, "start", unit=unit)


@log_status
def stop(ctx: Context, unit: str) -> None:
    assert ctx.settings.systemd is not None
    systemctl(ctx.settings.systemd, "stop", unit=unit)


@log_status
def reload(ctx: Context, unit: str) -> None:
    assert ctx.settings.systemd is not None
    systemctl(ctx.settings.systemd, "reload", unit=unit)


@log_status
def restart(ctx: Context, unit: str) -> None:
    assert ctx.settings.systemd is not None
    systemctl(ctx.settings.systemd, "restart", unit=unit)


def is_active(ctx: Context, unit: str) -> bool:
    assert ctx.settings.systemd is not None
    r = systemctl(
        ctx.settings.systemd, "is-active", "--quiet", "--user", unit=unit, check=False
    )
    return r.returncode == 0


def get_property(ctx: Context, unit: str, property: str) -> str:
    assert ctx.settings.systemd is not None
    r = systemctl(
        ctx.settings.systemd, "show", "--user", "--property", property, unit=unit
    )
    return r.stdout
