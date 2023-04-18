""" pynchon.config.project
"""
import os

from pynchon import abcs
from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)

from . import initialized


class ProjectConfig(abcs.Config):
    """ """

    config_key = "project"
    # @property
    # def src_root(self) -> str:
    #     """ """
    #     return self.subproject and pynchon["working_dir"]

    @property
    def name(self) -> str:
        """ """
        return initialized["git"].get("repo_name", os.path.split(os.getcwd())[-1])

    @property
    def root(self) -> str:
        """ """
        return os.environ.get(
            'PYNCHON_ROOT',
            initialized["git"].get("root"))

    @property
    def subproject(self) -> typing.Dict:
        """ """
        if os.environ.get('PYNCHON_ROOT'):
            return {}
        git, pynchon = initialized["git"], initialized["pynchon"]
        workdir = pynchon["working_dir"]
        r1 = workdir.absolute()
        r2 = git["root"].absolute()
        if r1 != r2:
            self.logger.warning("subproject detected (pynchon[working_dir]!=git[root])")
            return dict(
                name=workdir.name,
                root=workdir.absolute())
        return {}
