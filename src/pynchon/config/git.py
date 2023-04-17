""" pynchon.config.git
"""
import os

from memoized_property import memoized_property

from pynchon import abcs, util
from pynchon.util import lme, typing
from pynchon.util.os import invoke

LOGGER = lme.get_logger(__name__)

# from . import initialized


class GitConfig(abcs.Config):
    """ """

    priority = 0
    config_key = "git"

    @memoized_property
    def default_remote_branch(self):
        """ """
        return invoke(
            "git remote show origin " "| sed -n '/HEAD branch/s/.*: //p'"
        ).stdout.strip()

    @property
    def root(self) -> typing.StringMaybe:
        """ """
        return util.get_root(os.getcwd())

    @memoized_property
    def repo(self):
        """ """
        path = self.root
        cmd = invoke(
            f"cd {path} && git config --get remote.origin.url", log_command=False
        )
        return cmd.stdout.strip() if cmd.succeeded else ""

    @property
    def is_github(self):
        """ """
        tmp = "git@github https://github.com http://github.com".split()
        return any([self.repo.startswith(x) for x in tmp])

    @property
    def github_org(self):
        """ """
        if self.is_github:
            tmp = self.repo.split(":")[-1]
            org, repo_name = tmp.split("/")
            return org

    @property
    def repo_name(self):
        """ """
        tmp = self.repo.split(":")[-1]
        _org, repo_name = tmp.split("/")
        repo_name = repo_name.split(".git")[0]
        return repo_name

    @property
    def repo_url(self):
        """ """
        return f"https://github.com/{self.github_org}/{self.repo_name}"

    @property
    def hash(self) -> str:
        """ """
        path = self.root
        cmd = invoke(f"cd {path} && git rev-parse HEAD", log_command=False)
        return cmd.succeeded and cmd.stdout.strip()
