""" pynchon.plugins.globals """
from pynchon import abcs, models
from pynchon.util import lme, typing # noqa

class GlobalsConfig(abcs.Config):
    """ """

    defaults = dict(exclude_patterns=[])
    config_key: typing.ClassVar[str] =  "globals"


class Globals(models.Provider):
    """Context for pynchon globals"""

    priority = 2
    name = "globals"
    config_class = GlobalsConfig
