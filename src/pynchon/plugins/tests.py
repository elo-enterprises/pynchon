""" pynchon.plugins.tests
"""
from pynchon import abcs, cli, events, models  # noqa
from pynchon.util import lme, typing, tagging  # noqa

LOGGER = lme.get_logger(__name__)


class Tests(models.Planner):
    """Management tool for project tests"""

    name = "tests"
    cli_name = 'tests'

    class config_class(abcs.Config):
        config_key = 'tests'
