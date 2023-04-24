""" pynchon.config
"""
import platform

from pynchon import abcs
from pynchon.util import lme, typing, python

LOGGER = lme.get_logger(__name__)
from memoized_property import memoized_property

from pynchon.util.os import invoke


class PythonCliConfig(abcs.Config):
    config_key = "python_cli"
    @property
    def entrypoints(self) -> dict:
        """ """
        import os
        import glob

        from pynchon import config

        project, pynchon = config.project, config.pynchon
        src_root = project.get("src_root", pynchon.get("src_root"))
        if not src_root:
            msg = "`src_root` not set for pynchon or project config; cannot enumerate entrypoints"
            LOGGER.warning(msg)
            return []
        pat = os.path.sep.join([src_root, "**", "__main__.py"])
        matches = [[os.path.relpath(x), {}] for x in glob.glob(pat, recursive=True)]
        matches = dict(matches)
        pkg_name = config.python.package.get("name", "unknown")
        for f, meta in matches.items():
            tmp = f[len(src_root) : -len("__main__.py")]
            tmp = tmp[1:] if tmp.startswith("/") else tmp
            tmp = tmp[:-1] if tmp.endswith("/") else tmp
            matches[f] = {**matches[f], **dict(dotpath=".".join(tmp.split("/")))}
        return matches


class PythonConfig(abcs.Config):
    """ """

    config_key = "python"
    defaults = dict(
        version=platform.python_version(),
    )

    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)

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
