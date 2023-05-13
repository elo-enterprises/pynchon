"""
"""
from pynchon import abcs, models


class GlobalsConfig(abcs.Config):
    """ """

    defaults = dict(exclude_patterns=[])
    config_key = "globals"


class Globals(models.Provider):
    """Context for pynchon globals"""

    priority = 2
    name = "globals"
    config_class = GlobalsConfig
