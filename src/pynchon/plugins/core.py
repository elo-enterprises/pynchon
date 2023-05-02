""" pynchon.plugins.Core
"""
from pynchon import models, cli
from pynchon.api import project
from pynchon.bin import entry
from pynchon.core import Config as CoreConfig
from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class Core(models.Planner):
    """Core Plugin"""

    name = "core"
    config_class = CoreConfig
    contribute_plan_apply = False

    @typing.classproperty
    def click_group(kls):
        kls._finalized_click_groups[kls] = entry.entry
        return kls._finalized_click_groups[kls]

    @classmethod
    def get_current_config(kls):
        """ """
        from pynchon import config as config_mod

        result = getattr(config_mod, getattr(kls.config_class, 'config_key', kls.name))
        return result

    def plan(self, config=None) -> typing.List:
        """Creates a plan for all plugins"""
        raise NotImplementedError()

    def apply(self, config=None) -> None:
        """Executes the result returned by planner"""
        raise NotImplementedError()

    def config(self):
        """Show current project config (with templating/interpolation)"""
        return project.get_config()

    @cli.click.option('--bash', default=False, is_flag=True, help='bootstrap bash')
    def bootstrap(self, bash: bool = False, strict: bool = False) -> None:
        """
        bootstrappery
        """
        if bash:
            return 'alias p=pynchon'

    def raw(self) -> None:
        """
        Returns (almost) raw config,
        without interpolation
        """
        from pynchon.config import RAW

        return RAW
