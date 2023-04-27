"""
"""
from pynchon import abcs, models


class GlobalsConfig(abcs.Config):
    """ """

    defaults = dict()
    config_key = 'globals'


class Globals(models.ContextPlugin):
    """context-provider: pynchon-globals"""

    priority = 2
    name = 'globals'
    defaults = dict()
    config_kls = GlobalsConfig
