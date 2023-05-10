""" pynchon.plugins.git
"""
from memoized_property import memoized_property

from pynchon import models, abcs
from pynchon.util import lme, typing, files, os, tagging

LOGGER = lme.get_logger(__name__)


class GitConfig(abcs.Config):
    """ """

    config_key = "git"

    def _run(self, cmd, log_command=False, **kwargs):
        """ """
        return os.invoke(f"cd {self.root} && {cmd}", log_command=log_command, **kwargs)

    @memoized_property
    def default_remote_branch(self) -> typing.StringMaybe:
        """ """
        tmp = self._run("git remote show origin " "| sed -n '/HEAD branch/s/.*: //p'")
        if tmp.succeeded:
            return tmp.stdout.strip()

    @property
    def root(self) -> typing.StringMaybe:
        """ """
        tmp = files.get_git_root(abcs.Path("."))
        return tmp and tmp.parents[0]

    @memoized_property
    def repo(self) -> typing.StringMaybe:
        """ """
        cmd = os.invoke(
            f"cd {self.root} && git config --get remote.origin.url", log_command=False
        )
        return cmd.stdout.strip() if cmd.succeeded else None

    @property
    def is_github(self):
        """ """
        tmp = "git@github https://github.com http://github.com".split()
        return self.repo and any([self.repo.startswith(x) for x in tmp])

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
    def branch_name(self):
        """ """
        cmd = self._run("git rev-parse --abbrev-ref HEAD")
        return cmd.succeeded and cmd.stdout.strip()

    @property
    def hash(self) -> str:
        """ """
        cmd = self._run("git rev-parse HEAD")
        return cmd.succeeded and cmd.stdout.strip()


class Git(models.Provider):
    """Context for git"""

    priority = -2
    name = 'git'
    defaults: typing.Dict = dict()
    config_class = GitConfig

    @property
    def modified(self) -> typing.List[abcs.Path]:
        """ """
        return self.status().get('modified', [])

    @tagging.tags(click_aliases=['st', 'stat'])
    def status(self) -> typing.Dict:
        """JSON version of `git status` for this project"""
        cmd = self.config._run('git status --short')
        lines = [line.lstrip().strip() for line in cmd.stdout.split('\n')]
        lines = [filter(None, line.split(' ')) for line in lines if line]
        abspaths = [
            (code, abcs.Path(self.config.root) / abcs.Path(fname))
            for code, fname in lines
        ]
        modified = [p for (code, p) in abspaths if code.strip() == 'M']
        return dict(modified=modified)
