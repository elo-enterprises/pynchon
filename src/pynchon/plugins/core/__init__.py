""" pynchon.plugins.Core
"""
from pynchon import models
from pynchon.api import project
from pynchon.bin import entry
from pynchon.util import lme, typing

from .config import CoreConfig

LOGGER = lme.get_logger(__name__)


class Core(models.Planner):
    """Core Plugin"""

    name = "core"
    config_kls = CoreConfig
    contribute_plan_apply = False

    @typing.classproperty
    def click_group(kls):
        kls._finalized_click_groups[kls] = entry.entry
        return kls._finalized_click_groups[kls]

    def plan(self, config=None) -> typing.List:
        """Creates a plan for all plugins"""
        raise NotImplementedError()

    def apply(self, config=None) -> None:
        """Executes the result returned by planner"""
        raise NotImplementedError()

    def config(self):
        """Show current project config (with templating/interpolation)"""
        return project.get_config()

    @classmethod
    def get_current_config(kls):
        """ """
        from pynchon import config as config_mod

        result = getattr(config_mod, getattr(kls.config_kls, 'config_key', kls.name))
        return result

    def raw(self) -> None:
        """
        Returns (almost) raw config,
        before templating & interpolation
        """
        from pynchon.config import RAW

        return RAW