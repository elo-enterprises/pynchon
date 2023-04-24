""" pynchon.plugins.git
"""
from pynchon.util import lme, typing
from pynchon.models import Plugin

from .config import GitConfig

LOGGER = lme.get_logger(__name__)


class Git(Plugin):
    """ """

    priority = 0
    name = 'git'
    defaults: typing.Dict = dict()
    config_kls = GitConfig

    # @staticmethod
    # def init_cli(kls):
    #     """pynchon.bin.project"""
    #     Plugin.init_cli(kls)
