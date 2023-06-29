""" pynchon.plugins.git
"""

from pynchon import abcs, models
from pynchon.util import files, lme, os, tagging, typing

LOGGER = lme.get_logger(__name__)


class GitConfig(abcs.Config):
    """ """

    # _root: str = None
    config_key: typing.ClassVar[str] = "git"

    # class Config:
    #     fields = {
    #         # '_root': 'root',
    #         '_repo': 'repo',
    #     }

    def _run(self, cmd, log_command=False, **kwargs):
        """
        :param cmd: param log_command:  (Default value = False)
        :param log_command:  (Default value = False)
        :param **kwargs:
        """
        if self.root:
            pre = f"cd {self.root} && " if self.root else ""
            return os.invoke(f"{pre}{cmd}", log_command=log_command, **kwargs)

    #
    # @memoized_property
    # def default_remote_branch(self) -> typing.StringMaybe:
    #     """ """
    #     tmp = self._run("git remote show origin " "| sed -n '/HEAD branch/s/.*: //p'")
    #     if tmp and tmp.succeeded:
    #         return tmp.stdout.strip() or None

    @property
    def root(self) -> typing.StringMaybe:
        """ """
        tmp = self.__dict__.get("_root")
        if tmp:
            return tmp
        tmp = files.get_git_root(abcs.Path("."))
        return tmp and tmp.parents[0]

    @property
    def repo(self) -> typing.StringMaybe:
        """ """
        cmd = self._run("git config --get remote.origin.url")
        return cmd and (cmd.stdout.strip() if cmd.succeeded else None)

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
        tmp = cmd and cmd.succeeded and cmd.stdout.strip()
        return tmp or None

    @property
    def hash(self) -> str:
        """ """
        cmd = self._run("git rev-parse HEAD")
        tmp = cmd and cmd.succeeded and cmd.stdout.strip()
        return tmp or None


@tagging.tags(click_aliases=["g"])
class Git(models.Provider):
    """Context for git"""

    priority = -2
    name = "git"
    config_class = GitConfig

    @property
    def modified(self) -> typing.List[abcs.Path]:
        """ """
        return self.status().get("modified", [])

    @tagging.tags(click_aliases=["st", "stat"])
    def status(self) -> typing.Dict:
        """JSON version of `git status` for this project"""
        cmd = self.config._run("git status --short")
        lines = [line.lstrip().strip() for line in cmd.stdout.split("\n")]
        lines = [filter(None, line.split(" ")) for line in lines if line]
        abspaths = [
            (code, abcs.Path(self.config.root) / abcs.Path(fname))
            for code, fname in lines
        ]
        modified = [p for (code, p) in abspaths if code.strip() == "M"]
        return dict(modified=modified)
