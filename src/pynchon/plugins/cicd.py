""" pynchon.plugins.cicd
"""
import webbrowser

from pynchon import abcs, models

from pynchon.cli import click, common, options  # noqa
from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)


class CiCd(models.Provider):
    """Context for CI/CD"""

    class config_class(abcs.Config):
        config_key = "cicd"
        defaults = dict(
            url_base=None,
            url_deploy=None,
            url_build=None,
        )

        @property
        def type(self):
            """"""
            from pynchon.config import src

            src_root = abcs.Path(src["root"])
            default = "unknown"
            file_mapper = dict(
                jenkins="Jenkinsfile*",
                github_actions=".github/workflows/",
                travis=".travis.yml",
            )
            for typ, pat in file_mapper.items():
                if list(src_root.glob(pat)):
                    return typ
            return default

    name = "cicd"

    def open(self):
        """Opens CI/CD URL for this project"""
        url = self["url_build" :: self["url_base"]]
        if not url:
            LOGGER.critical("could not determine cicd url for this project config")
            return False
        else:
            return webbrowser.open(url)

    # @cli.click.option()
    def trigger(self):
        """Triggers CI/CD job for this project"""
        url = self["url_build"]
        raise NotImplementedError()
