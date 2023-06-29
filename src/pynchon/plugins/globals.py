""" pynchon.plugins.globals """
from pynchon import abcs, models

from pynchon.util import lme, typing  # noqa


class GlobalsConfig(abcs.Config):
    """ """

    config_key: typing.ClassVar[str] = "globals"
    exclude_patterns: typing.List[str] = typing.Field(default=[])


class Globals(models.Provider):
    """Context for pynchon globals"""

    priority = 2
    name = "globals"
    config_class = GlobalsConfig
