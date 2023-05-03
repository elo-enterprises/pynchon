""" pynchon.plugins.project
"""
import os

from pynchon import abcs, config, models

from pynchon.cli import common, options  # noqa
from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)


class ProjectConfig(abcs.Config):
    """ """

    priority = 1
    config_key = "project"

    @property
    def name(self) -> typing.StringMaybe:
        """ """
        repo_name = config.git.get("repo_name")
        return repo_name or os.path.split(os.getcwd())[-1]

    @property
    def root(self) -> str:
        """ """
        git = config.GIT
        return (
            os.environ.get("PYNCHON_ROOT") or (git and git.get("root")) or os.getcwd()
        )

    @property
    def subproject(self) -> typing.Dict:
        """ """
        if os.environ.get("PYNCHON_ROOT"):
            return {}
        git = config.GIT
        git_root = git["root"]
        workdir = abcs.Path('.')
        # workdir = pynchon["working_dir"]
        r1 = workdir.absolute()
        r2 = git_root and git_root.absolute()
        if r2 and (r1 != r2):
            self.logger.warning("subproject detected ({tmp}!=git[root])")
            return dict(name=workdir.name, root=workdir.absolute())
        return {}


class Project(models.Manager):
    """Macros for plan/applies across plugins"""

    name = 'project'
    priority = 2
    config_class = ProjectConfig

    # @common.kommand(
    #     name="version",
    #     parent=parent,
    #     formatters=dict(markdown=constants.T_VERSION_METADATA),
    #     options=[
    #         # FIXME: options.output_with_default('docs/VERSION.md'),
    #         options.format_markdown,
    #         options.output,
    #         options.header,
    #     ],
    # )
    # def project_version(format, output, header) -> None:
    #     """
    #     Describes version details for this package (and pynchon itself).
    #     """
    #     # from pynchon.api import python #, git
    #     import pynchon
    #     from pynchon.config import git, python
    #
    #     return dict(
    #         pynchon_version=pynchon.__version__,
    #         package_version=python.package.version,
    #         git_hash=git.hash,
    #     )
