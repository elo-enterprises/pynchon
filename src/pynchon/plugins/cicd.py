""" pynchon.plugins.cicd
"""
from pynchon import abcs, models

from pynchon.cli import click, common, options  # noqa

from pynchon.util import lme, typing  # noqa


LOGGER = lme.get_logger(__name__)


class CiCd(models.Provider):
    """
    Context for CI/CD
    """

    name = "cicd"

    class config_class(abcs.Config):
        config_key = 'cicd'
        defaults = dict(
            url_base=None,
            url_deploy=None,
            url_build=None,
        )
