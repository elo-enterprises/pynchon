""" pynchon.api.config
"""
import glob
import os
import platform
import typing

from memoized_property import memoized_property

from pynchon import __version__, abcs, util
from pynchon.util import lme
from pynchon.util import python as util_python

LOGGER = lme.get_logger(__name__)


class JinjaConfig(abcs.Config):
    """ """

    @property
    def _base(self) -> abcs.AttrDict:
        return abcs.AttrDict(**pynchon.get("jinja", {}))

    @property
    def includes(self) -> typing.List:
        docs_root = pynchon.get("docs_root", None)
        docs_root = docs_root and abcs.Path(docs_root)
        if docs_root:
            extra = [abcs.Path(docs_root.joinpath("templates"))]
        else:
            LOGGER.warning("`docs_root` is not set; cannot guess `jinja.includes`")
            extra = []
        return extra + self._base.get("includes", [])


class PyPiConfig(abcs.Config):
    @property
    def name(self):
        return "Public PyPI"

    @property
    def docs_url(self):
        return "https://pypi.org/"

    @property
    def base_url(self):
        return "https://pypi.org/project"


class GitConfig(abcs.Config):
    """ """

    @memoized_property
    def default_remote_branch(self):
        """ """
        return util.invoke(
            "git remote show origin " "| sed -n '/HEAD branch/s/.*: //p'"
        ).stdout.strip()

    @property
    def root(self):
        """ """
        return util.get_root(os.getcwd())

    @memoized_property
    def repo(self):
        """ """
        path = self.root
        cmd = util.invoke(
            f"cd {path} && git config --get remote.origin.url", log_command=False
        )
        return cmd.stdout.strip() if cmd.succeeded else ""

    @property
    def repo_url(self):
        """ """
        tmp = self.repo  # i.e. git@github.com:org/repo-name.git
        if not tmp.startswith("git@github"):
            self._logger.warning(f"don't know how to tokenize {tmp}")
        else:
            tmp = tmp.split(":")[-1]
            org, repo_name = tmp.split("/")
            repo_name = tmp.split(".git")[0]
            return f"https://github.com/{org}/{repo_name}"

    @property
    def repo_name(self):
        """ """
        return self.repo.split("/")[-1].split(".")[0]

    @property
    def hash(self) -> str:
        """ """
        path = self.root
        cmd = util.invoke(f"cd {path} && git rev-parse HEAD", log_command=False)
        return cmd.succeeded and cmd.stdout.strip()


class PythonConfig(abcs.Config):
    """ """

    def __init__(self, **kwargs):
        super(PythonConfig, self).__init__(**kwargs)

    @property
    def version(self) -> str:
        """ """
        return platform.python_version()

    @memoized_property
    def is_package(self):
        LOGGER.debug("checking if this a python package..")
        cmd = util.invoke("python setup.py --version 2>/dev/null", log_command=False)
        return cmd.succeeded

    @property
    def package(self) -> dict:
        """ """
        if self.is_package:
            return PackageConfig()
        else:
            return {}

    @property
    def entrypoints(self) -> dict:
        """ """
        src_root = project.get("src_root", pynchon.get("src_root"))
        if not src_root:
            msg = "`src_root` not set for pynchon or project config; cannot enumerate entrypoints"
            LOGGER.warning(msg)
            return []
        pat = os.path.join(src_root, "**", "__main__.py")
        matches = [[os.path.relpath(x), {}] for x in glob.glob(pat, recursive=True)]
        matches = dict(matches)
        pkg_name = self.package.get("name", "unknown")
        for f, meta in matches.items():
            tmp = f[len(src_root) : -len("__main__.py")]
            tmp = tmp[1:] if tmp.startswith("/") else tmp
            tmp = tmp[:-1] if tmp.endswith("/") else tmp
            matches[f] = {**matches[f], **dict(dotpath=".".join(tmp.split("/")))}
        return matches


class PynchonConfig(abcs.Config):
    """ """

    def __init__(self, **kwargs):
        """ " """
        super(PynchonConfig, self).__init__(**kwargs)
        file, config = util_python.load_pyprojecttoml(path=git["root"])
        config = config.get("tool", {}).get("pynchon", {})
        if config:
            for k, v in config.items():
                self[k] = v
        else:
            LOGGER.warning("could not load pyproject.toml")
        self["config_file"] = file
        # for k, v in os.environ.items():
        #     if k.startswith("PYNCHON_"):
        #         var = k[len("PYNCHON_"):].lower()
        #         val = os.environ[k]
        #         if "," in val:
        #             val = val.split(",")
        #         LOGGER.debug(f"found {k}; assigning pynchon[{var}] = {val}")
        #         self[var] = val

    # @property
    # def src_root(self):
    #     return self.get(
    #         "src_root",
    #         git['root'])
    #
    @property
    def docs_root(self):
        """ """
        if git["root"].joinpath("docs"):
            return git["root"].joinpath("docs")
        # git_root.joinpath('docs')
        # if 'docs_root' in self: # set in pyproject.toml
        #     return abcs.Path(self["docs_root"]).relative_to(pynchon['config_file'])
        # else:
        #     tmp = abcs.Path(self.working_dir.joinpath("docs"))
        #     if tmp.exists():
        #         return abcs.Path(tmp)

    @property
    def working_dir(self):
        """ """
        return abcs.Path(".").absolute()

    @property
    def version(self) -> str:
        """ """
        return __version__


class PackageConfig(abcs.Config):
    @property
    def name(self) -> str:
        """ """
        return util_python.load_setupcfg().get("metadata", {}).get("name")

    @memoized_property
    def version(self) -> str:
        """ """
        LOGGER.debug("resolving project version..")
        cmd = util.invoke("python setup.py --version 2>/dev/null", log_command=False)
        return cmd.succeeded and cmd.stdout.strip()


class ProjectConfig(abcs.Config):
    """ """

    # @property
    # def src_root(self) -> str:
    #     """ """
    #     return self.subproject and pynchon["working_dir"]

    @property
    def name(self) -> str:
        """ """
        return git.get("repo_name", os.path.split(os.getcwd())[-1])

    @property
    def root(self) -> str:
        """ """
        return git.get("root")

    @property
    def subproject(self) -> dict:
        """ """
        r1 = os.path.abspath(pynchon["working_dir"])
        r2 = os.path.abspath(git["root"])
        if r1 != r2:
            LOGGER.warning("subproject detected (pynchon[working_dir]!=git[root])")
            return dict(name=os.path.split(pynchon["working_dir"])[-1], root=".")
        return {}


git = GitConfig(
    # **pynchon.get("git", {})
)
pynchon = PynchonConfig()
project = ProjectConfig(**pynchon.get("project", {}))
python = PythonConfig(**pynchon.get("python", {}))
jinja = JinjaConfig(**pynchon.get("jinja", {}))
pypi = PyPiConfig(**pynchon.get("pypi", {}))
