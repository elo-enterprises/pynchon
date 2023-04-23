""" pynchon.plugins.git
"""
from memoized_property import memoized_property

from pynchon import abcs
from pynchon.bin import groups, common
from pynchon.abcs import Path
from pynchon.util import lme, typing, files
from pynchon.util.os import invoke
from pynchon.bin.entry import entry
from pynchon.models import Plugin

LOGGER = lme.get_logger(__name__)

from .config import GitConfig
class Git(Plugin):
    """ """

    priority = 0
    name = 'git'
    defaults = dict()
    config_kls = GitConfig

    @staticmethod
    def init_cli(kls):
        """pynchon.bin.project"""
        Plugin.init_cli(kls)
