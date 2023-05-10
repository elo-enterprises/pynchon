""" pynchon.plugins.cicd
"""
import webbrowser

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

    # @cli.click.option()
    def open(self):
        """Opens CI/CD URL for this project"""
        url = self['url_build' :: self['url_base']]
        return webbrowser.open(url)

    # @cli.click.option()
    def trigger(self):
        """Triggers CI/CD job for this project"""
        url = self['url_build']
        raise NotImplementedError()
