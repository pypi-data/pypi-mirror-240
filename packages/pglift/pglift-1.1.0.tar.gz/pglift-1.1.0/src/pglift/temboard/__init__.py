from __future__ import annotations

import logging
from collections.abc import Iterator
from typing import Any

from pgtoolkit.conf import Configuration
from pydantic import Field

from .. import hookimpl
from .. import service as service_mod
from .. import systemd, util
from ..ctx import Context
from ..models import interface, system
from ..settings import Settings
from ..types import Status
from . import impl, models
from .impl import available as available
from .impl import get_settings

logger = logging.getLogger(__name__)


def register_if(settings: Settings) -> bool:
    return available(settings) is not None


@hookimpl
def site_configure_install(settings: Settings) -> None:
    s = get_settings(settings)
    logger.info("creating temboard log directory")
    s.logpath.mkdir(mode=0o740, parents=True, exist_ok=True)


@hookimpl
def site_configure_uninstall(settings: Settings) -> None:
    s = get_settings(settings)
    logger.info("deleting temboard log directory")
    util.rmtree(s.logpath)


@hookimpl
def site_configure_installed(settings: Settings) -> bool:
    s = get_settings(settings)
    if not s.logpath.exists():
        logger.error("temBoard log directory '%s' missing", s.logpath)
        return False
    return True


@hookimpl
def system_lookup(instance: system.PostgreSQLInstance) -> models.Service | None:
    settings = get_settings(instance._settings)
    return impl.system_lookup(instance.qualname, settings)


@hookimpl
def interface_model() -> tuple[str, Any, Any]:
    return (
        models.ServiceManifest.__service__,
        models.ServiceManifest,
        Field(
            default=models.ServiceManifest(),
            description="Configuration for the temBoard service, if enabled in site settings.",
        ),
    )


@hookimpl
def get(instance: system.Instance) -> models.ServiceManifest | None:
    try:
        s = instance.service(models.Service)
    except ValueError:
        return None
    else:
        return models.ServiceManifest(port=s.port)


SYSTEMD_SERVICE_NAME = "pglift-temboard_agent@.service"


@hookimpl
def systemd_unit_templates(
    settings: Settings, content: bool
) -> Iterator[str] | Iterator[tuple[str, str]]:
    if not content:
        yield SYSTEMD_SERVICE_NAME
        return
    s = get_settings(settings)
    configpath = str(s.configpath).replace("{name}", "%i")
    yield SYSTEMD_SERVICE_NAME, systemd.template(SYSTEMD_SERVICE_NAME).format(
        executeas=systemd.executeas(settings),
        configpath=configpath,
        execpath=str(s.execpath),
    )


@hookimpl
def instance_configured(
    ctx: Context, manifest: interface.Instance, config: Configuration
) -> None:
    """Install temboard agent for an instance when it gets configured."""
    settings = get_settings(ctx.settings)
    impl.setup(ctx, manifest, settings, config)


@hookimpl
def instance_started(ctx: Context, instance: system.Instance) -> None:
    """Start temboard agent service."""
    try:
        service = instance.service(models.Service)
    except ValueError:
        return
    impl.start(ctx, service)


@hookimpl
def instance_stopped(ctx: Context, instance: system.Instance) -> None:
    """Stop temboard agent service."""
    try:
        service = instance.service(models.Service)
    except ValueError:
        return
    impl.stop(ctx, service)


@hookimpl
def instance_dropped(ctx: Context, instance: system.Instance) -> None:
    """Uninstall temboard from an instance being dropped."""
    settings = get_settings(instance._settings)
    manifest = interface.Instance(name=instance.name, version=instance.version)
    impl.revert_setup(ctx, manifest, settings, instance.config())


@hookimpl
def rolename(settings: Settings) -> str:
    assert settings.temboard
    return settings.temboard.role


@hookimpl
def role(settings: Settings, manifest: interface.Instance) -> interface.Role:
    name = rolename(settings)
    service_manifest = manifest.service_manifest(models.ServiceManifest)
    return interface.Role(
        name=name, password=service_manifest.password, login=True, superuser=True
    )


@hookimpl
def instance_status(
    ctx: Context, instance: system.Instance
) -> tuple[Status, str] | None:
    try:
        service = instance.service(models.Service)
    except ValueError:
        return None
    return (service_mod.status(ctx, service), "temBoard")
