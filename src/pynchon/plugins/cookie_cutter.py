""" pynchon.plugins.cookie_cutter
"""
from pynchon import abcs, cli, events, models  # noqa
from pynchon.util import lme, typing, tagging  # noqa

LOGGER = lme.get_logger(__name__)


class CookierCutter(models.ToolPlugin):
    """ Tools for working with cookie-cutter """

    name = "cookie-cutter"
    cli_name = 'cut'

    class config_class(abcs.Config):
        config_key = 'cookie-cutter'
