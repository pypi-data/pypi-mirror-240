from __future__ import annotations

from datetime import datetime
from functools import partial
from typing import Any

import attrs
import click

from .. import cmd, postgresql, types
from ..cli.instance import instance_identifier
from ..cli.util import (
    Command,
    OutputFormat,
    instance_identifier_option,
    output_format_option,
    pass_component_settings,
    pass_ctx,
    print_json_for,
    print_table_for,
)
from ..ctx import Context
from ..models import system
from ..settings import _pgbackrest
from . import base, models, repo_path

pass_pgbackrest_settings = partial(pass_component_settings, base, "pgbackrest")


@click.command(
    "pgbackrest",
    hidden=True,
    cls=Command,
    context_settings={"ignore_unknown_options": True},
)
@instance_identifier_option
@click.argument("command", nargs=-1, type=click.UNPROCESSED)
@pass_pgbackrest_settings
@click.pass_context
def pgbackrest(
    context: click.Context,
    /,
    settings: _pgbackrest.Settings,
    command: tuple[str, ...],
    **kwargs: Any,
) -> None:
    """Proxy to pgbackrest operations on an instance"""
    s = context.obj.instance.service(models.Service)
    cmd_args = base.make_cmd(s.stanza, settings, *command)
    cmd.run(cmd_args, capture_output=False, check=True)


@click.command("backup", cls=Command)
@instance_identifier(nargs=1)
@click.option(
    "--type",
    "backup_type",
    type=click.Choice([t.name for t in types.BackupType]),
    default=types.BackupType.default().name,
    help="Backup type",
    callback=lambda ctx, param, value: types.BackupType(value),
)
@pass_pgbackrest_settings
@pass_ctx
def instance_backup(
    ctx: Context,
    settings: _pgbackrest.Settings,
    instance: system.Instance,
    backup_type: types.BackupType,
) -> None:
    """Back up PostgreSQL INSTANCE"""
    with ctx.lock:
        repo_path.backup(instance, settings, type=backup_type)


@click.command("restore", cls=Command)
@instance_identifier(nargs=1)
@click.option("--label", help="Label of backup to restore")
@click.option("--date", type=click.DateTime(), help="Date of backup to restore")
@pass_pgbackrest_settings
@pass_ctx
def instance_restore(
    ctx: Context,
    settings: _pgbackrest.Settings,
    instance: system.Instance,
    label: str | None,
    date: datetime | None,
) -> None:
    """Restore PostgreSQL INSTANCE"""
    postgresql.check_status(instance, types.Status.not_running)
    if label is not None and date is not None:
        raise click.BadArgumentUsage(
            "--label and --date arguments are mutually exclusive"
        ) from None
    with ctx.lock:
        base.restore(ctx, instance, settings, label=label, date=date)


@click.command("backups", cls=Command)
@output_format_option
@instance_identifier(nargs=1)
@pass_pgbackrest_settings
def instance_backups(
    settings: _pgbackrest.Settings,
    instance: system.Instance,
    output_format: OutputFormat,
) -> None:
    """List available backups for INSTANCE"""
    values = list(map(attrs.asdict, base.iter_backups(instance, settings)))
    if output_format == OutputFormat.json:
        print_json_for(values)
    else:
        print_table_for(values, title=f"Available backups for instance {instance}")
