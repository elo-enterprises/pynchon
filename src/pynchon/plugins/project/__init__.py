""" pynchon.plugins.project
"""
import os

from pynchon import abcs, config
from pynchon.bin import groups, options, common
from pynchon.util import lme, typing
from pynchon.bin.entry import entry
from pynchon.models import Plugin

LOGGER = lme.get_logger(__name__)


class ProjectConfig(abcs.Config):
    """ """

    priority = 1
    config_key = "project"
    # @property
    # def src_root(self) -> str:
    #     """ """
    #     return self.subproject and pynchon["working_dir"]

    @property
    def name(self) -> str:
        """ """
        repo_name = config.git.get("repo_name")
        return repo_name or os.path.split(os.getcwd())[-1]

    @property
    def root(self) -> str:
        """ """
        git = config.initialized["git"]
        return (
            os.environ.get("PYNCHON_ROOT") or (git and git.get("root")) or os.getcwd()
        )

    @property
    def subproject(self) -> typing.Dict:
        """ """
        if os.environ.get("PYNCHON_ROOT"):
            return {}
        git = config.initialized["git"]
        git_root = git["root"]
        workdir = abcs.Path('.')
        # workdir = pynchon["working_dir"]
        r1 = workdir.absolute()
        r2 = git_root and git_root.absolute()
        if r2 and (r1 != r2):
            self.logger.warning("subproject detected ({tmp}!=git[root])")
            return dict(name=workdir.name, root=workdir.absolute())
        return {}


class Project(Plugin):
    name = 'project'
    priority = 2
    defaults = dict()
    config_kls = ProjectConfig

    @staticmethod
    def init_cli(kls):
        """pynchon.bin.project"""
        import json

        from pynchon import abcs, constants, util
        from pynchon.api import project
        from pynchon.util import lme, text
        from pynchon.util.os import invoke

        LOGGER = lme.get_logger(__name__)

        @common.groop(f"{kls.name}", parent=entry)
        def project_group():
            """
            Project Automation
            """

        @common.kommand(
            name="entrypoints",
            parent=project_group,
            formatters=dict(markdown=constants.T_TOC_CLI),
            options=[
                options.file_setupcfg,
                options.format,
                options.stdout,
                options.output,
                options.header,
            ],
        )
        def project_entrypoints(format, file, stdout, output, header) -> None:
            """
            Describe entrypoints for this project (parses setup.cfg)
            """
            config, plan = project.plan()
            return {
                **util.python.load_entrypoints(util.python.load_setupcfg(file=file)),
                **dict(__main__=config.get("source", {}).get("__main__", [])),
            }

        @common.kommand(
            name="version",
            parent=project_group,
            formatters=dict(markdown=constants.T_VERSION_METADATA),
            options=[
                # FIXME: options.output_with_default('docs/VERSION.md'),
                options.format_markdown,
                options.output,
                options.header,
            ],
        )
        def project_version(format, output, header) -> None:
            """
            Describes version details for this package (and pynchon itself).
            """
            # from pynchon.api import python #, git
            import pynchon
            from pynchon.config import git, python

            return dict(
                pynchon_version=pynchon.__version__,
                package_version=python.package.version,
                git_hash=git.hash,
            )

        @project_group.command(
            name="config",
            # parent=project_group,
            # options=[],
        )
        def project_config(config=None) -> None:
            """
            Describe the config for this project
            """
            tmp = project.get_config()
            print(text.to_json(tmp))

        @common.kommand(
            name="apply",
            parent=project_group,
            options=[],
        )
        def project_apply() -> None:
            """
            Apply the plan created by `pynchon project plan`
            """
            config, plan = project.plan()
            for p in plan:
                invoke(p)
            return plan

        @common.kommand(
            name="plan",
            parent=project_group,
            options=[
                options.stdout,
            ],
        )
        def project_plan(stdout):
            """
            List goals for auto-documenting this project
            """
            config, plan = project.plan()
            config["plan"] = plan
            return json.dumps(config, indent=2, cls=abcs.JSONEncoder)