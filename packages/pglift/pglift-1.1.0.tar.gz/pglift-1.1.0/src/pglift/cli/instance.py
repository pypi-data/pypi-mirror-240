from __future__ import annotations

from collections.abc import Sequence
from typing import IO, Any, Callable

import attrs
import click
from pydantic.utils import deep_update

from .. import instances, plugin_manager, postgresql, privileges, task
from ..ctx import Context
from ..models import helpers, interface, system
from ..settings._postgresql import PostgreSQLVersion
from ..types import Status
from .util import (
    Callback,
    CompositeCommandGroup,
    Obj,
    OutputFormat,
    PluggableCommandGroup,
    _list_instances,
    dry_run_option,
    foreground_option,
    instance_lookup,
    output_format_option,
    pass_ctx,
    print_argspec,
    print_json_for,
    print_schema,
    print_table_for,
)


def instance_identifier(
    nargs: int = 1, required: bool = False
) -> Callable[[Callback], Callback]:
    def decorator(fn: Callback) -> Callback:
        command = click.argument(
            "instance",
            nargs=nargs,
            required=required,
            callback=instance_lookup,
            shell_complete=_list_instances,
        )(fn)
        assert command.__doc__
        command.__doc__ += (
            "\n\n    INSTANCE identifies target instance as <version>/<name> where the "
            "<version>/ prefix may be omitted if there is only one instance "
            "matching <name>."
        )
        if not required:
            command.__doc__ += " Required if there is more than one instance on system."
        return command

    return decorator


class InstanceCommands(
    PluggableCommandGroup, CompositeCommandGroup[interface.Instance]
):
    """Group for 'instance' sub-commands handling some of them that require a
    composite interface.Instance model built from registered plugins at
    runtime.
    """

    model = interface.Instance

    def register_plugin_commands(self, obj: Obj) -> None:
        obj.ctx.hook.instance_cli(group=self)


def print_instance_schema(
    context: click.Context, param: click.Parameter, value: bool
) -> None:
    settings = context.obj.ctx.settings
    p = plugin_manager(settings)
    return print_schema(context, param, value, model=interface.Instance.composite(p))


def print_instance_argspec(
    context: click.Context, param: click.Parameter, value: bool
) -> None:
    settings = context.obj.ctx.settings
    model = interface.Instance.composite(plugin_manager(settings))
    print_argspec(context, param, value, model=model)


@click.group(cls=InstanceCommands)
@click.option(
    "--schema",
    is_flag=True,
    callback=print_instance_schema,
    expose_value=False,
    is_eager=True,
    help="Print the JSON schema of instance model and exit.",
)
@click.option(
    "--ansible-argspec",
    is_flag=True,
    callback=print_instance_argspec,
    expose_value=False,
    is_eager=True,
    hidden=True,
    help="Print the Ansible argspec of instance model and exit.",
)
def cli() -> None:
    """Manage instances."""


# Help mypy because click.group() looses the type of 'cls' argument.
assert isinstance(cli, InstanceCommands)


@cli.command_with_composite_model("create")
def _create(Instance: type[interface.Instance]) -> Callback:
    @helpers.parameters_from_model(Instance, "create")
    @click.option(
        "--drop-on-error/--no-drop-on-error",
        default=True,
        help=(
            "On error, drop partially initialized instance by possibly "
            "rolling back operations (true by default)."
        ),
    )
    @pass_ctx
    def command(
        ctx: Context, instance: interface.Instance, drop_on_error: bool
    ) -> None:
        """Initialize a PostgreSQL instance"""
        with ctx.lock:
            if instances.exists(instance.name, instance.version, ctx.settings):
                raise click.ClickException("instance already exists")
            with task.transaction(drop_on_error):
                instances.apply(ctx, instance)

    return command


@cli.command_with_composite_model("alter")
def _alter(Instance: type[interface.Instance]) -> Callback:
    @instance_identifier(nargs=1)
    @helpers.parameters_from_model(Instance, "update", parse_model=False)
    @pass_ctx
    def command(ctx: Context, instance: system.Instance, **changes: Any) -> None:
        """Alter PostgreSQL INSTANCE"""
        with ctx.lock:
            status = postgresql.status(instance)
            values = instances._get(ctx, instance, status).dict(exclude={"settings"})
            values = deep_update(values, changes)
            altered = Instance.parse_obj(values)
            instances.apply(ctx, altered, _is_running=status == Status.running)

    return command


