""" pynchon.plugins.gen
"""
from pynchon import models
from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class Generators(models.NameSpace):
    """
    Collects `gen` commands from other plugins
    """

    name = cli_name = 'gen'
    priority = -1
    config_class = None
    cli_subsumes: typing.List[typing.Callable] = []
