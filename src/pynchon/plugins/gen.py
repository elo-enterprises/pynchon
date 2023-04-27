""" pynchon.plugins.gen
"""
from pynchon import models
from pynchon.util import lme, typing

# , files  # , files
# from pynchon.util.os import invoke

# from .config import ScaffoldingConfig, ScaffoldingItem

LOGGER = lme.get_logger(__name__)
# from pynchon.util import tagging


class Generators(models.CliAliases):
    """
    Namespace for rendering docs-generation commands from other plugins
    """

    name = cli_name = 'gen'
    defaults = dict()
    priority = -1
    config_kls = None

    def placeholder(self) -> typing.Dict:
        return dict()

    # @common.groop("api", parent=groups.gen)
    # def gen_api() -> None:
    #     """
    #     Generate API docs from python modules, packages, etc
    #     """
    #
    # @common.groop("cli", parent=groups.gen)
    # def gen_cli():
    #     """Generate CLI docs"""
    #
