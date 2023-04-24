""" pynchon.plugins.base
"""
from pynchon.bin import groups, common
from pynchon.util import lme, typing
from pynchon.models import Plugin

LOGGER = lme.get_logger(__name__)


class Base(Plugin):
    """ """

    name = "base"
    config_kls = dict
    defaults = dict()

    def plan(self, config) -> typing.List[str]:
        return []

    @common.groop("api", parent=groups.gen)
    def gen_api() -> None:
        """
        Generate API docs from python modules, packages, etc
        """

    @common.groop("cli", parent=groups.gen)
    def gen_cli():
        """Generate CLI docs"""

    @staticmethod
    def init_cli(kls):
        """pynchon.bin.gen:
        Option parsing for the `gen` subcommand
        """
