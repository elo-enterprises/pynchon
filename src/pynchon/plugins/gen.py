""" pynchon.plugins.gen
"""

from pynchon import abcs, cli, models  # noqa
from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class Generators(models.NameSpace):
    """Collects `gen` commands from other plugins"""

    name = cli_name = "gen"
    priority = 1
    config_class = None

    @classmethod
    def siblings_with_subcommand(
        kls, target_name: str, siblings: typing.Dict = {}
    ) -> typing.Dict[object, typing.Callable]:
        result = {}
        for name, obj in siblings.items():
            if obj.name == "core":
                continue
            elif target_name in dir(obj):
                result[obj] = getattr(obj, target_name)
        return result

    @classmethod
    def acquire_cli_subcommands(kls, target_name, **kwargs) -> None:
        cmd_names = []

        def acqcmd(cmd, group=None):
            cmd_name = getattr(cmd, "name", getattr(cmd, "__name__", ""))
            if cmd_name in [target_name]:
                cmd_name = sibling.name
            if cmd_name in cmd_names:
                cmd_name = f"{sibling.name}-{cmd_name}"
            cmd_name = cmd_name.replace("_", "-")
            if cmd_name in cmd_names:
                raise Exception(f"collision acquiring subcommand: [{cmd_name}, {cmd}]")
            assert cmd_name, [cmd]
            gname = f"{group.name} " if group else ""
            cname = f"{gname}{cmd_name}"
            ocli = f"`{sibling.cli_path} {cname}`"
            descr = "from" if group else "to"
            kls.click_acquire(
                cmd,
                copy=True,
                name=cmd_name,
                help=f"Alias {descr} {ocli}",
            )

        for sibling, cmd in kls.siblings_with_subcommand("gen", **kwargs).items():
            LOGGER.info(f"acquiring {cmd} (type={type(cmd)}) from {sibling}")
            if isinstance(cmd, cli.click.Group):
                [acqcmd(c, group=cmd) for c in cmd.commands.values()]
            else:
                acqcmd(cmd)

    @classmethod
    def init_cli(kls) -> cli.click.Group:
        """ """
        result = super(kls, kls).init_cli()
        kls.acquire_cli_subcommands("gen", siblings=kls.siblings)
        return result
