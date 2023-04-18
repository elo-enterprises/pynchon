""" pynchon.config.python
"""
import os
import glob
import platform

from memoized_property import memoized_property

from pynchon import abcs
from pynchon.util import lme, python, typing
from pynchon.util.os import invoke

LOGGER = lme.get_logger(__name__)

from . import initialized


class PythonConfig(abcs.Config):
    """ """

    config_key = "python"
    defaults = dict(
        version=platform.python_version(),
    )

    def __init__(self, **kwargs):
        super(PythonConfig, self).__init__(**kwargs)

    @memoized_property
    def is_package(self) -> bool:
        # self.logger.debug("checking if this a python package..")
        cmd = invoke("python setup.py --version 2>/dev/null", log_command=False)
        return cmd.succeeded

    @property
    def package(self) -> typing.Dict:
        """ """
        if self.is_package:
            return PackageConfig()
        else:
            return {}

    @property
    def entrypoints(self) -> dict:
        """ """
        project, pynchon = initialized["project"], initialized["pynchon"]
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


class PyPiConfig(abcs.Config):
    config_key = "pypi"
    defaults = dict(
        name="Public PyPI",
        docs_url="https://pypi.org/",
        base_url="https://pypi.org/project",
    )


class PackageConfig(abcs.Config):
    parent = PythonConfig
    config_key = "package"

    @property
    def name(self) -> str:
        """ """
        return python.load_setupcfg().get("metadata", {}).get("name")

    @memoized_property
    def version(self) -> str:
        """ """
        # self.logger.debug("resolving project version..")
        cmd = invoke("python setup.py --version 2>/dev/null", log_command=False)
        return cmd.succeeded and cmd.stdout.strip()
