""" pynchon.plugins.git
"""
from memoized_property import memoized_property

from pynchon import abcs
from pynchon.bin import groups, common
from pynchon.bin.entry import entry
from pynchon.abcs import Path
from pynchon.util import lme, typing, files
from pynchon.util.os import invoke
from pynchon.abcs.plugin import Plugin

LOGGER = lme.get_logger(__name__)


class GitConfig(abcs.Config):
    """ """

    config_key = "git"

    def _run(self, cmd, log_command=False, **kwargs):
        """ """
        return invoke(f"cd {self.root} && {cmd}", log_command=log_command, **kwargs)

    @memoized_property
    def default_remote_branch(self) -> typing.StringMaybe:
        """ """
        tmp = self._run("git remote show origin " "| sed -n '/HEAD branch/s/.*: //p'")
        if tmp.succeeded:
            return tmp.stdout.strip()

    @property
    def root(self) -> typing.StringMaybe:
        """ """
        tmp = files.get_git_root(Path("."))
        return tmp and tmp.parents[0]

    @memoized_property
    def repo(self):
        """ """
        cmd = invoke(
            f"cd {self.root} && git config --get remote.origin.url", log_command=False
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
    def repo_name(self) -> typing.StringMaybe:
        """ """
        if self.repo:
            tmp = self.repo.split(":")[-1]
            _org, repo_name = tmp.split("/")
            # err=f"cannot determine repo name from {self.repo}"
            # self.logger.critical(err)
            # raise ValueError(err)
            repo_name = repo_name.split(".git")[0]
            return repo_name

    @property
    def repo_url(self):
        """ """
        if all([self.github_org, self.repo_name]):
            return f"https://github.com/{self.github_org}/{self.repo_name}"

    @property
    def hash(self) -> str:
        """ """
        cmd = self._run("git rev-parse HEAD")
        return cmd.succeeded and cmd.stdout.strip()


class Git(Plugin):
    """ """

    priority = 0
    name = 'git'
    defaults = dict()
    config_kls =GitConfig

    @classmethod
    def init_cli(kls):
        """pynchon.bin.project"""

        @common.groop(kls.name, parent=entry)
        def plugin_main():
            """subcommands for plugin"""

        @plugin_main.command('config')
        def config():
            """shows current config for this plugin"""
            LOGGER.debug(kls.config)
