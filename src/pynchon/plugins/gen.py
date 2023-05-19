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

    @typing.classproperty
    def siblings_with_gen(kls):
        result = {}
        for name, obj in kls.siblings.items():
            if obj.name == "core":
                continue
            elif "gen" in dir(obj):
                result[obj] = obj.gen
        return result

    @classmethod
    def init_cli(kls) -> cli.click.Group:
        """ """
        result = super(kls, kls).init_cli()
        for sibling, cmd in kls.siblings_with_gen.items():
            LOGGER.info(f"acquiring {cmd} from {sibling}")
            kls.click_acquire(
                cmd,
                copy=True,
                name=sibling.name,
                help=f"Alias for `{kls.click_entry.name} {sibling.name} gen`",
            )
        return result
