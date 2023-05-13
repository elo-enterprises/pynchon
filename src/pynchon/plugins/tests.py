""" pynchon.plugins.tests
"""
from pynchon import abcs, cli, events, models  # noqa
from pynchon.util import lme, tagging, typing  # noqa

LOGGER = lme.get_logger(__name__)


class Tests(models.Planner):
    """Management tool for project tests"""

    class config_class(abcs.Config):
        config_key = "tests"

    name = "tests"
    cli_name = "tests"
