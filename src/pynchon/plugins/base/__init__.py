""" pynchon.plugins.base
"""
from pynchon.bin import groups, common
from pynchon.util import lme, typing
from pynchon.models import Plugin

LOGGER = lme.get_logger(__name__)
from .config import BaseConfig


class Base(Plugin):
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

    @common.groop("api", parent=groups.gen)
    def gen_api() -> None:
        """
        Generate API docs from python modules, packages, etc
        """

    @common.groop("cli", parent=groups.gen)
    def gen_cli():
        """Generate CLI docs"""

    def config_raw(self) -> None:
        """
        shows raw-config (no interpolation or templating)
        """
        from pynchon.config import RAW

        return RAW
