""" pynchon.plugins.gen
"""
from pynchon import models
from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class Generators(models.CliAliases):
    """
    Namespace for rendering docs-generation commands from other plugins
    """

    name = cli_name = 'gen'
    defaults = dict()
    priority = -1
    config_kls = None
    cli_includes: typing.List[typing.Callable] = []

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