@cli.command("apply", hidden=True)
@click.option("-f", "--file", type=click.File("r"), metavar="MANIFEST", required=True)
@output_format_option
@dry_run_option
@pass_ctx
def apply(
    ctx: Context,
    file: IO[str],
    output_format: OutputFormat,
    dry_run: bool,
) -> None:
    """Apply manifest as a PostgreSQL instance"""
    p = plugin_manager(ctx.settings)
    model = interface.Instance.composite(p)
    instance = model.parse_yaml(file)
    if dry_run:
        ret = interface.InstanceApplyResult(change_state=None)
    else:
        with ctx.lock:
            ret = instances.apply(ctx, instance)
    if output_format == OutputFormat.json:
        print_json_for(ret)


@cli.command("promote")
@instance_identifier(nargs=1)
@pass_ctx
def promote(ctx: Context, instance: system.Instance) -> None:
    """Promote standby PostgreSQL INSTANCE"""
    with ctx.lock:
        instances.promote(ctx, instance)


@cli.command("get")
@output_format_option
@instance_identifier(nargs=1)
@pass_ctx
def get(
    ctx: Context,
    instance: system.Instance,
    output_format: OutputFormat,
) -> None:
    """Get the description of PostgreSQL INSTANCE.

    Unless --output-format is specified, 'settings' and 'state' fields are not
    shown as well as 'standby' information if INSTANCE is not a standby.
    """
    exclude = set()
    if not output_format:
        exclude.update(
            [
                "settings",
                "state",
                "data_directory",
                "wal_directory",
                "powa",
            ]
        )
        if not instance.standby:
            exclude.add("standby")
    m = instances.get(ctx, instance).dict(by_alias=True, exclude=exclude)
    if output_format == OutputFormat.json:
        print_json_for(m)
    else:
        print_table_for([m], box=None)


@cli.command("list")
@click.option(
    "--version",
    type=click.Choice(list(PostgreSQLVersion)),
    help="Only list instances of specified version.",
)
@output_format_option
@pass_ctx
def ls(
    ctx: Context,
    version: PostgreSQLVersion | None,
    output_format: OutputFormat,
) -> None:
    """List the available instances"""

    values = [attrs.asdict(i) for i in instances.ls(ctx.settings, version=version)]
    if output_format == OutputFormat.json:
        print_json_for(values)
    else:
        print_table_for(values)


@cli.command("drop")
@instance_identifier(nargs=-1)
@pass_ctx
def drop(ctx: Context, instance: tuple[system.Instance, ...]) -> None:
    """Drop PostgreSQL INSTANCE"""
    with ctx.lock:
        for i in instance:
            instances.drop(ctx, i)


@cli.command("status")
@instance_identifier(nargs=1)
@click.pass_context
def status(context: click.Context, instance: system.Instance) -> None:
    """Check the status of instance and all satellite components.

    Output the status string value ('running', 'not running') for each component.
    If not all services are running, the command exit code will be 3.
    """
    ctx: Context = context.obj.ctx
    exit_code = Status.running.value
    for status, component in reversed(
        ctx.hook.instance_status(ctx=ctx, instance=instance)
    ):
        if status != Status.running:
            exit_code = Status.not_running.value
        click.echo(f"{component}: {status.name.replace('_', ' ')}")
    context.exit(exit_code)


@cli.command("start")
@instance_identifier(nargs=-1)
@foreground_option
@click.option("--all", "all_instances", is_flag=True, help="Start all instances.")
@pass_ctx
def start(
    ctx: Context,
    instance: tuple[system.Instance, ...],
    foreground: bool,
    all_instances: bool,
) -> None:
    """Start PostgreSQL INSTANCE"""
    if foreground and len(instance) != 1:
        raise click.UsageError(
            "only one INSTANCE argument may be given with --foreground"
        )
    with ctx.lock:
        for i in instance:
            instances.start(ctx, i, foreground=foreground)


@cli.command("stop")
@instance_identifier(nargs=-1)
@click.option("--all", "all_instances", is_flag=True, help="Stop all instances.")
@pass_ctx
def stop(
    ctx: Context, instance: tuple[system.Instance, ...], all_instances: bool
) -> None:
    """Stop PostgreSQL INSTANCE"""
    with ctx.lock:
        for i in instance:
            instances.stop(ctx, i)


@cli.command("reload")
@instance_identifier(nargs=-1)
@click.option("--all", "all_instances", is_flag=True, help="Reload all instances.")
@pass_ctx
def reload(
    ctx: Context, instance: tuple[system.Instance, ...], all_instances: bool
) -> None:
    """Reload PostgreSQL INSTANCE"""
    with ctx.lock:
        for i in instance:
            instances.reload(ctx, i)


