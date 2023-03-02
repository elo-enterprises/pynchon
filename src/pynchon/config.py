""" pynchon.api.config
"""
import os
import platform
import glob

import pynchon as base
from pynchon import util
from pynchon import __version__
from pynchon.abcs import Config, Path, JSONEncoder
from pynchon.util import python as util_python

LOGGER = base.get_logger(__name__)


class GitConfig(Config):
    """ """

    @property
    def root(self):
        return util.get_root(os.getcwd())

    @property
    def repo(self):
        path = self.root
        cmd = util.invoke(f"cd {path} && git config --get remote.origin.url")
        return cmd.stdout.strip() if cmd.succeeded else ""

    @property
    def repo_name(self):
        return self.repo.split("/")[-1].split(".")[0]

    @property
    def hash(self) -> str:
        path = self.root
        cmd = util.invoke(f"cd {path} && git rev-parse HEAD")
        return cmd.succeeded and cmd.stdout.strip()


class PythonConfig(Config):
    """
    """
    def __init__(self, **kwargs):
        super(PythonConfig, self).__init__(**kwargs)

    @property
    def version(self) -> str:
        """ """
        return platform.python_version()

    @property
    def package(self) -> dict:
        if util_python.is_package():
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
        pkg_name = self.package.get('name','unknown')
        for f,meta in matches.items():
            tmp = f[len(src_root):-len("__main__.py")]
            tmp = tmp[1:] if tmp.startswith('/') else tmp
            tmp = tmp[:-1] if tmp.endswith('/') else tmp
            matches[f] = {
                **matches[f],
                **dict(
                    dotpath=".".join(tmp.split('/')))
            }
        return matches


class PynchonConfig(Config):
    """ """
    def __init__(self, **kwargs):
        super(PynchonConfig, self).__init__(**kwargs)
        file, config = util_python.load_pyprojecttoml(path=git['root'])
        config = config.get("tool", {}).get("pynchon", {})
        if config:
            for k, v in config.items():
                self[k] = v
        else:
            LOGGER.warning("could not load pyproject.toml")
        self['config_file'] = file
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
        if git['root'].joinpath('docs'):
            return git['root'].joinpath('docs')
        # git_root.joinpath('docs')
        # if 'docs_root' in self: # set in pyproject.toml
        #     return Path(self["docs_root"]).relative_to(pynchon['config_file'])
        # else:
        #     tmp = Path(self.working_dir.joinpath("docs"))
        #     if tmp.exists():
        #         return Path(tmp)

    @property
    def jinja_includes(self) -> list:
        if self.get('docs_root'):
            return [Path(self['docs_root'].joinpath("templates"))]
        else:
            LOGGER.warning("`docs_root` is not set; cannot guess `jinja_includes`")
            return []

    @property
    def working_dir(self):
        return Path(".").absolute()

    @property
    def version(self) -> str:
        return __version__


class PackageConfig(Config):
    @property
    def name(self) -> str:
        return util_python.load_setupcfg().get("metadata", {}).get("name")

    @property
    def version(self) -> str:
        """ """
        LOGGER.debug("resolving project version..")
        cmd = util.invoke("python setup.py --version")
        return cmd.succeeded and cmd.stdout.strip()


class ProjectConfig(Config):
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
            return dict(
                name=os.path.split(pynchon['working_dir'])[-1],
                root=".")
        return {}

git = GitConfig()
pynchon = PynchonConfig()
project = ProjectConfig()
python = PythonConfig()
