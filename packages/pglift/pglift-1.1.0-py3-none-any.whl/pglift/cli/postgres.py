from __future__ import annotations

import click

from ..cmd import execute_program
from ..ctx import Context
from ..exceptions import InstanceNotFound
from ..models import system


def instance_from_qualname(
    context: click.Context, param: click.Parameter, value: str
) -> system.PostgreSQLInstance:
    ctx: Context = context.obj.ctx
    try:
        return system.PostgreSQLInstance.from_qualname(value, ctx.settings)
    except (ValueError, InstanceNotFound) as e:
        raise click.BadParameter(str(e), context) from None


@click.command("postgres", hidden=True)
@click.argument("instance", callback=instance_from_qualname)
def cli(instance: system.Instance) -> None:
    """Start postgres for specified INSTANCE, identified as <version>-<name>."""
    cmd = [str(instance.bindir / "postgres"), "-D", str(instance.datadir)]
    execute_program(cmd)
