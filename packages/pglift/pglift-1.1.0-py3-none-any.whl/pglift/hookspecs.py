from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Literal, Optional

import click
import pluggy
from pgtoolkit.conf import Configuration
from pydantic.fields import FieldInfo
from typing_extensions import TypeAlias

from . import __name__ as pkgname

if TYPE_CHECKING:
    from .ctx import Context
    from .models import interface, system
    from .models.system import BaseInstance, Instance, PostgreSQLInstance
    from .pm import PluginManager
    from .postgresql import Standby
    from .settings import Settings
    from .types import ConfigChanges, ServiceManifest, Status

hookspec = pluggy.HookspecMarker(pkgname)

FirstResult: TypeAlias = Optional[Literal[True]]


@hookspec
def site_configure_install(
    settings: Settings, pm: PluginManager, header: str, env: str | None
) -> None:
    """Global configuration hook."""
    raise NotImplementedError


@hookspec
def site_configure_uninstall(
    settings: Settings, pm: PluginManager, ctx: Context
) -> None:
    """Global configuration hook."""
    raise NotImplementedError


@hookspec
def systemd_unit_templates(
    settings: Settings, env: dict[str, Any], content: bool
) -> Iterator[str] | Iterator[tuple[str, str]]:
    """Systemd unit templates used by each plugin."""
    raise NotImplementedError


@hookspec
def site_configure_installed(settings: Settings, pm: PluginManager) -> bool:
    """Check installation in each plugin, returning True is installation is okay."""
    raise NotImplementedError


@hookspec
def cli() -> click.Command:
    """Return command-line entry point as click Command (or Group) for the plugin."""
    raise NotImplementedError


@hookspec
def instance_cli(group: click.Group) -> None:
    """Extend 'group' with extra commands from the plugin."""
    raise NotImplementedError


@hookspec
def system_lookup(instance: PostgreSQLInstance) -> Any | None:
    """Look up for the satellite service object on system that matches specified instance."""
    raise NotImplementedError


@hookspec
def get(instance: Instance) -> ServiceManifest | None:
    """Return the description the satellite service bound to specified instance."""
    raise NotImplementedError


@hookspec
def interface_model() -> tuple[str, Any, Any]:
    """The interface model for satellite component provided plugin."""
    raise NotImplementedError


@hookspec
def instance_settings(
    manifest: interface.Instance, instance: BaseInstance
) -> Configuration:
    """Called before the PostgreSQL instance settings is written."""
    raise NotImplementedError


@hookspec(firstresult=True)
def standby_model(
    ctx: Context,
    instance: system.Instance,
    standby: system.Standby,
    running: bool,
) -> Standby | None:
    """The interface model holding standby information, if 'instance' is a
    plain standby.

    Only one implementation should be invoked so call order and returned value
    matter.

    An implementation may raise a ValueError to interrupt hook execution.
    """
    raise NotImplementedError


@hookspec
def instance_configured(
    ctx: Context,
    manifest: interface.Instance,
    config: Configuration,
    changes: ConfigChanges,
    creating: bool,
    upgrading_from: Instance | None,
) -> None:
    """Called when the PostgreSQL instance got (re-)configured."""
    raise NotImplementedError


@hookspec
def instance_dropped(ctx: Context, instance: Instance) -> None:
    """Called when the PostgreSQL instance got dropped."""
    raise NotImplementedError


@hookspec
def instance_started(ctx: Context, instance: Instance) -> None:
    """Called when the PostgreSQL instance got started."""
    raise NotImplementedError


@hookspec
def instance_stopped(ctx: Context, instance: Instance) -> None:
    """Called when the PostgreSQL instance got stopped."""
    raise NotImplementedError


@hookspec
def instance_promoted(instance: Instance) -> None:
    """Called when the PostgreSQL instance got promoted."""
    raise NotImplementedError


@hookspec
def instance_env(instance: Instance) -> dict[str, str]:
    """Return environment variables for instance defined by the plugin."""
    raise NotImplementedError


@hookspec
def instance_upgraded(old: PostgreSQLInstance, new: PostgreSQLInstance) -> None:
    """Called when 'old' PostgreSQL instance got upgraded as 'new'."""
    raise NotImplementedError


@hookspec
def instance_status(ctx: Context, instance: Instance) -> tuple[Status, str] | None:
    """Return instance status"""
    raise NotImplementedError


@hookspec
def role_model() -> tuple[str, Any, FieldInfo]:
    """Return the definition for an extra field to the Role interface model
    provided by a plugin.
    """
    raise NotImplementedError


