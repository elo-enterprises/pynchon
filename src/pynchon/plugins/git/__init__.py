""" pynchon.plugins.git
"""
from pynchon import models
from pynchon.util import lme, typing

from .config import GitConfig

LOGGER = lme.get_logger(__name__)


class Git(models.Provider):
    """Context for git"""

    priority = 0
    name = 'git'
    defaults: typing.Dict = dict()
    config_class = GitConfig

    # @classmethod
    # def init_cli(kls):
    #     pass