@cli.command("restart")
@instance_identifier(nargs=-1)
@click.option("--all", "all_instances", is_flag=True, help="Restart all instances.")
@pass_ctx
def restart(
    ctx: Context, instance: tuple[system.Instance, ...], all_instances: bool
) -> None:
    """Restart PostgreSQL INSTANCE"""
    with ctx.lock:
        for i in instance:
            instances.restart(ctx, i)


@cli.command("exec")
@instance_identifier(nargs=1, required=True)
@click.argument("command", required=True, nargs=-1, type=click.UNPROCESSED)
@pass_ctx
def exec(ctx: Context, instance: system.Instance, command: tuple[str, ...]) -> None:
    """Execute command in the libpq environment for PostgreSQL INSTANCE.

    COMMAND parts may need to be prefixed with -- to separate them from
    options when confusion arises.
    """
    instances.exec(ctx, instance, command)


@cli.command("env")
@instance_identifier(nargs=1)
@output_format_option
@pass_ctx
def env(ctx: Context, instance: system.Instance, output_format: OutputFormat) -> None:
    """Output environment variables suitable to handle to PostgreSQL INSTANCE.

    This can be injected in shell using:

        export $(pglift instance env myinstance)
    """
    instance_env = instances.env_for(ctx, instance, path=True)
    if output_format == OutputFormat.json:
        print_json_for(instance_env)
    else:
        for key, value in sorted(instance_env.items()):
            click.echo(f"{key}={value}")


@cli.command("logs")
@click.option("--follow/--no-follow", "-f/", default=False, help="Follow log output.")
@instance_identifier(nargs=1)
def logs(instance: system.Instance, follow: bool) -> None:
    """Output PostgreSQL logs of INSTANCE.

    This assumes that the PostgreSQL instance is configured to use file-based
    logging (i.e. log_destination amongst 'stderr' or 'csvlog').
    """
    if follow:
        logstream = postgresql.logs(instance)
    else:
        logstream = postgresql.logs(instance, timeout=0)
    try:
        for line in logstream:
            click.echo(line, nl=False)
    except TimeoutError:
        pass
    except FileNotFoundError as e:
        raise click.ClickException(str(e)) from None


@cli.command("privileges")
@instance_identifier(nargs=1)
@click.option(
    "-d",
    "--database",
    "databases",
    multiple=True,
    help="Database to inspect. When not provided, all databases are inspected.",
)
@click.option("-r", "--role", "roles", multiple=True, help="Role to inspect")
@click.option("--default", "defaults", is_flag=True, help="Display default privileges")
@output_format_option
@pass_ctx
def list_privileges(
    ctx: Context,
    instance: system.Instance,
    databases: Sequence[str],
    roles: Sequence[str],
    defaults: bool,
    output_format: OutputFormat,
) -> None:
    """List privileges on INSTANCE's databases."""
    with postgresql.running(ctx, instance):
        try:
            prvlgs = privileges.get(
                ctx, instance, databases=databases, roles=roles, defaults=defaults
            )
        except ValueError as e:
            raise click.ClickException(str(e)) from None
    values = [attrs.asdict(p) for p in prvlgs]
    if output_format == OutputFormat.json:
        print_json_for(values)
    else:
        if defaults:
            title = f"Default privileges on instance {instance}"
        else:
            title = f"Privileges on instance {instance}"
        print_table_for(values, title=title)


@cli.command("upgrade")
@instance_identifier(nargs=1)
@click.option(
    "--version",
    "newversion",
    type=click.Choice(list(PostgreSQLVersion)),
    help="PostgreSQL version of the new instance (default to site-configured value).",
)
@click.option(
    "--name", "newname", help="Name of the new instance (default to old instance name)."
)
@click.option(
    "--port", required=False, type=click.INT, help="Port of the new instance."
)
@click.option(
    "--jobs",
    required=False,
    type=click.INT,
    help="Number of simultaneous processes or threads to use (from pg_upgrade).",
)
@pass_ctx
def upgrade(
    ctx: Context,
    instance: system.Instance,
    newversion: PostgreSQLVersion | None,
    newname: str | None,
    port: int | None,
    jobs: int | None,
) -> None:
    """Upgrade INSTANCE using pg_upgrade"""
    with ctx.lock:
        postgresql.check_status(instance, Status.not_running)
        new_instance = instances.upgrade(
            ctx, instance, version=newversion, name=newname, port=port, jobs=jobs
        )
        instances.start(ctx, new_instance)
