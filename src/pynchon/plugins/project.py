""" pynchon.plugins.project
"""
import os

from pynchon import abcs, config
from pynchon.util import lme, typing
from pynchon.abcs.plugin import Plugin

LOGGER = lme.get_logger(__name__)


class Project(Plugin):
    name = 'project'
    defaults = dict()

    class config(abcs.Config):
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
            return config.git.get("repo_name", os.path.split(os.getcwd())[-1])

        @property
        def root(self) -> str:
            """ """
            return os.environ.get("PYNCHON_ROOT", config.initialized["git"].get("root"))

        @property
        def subproject(self) -> typing.Dict:
            """ """
            if os.environ.get("PYNCHON_ROOT"):
                return {}
            git = config.initialized["git"]
            workdir = abcs.Path('.')
            # workdir = pynchon["working_dir"]
            r1 = workdir.absolute()
            r2 = git["root"].absolute()
            if r1 != r2:
                self.logger.warning("subproject detected ({tmp}!=git[root])")
                return dict(name=workdir.name, root=workdir.absolute())
            return {}
