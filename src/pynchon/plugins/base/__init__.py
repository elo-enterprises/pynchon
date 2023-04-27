""" pynchon.plugins.base
"""
from pynchon import models

# from pynchon.bin import common
from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)
from .config import BaseConfig


class Base(models.BasePlugin):
    """ """

    name = "base"
    config_kls = BaseConfig
    contribute_plan_apply = False

    @staticmethod
    def init_cli_group(kls):
        from pynchon.bin.entry import entry

        return entry

    def plan(self, config=None) -> typing.List:
        """Creates a plan for all plugins"""
        self.state = config
        return []

    def apply(self, config=None) -> None:
        """Executes the result returned by planner"""
        plan = self.plan(config=config)
        from pynchon.util.os import invoke

        return [invoke(p).succeeded for p in plan]

    def config(self):
        """Show current project config (with templating/interpolation)"""
        from pynchon.api import project

        return project.get_config()

    @classmethod
    def get_current_config(kls):
        """ """
        from pynchon import config as config_mod

        result = getattr(config_mod, getattr(kls.config_kls, 'config_key', kls.name))
        return result

    # def plan(self, config) -> typing.List[str]:
    #     return []

    def raw(self) -> None:
        """
        Returns (almost) raw config,
        before templating & interpolation
        """
        from pynchon.config import RAW

        return RAW
