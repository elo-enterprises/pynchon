""" pynchon.plugins.griffe
"""
from pynchon import abcs, cli, events, models  # noqa
from pynchon.util import lme, typing, tagging  # noqa

LOGGER = lme.get_logger(__name__)


class Griffe(models.ToolPlugin):
    """
    Tools for working with Python ASTs
    """

    name = "griffe"
    cli_name = 'griffe'

    class config_class(abcs.Config):
        config_key = 'griffe'
