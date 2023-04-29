"""
"""
from pynchon import abcs, models


class GlobalsConfig(abcs.Config):
    """ """

    defaults = dict()
    config_key = 'globals'


class Globals(models.Provider):
    """Context for pynchon globals"""

    priority = 2
    name = 'globals'
    defaults = dict()
    config_class = GlobalsConfig