@hookspec
def role_change(role: interface.BaseRole, instance: PostgreSQLInstance) -> bool:
    """Called when 'role' changed in 'instance' (be it a create, an update or a deletion).

    Return True if any change happened during hook invocation.
    """
    raise NotImplementedError


@hookspec
def role_inspect(instance: PostgreSQLInstance, name: str) -> dict[str, Any]:
    """Return extra attributes for 'name' role from plugins."""
    raise NotImplementedError


@hookspec
def rolename(settings: Settings) -> str:
    """Return the name of role used by a plugin."""
    raise NotImplementedError


@hookspec
def role(settings: Settings, manifest: interface.Instance) -> interface.Role:
    """Return the role used by a plugin, to be created at instance creation."""
    raise NotImplementedError


@hookspec
def database(settings: Settings, manifest: interface.Instance) -> interface.Database:
    """Return the database used by a plugin, to be created at instance creation."""
    raise NotImplementedError


@hookspec(firstresult=True)
def initdb(
    ctx: Context, manifest: interface.Instance, instance: BaseInstance
) -> FirstResult:
    """Initialize a PostgreSQL database cluster.

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec
def patroni_create_replica_method(
    manifest: interface.Instance,
    instance: BaseInstance,
) -> tuple[str, dict[str, Any]] | None:
    raise NotImplementedError


@hookspec(firstresult=True)
def postgresql_editable_conf(ctx: Context, instance: BaseInstance) -> str | None:
    """Return the content of editable postgresql.conf.

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def configure_postgresql(
    ctx: Context,
    manifest: interface.Instance,
    configuration: Configuration,
    instance: BaseInstance,
) -> ConfigChanges | None:
    """Configure PostgreSQL and return 'changes' to postgresql.conf.

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def configure_auth(
    settings: Settings, instance: BaseInstance, manifest: interface.Instance
) -> bool | None:
    """Configure authentication for PostgreSQL (pg_hba.conf, pg_ident.conf).

    Only one implementation should be invoked so call order and returned value
    matter.

    If returning True, PostgreSQL should be restarted by the caller.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def start_postgresql(
    ctx: Context, instance: PostgreSQLInstance, foreground: bool, wait: bool
) -> FirstResult:
    """Start PostgreSQL for specified 'instance'.

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def stop_postgresql(
    ctx: Context,
    instance: PostgreSQLInstance,
    mode: str,
    wait: bool,
    deleting: bool,
) -> FirstResult:
    """Stop PostgreSQL for specified 'instance'.

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def restart_postgresql(
    ctx: Context, instance: Instance, mode: str, wait: bool
) -> FirstResult:
    """Restart PostgreSQL for specified 'instance'.

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def reload_postgresql(ctx: Context, instance: Instance) -> FirstResult:
    """Reload PostgreSQL configuration for 'instance'.

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def promote_postgresql(ctx: Context, instance: Instance) -> FirstResult:
    """Promote PostgreSQL for 'instance'.

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def postgresql_service_name(ctx: Context, instance: BaseInstance) -> str:
    """Return the system service name (e.g.  postgresql).

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def enable_service(ctx: Context, service: str, name: str | None) -> FirstResult:
    """Enable a service

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def disable_service(
    ctx: Context, service: str, name: str | None, now: bool | None
) -> FirstResult:
    """Disable a service

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def start_service(ctx: Context, service: str, name: str | None) -> FirstResult:
    """Start a service for a plugin

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def stop_service(ctx: Context, service: str, name: str | None) -> FirstResult:
    """Stop a service for a plugin

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def restart_service(ctx: Context, service: str, name: str | None) -> FirstResult:
    """Restart a service for a plugin

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def service_status(ctx: Context, service: str, name: str | None) -> Status:
    """Return a service status for a plugin

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def schedule_service(ctx: Context, service: str, name: str) -> FirstResult:
    """Schedule a job through timer

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def unschedule_service(
    ctx: Context, service: str, name: str, now: bool | None
) -> FirstResult:
    """Unchedule a job

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def start_timer(ctx: Context, service: str, name: str) -> FirstResult:
    """Start a timer

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec(firstresult=True)
def stop_timer(ctx: Context, service: str, name: str) -> FirstResult:
    """Stop a timer

    Only one implementation should be invoked so call order and returned value
    matter.
    """
    raise NotImplementedError


@hookspec
def logrotate_config(settings: Settings) -> str:
    """Return logrotate configuration for the service matching specified instance."""
    raise NotImplementedError
