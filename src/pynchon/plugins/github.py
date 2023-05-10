""" pynchon.plugins.github
"""
from pynchon import abcs, cli, events, models  # noqa
from pynchon.util import lme, typing, tagging  # noqa

LOGGER = lme.get_logger(__name__)


class GitHub(models.Provider):
    """GitHub"""

    name = "github"
    cli_name = 'github'
    cli_aliases = []

    class config_class(abcs.Config):
        config_key = 'github'
