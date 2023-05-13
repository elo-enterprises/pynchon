""" pynchon.plugins.tests
"""
from pynchon import abcs, cli, events, models  # noqa
from pynchon.util import lme, tagging, typing  # noqa

LOGGER = lme.get_logger(__name__)


class Tests(models.ResourceManager):
    """Management tool for project tests"""

    class config_class(abcs.Config):
        config_key = "tests"
        defaults = dict(
            coverage={},
            suite_patterns=[],
            # suites={
            #     "{{tests.root}}/units/": {
            #           name:...
            #           descr:...
            #           runner:...
            #      }
            # }
            root=None,
        )

    name = "tests"
    cli_name = "tests"
