""" pynchon.plugins.project
"""
from pynchon import abcs, config, models, constants

from pynchon.cli import common, options  # noqa
from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)


class ProjectConfig(abcs.Config):
    """ """

    priority = 1
    config_key = "project"
    defaults = dict(shell_aliases=dict(), subproject_patterns=[])

    @property
    def name(self) -> typing.StringMaybe:
        """ """
        repo_name = config.git.get("repo_name")
        return repo_name or abcs.Path('.').name

    @property
    def _workdir(self):
        return abcs.Path('.').absolute()

    @property
    def root(self) -> str:
        """ """
        git = config.GIT
        return constants.PYNCHON_ROOT or (git and git.get("root")) or self._workdir

    @property
    def subproject(self) -> typing.Dict:
        """ """
        if constants.PYNCHON_ROOT:
            return {}
        git = config.GIT
        git_root = git["root"]
        r1 = self._workdir
        r2 = git_root and git_root.absolute()
        if r2 and (r1 != r2):
            self.logger.warning("subproject detected ({tmp}!=git[root])")
            return dict(name=self._workdir.name, root=self._workdir)
        return {}


class Project(models.Manager):
    """Meta-plugin for managing this project"""

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
