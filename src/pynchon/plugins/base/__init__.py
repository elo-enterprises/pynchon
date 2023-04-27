""" pynchon.plugins.base
"""
from pynchon.bin import groups, common
from pynchon.util import lme, typing
from pynchon import models

LOGGER = lme.get_logger(__name__)
from .config import BaseConfig


class Base(models.BasePlugin):
    """ """

    name = "base"
    config_kls = BaseConfig

    @staticmethod
    def init_cli_group(kls):
        from pynchon.bin.entry import entry

        return entry

    def plan(self, config=None) -> typing.List:
        """create a plan for all plugins"""
        self.state = config
        return []

    def apply(self, config=None) -> None:
        """execute the result returned by planner"""
        plan = self.plan(config=config)
        from pynchon.util.os import invoke

        return [invoke(p).succeeded for p in plan]

    def config(self):
        """show project config"""
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

    def config_raw(self) -> None:
        """
        Returns (almost) raw config, before templating
        """
        from pynchon.config import RAW

        return RAW
