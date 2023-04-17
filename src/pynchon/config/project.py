""" pynchon.config.project
"""
import os

from memoized_property import memoized_property

from pynchon import abcs, util
from pynchon.util import lme, python, text, typing
from pynchon.util.os import invoke

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
        return initialized["git"].get("root")

    @property
    def subproject(self) -> dict:
        """ """
        git, pynchon = initialized["git"], initialized["pynchon"]
        r1 = os.path.abspath(pynchon["working_dir"])
        r2 = os.path.abspath(git["root"])
        if r1 != r2:
            LOGGER.warning("subproject detected (pynchon[working_dir]!=git[root])")
            return dict(
                name=os.path.split(initialized["pynchon"]["working_dir"])[-1], root="."
            )
        return {}
