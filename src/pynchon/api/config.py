""" pynchon.api.config
"""
import os
import platform
import pynchon

from pynchon import util
from pynchon.abcs import Config
from pynchon.api import python

LOGGER = pynchon.get_logger(__name__)


def is_package() -> bool:
    """ """
    LOGGER.debug("checking if this a python package..")
    cmd = util.invoke("python setup.py --version")
    return cmd.succeeded


class GitConfig(Config):
    """ """

    @property
    def root(self):
        return util.get_root(PynchonConfig()["working_dir"])

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
    def __init__(self, **kwargs):
        super(PythonConfig, self).__init__(**kwargs)

    @property
    def version(self) -> str:
        """ """
        return platform.python_version()

    @property
    def package(self) -> dict:
        if is_package():
            return PackageConfig()
        else:
            return {}

    @property
    def entrypoints(self):
        """ """
        src_root = PynchonConfig()['src_root']
        pat = os.path.join(
            src_root, "**", "__main__.py"
        )
        import glob
        matches = [os.path.relpath(x) for x in glob.glob(pat, recursive=True)]
        return matches


class PynchonConfig(Config):
    """ """
    def __init__(self, **kwargs):
        super(PynchonConfig, self).__init__(**kwargs)
        for k, v in (
            python.load_pyprojecttoml().get("tool", {}).get("pynchon", {}).items()
        ):
            self[k] = v
        for k,v in os.environ.items():
            if k.startswith('PYNCHON_'):
                var = k[len('PYNCHON_'):].lower()
                val = os.environ[k]
                if ',' in val:
                    val = val.split(',')
                LOGGER.debug(f"found {k}; assigning pynchon[{var}] = {val}")
                self[var] = val

    @property
    def docs_root(self):
        return os.path.join(self.working_dir, 'docs')

    @property
    def jinja_includes(self):
        return os.path.join(self.docs_root, 'templates')

    @property
    def working_dir(self):
        return os.getcwd()

    @property
    def version(self) -> str:
        from pynchon import __version__
        return __version__


class PackageConfig(Config):
    @property
    def name(self) -> str:
        return python.load_setupcfg().get("metadata", {}).get("name")

    @property
    def version(self) -> str:
        """ """
        LOGGER.debug("resolving project version..")
        cmd = util.invoke("python setup.py --version")
        return cmd.succeeded and cmd.stdout.strip()

class ProjectConfig(Config):
    """ """

    @property
    def name(self) -> str:
        """ """
        return GitConfig().get("repo_name", os.path.split(os.getcwd())[-1])

    @property
    def root(self) -> str:
        """ """
        return GitConfig().get("root")

    @property
    def subproject(self) -> dict:
        """ """
        if os.path.abspath(PynchonConfig()["working_dir"]) != os.path.abspath(GitConfig()["root"]):
            LOGGER.debug("subproject detected")
            return dict(
                name=os.path.split(os.getcwd())[-1],
                root=os.getcwd())
