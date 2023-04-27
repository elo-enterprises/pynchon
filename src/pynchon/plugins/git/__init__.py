""" pynchon.plugins.git
"""
from pynchon import models
from pynchon.util import lme, typing

from .config import GitConfig

LOGGER = lme.get_logger(__name__)


class Git(models.ContextPlugin):
    """ """

    priority = 0
    name = 'git'
    defaults: typing.Dict = dict()
    config_kls = GitConfig

    @staticmethod
    def init_cli(kls):
        pass
