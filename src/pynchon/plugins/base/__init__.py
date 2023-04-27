""" pynchon.plugins.base
"""
from pynchon import models

from pynchon.util import lme, typing
from pynchon.bin import entry
from pynchon.api import project
from .config import BaseConfig

LOGGER = lme.get_logger(__name__)


class Base(models.Planner):
    """ Core Plugin """

    name = "base"
    config_kls = BaseConfig
    contribute_plan_apply = False

    @staticmethod
    def init_cli_group(kls):
        return entry.entry

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
