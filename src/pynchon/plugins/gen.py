""" pynchon.plugins.gen
"""
import os

from pynchon import abcs, models
from pynchon.util import lme, typing, files  # , files
from pynchon.util.os import invoke

# from .config import ScaffoldingConfig, ScaffoldingItem

LOGGER = lme.get_logger(__name__)
from pynchon.util import tagging


class Generators(models.ContextPlugin):
    cli_label = 'collector'
    name = cli_name = 'gen'
    defaults = dict()
    priority = -1
    config_kls = None
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
