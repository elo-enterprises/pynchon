""" pynchon.plugins.base
"""
from pynchon import constants
from pynchon.bin import groups, options, common
from pynchon.util import files, lme, typing
from pynchon.bin.common import kommand, groop
from pynchon.models import Plugin

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
