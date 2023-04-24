""" pynchon.plugins.base
"""
from pynchon.bin import groups
from pynchon.util import lme, typing
from pynchon.models import Plugin
from pynchon.bin.common import kommand, groop

LOGGER = lme.get_logger(__name__)


class Base(Plugin):
    """ """

    name = "base"
    config_kls = dict
    defaults = dict()

    def plan(self, config) -> typing.List[str]:
        return []

    @groop("api", parent=groups.gen)
    def gen_api() -> None:
        """
        Generate API docs from python modules, packages, etc
        """

    @groop("cli", parent=groups.gen)
    def gen_cli():
        """Generate CLI docs"""

    @staticmethod
    def init_cli(kls):
        """pynchon.bin.gen:
        Option parsing for the `gen` subcommand
        """
