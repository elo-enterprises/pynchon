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

from pynchon.config import initialized
from pynchon.abcs.plugin import Plugin

class Python(Plugin):
    """
    """
    priority=2
    name='python'
    defaults = dict()
    class config(abcs.Config):
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
    parent = Python.config
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


class PythonCLI(Plugin):
    """ """

    name = "python-cli"
    defaults = dict()
    class config(abcs.Config):
        @property
        def entrypoints(self) -> dict:
            """ """
            from pynchon import config
            project, pynchon = config.project, config.pynchon
            src_root = project.get("src_root", pynchon.get("src_root"))
            if not src_root:
                msg = "`src_root` not set for pynchon or project config; cannot enumerate entrypoints"
                LOGGER.warning(msg)
                return []
            pat = os.path.join(src_root, "**", "__main__.py")
            matches = [[os.path.relpath(x), {}] for x in glob.glob(pat, recursive=True)]
            matches = dict(matches)
            pkg_name = config.python.package.get("name", "unknown")
            for f, meta in matches.items():
                tmp = f[len(src_root) : -len("__main__.py")]
                tmp = tmp[1:] if tmp.startswith("/") else tmp
                tmp = tmp[:-1] if tmp.endswith("/") else tmp
                matches[f] = {**matches[f], **dict(dotpath=".".join(tmp.split("/")))}
            return matches

    def plan(self, config):
        plan = super(self.__class__, self).plan(config)
        droot = config.pynchon['docs_root']
        cli_root = f"{droot}/cli"
        plan += [f"mkdir -p {cli_root}"]
        plan += [f"pynchon gen cli toc --output {cli_root}/README.md"]
        plan += [f"pynchon gen cli all --output-dir {cli_root}"]
        plan += [
            f"pynchon gen cli main --file {fname} --output-dir {cli_root}"
            for fname in config.python_cli.entrypoints
        ]
        return plan


class PythonAPI(Plugin):
    """ """

    name = "python-api"
    config = dict
    defaults = dict()

    def plan(self, config) -> typing.List:
        plan = super(self.__class__, self).plan(config)
        # self.logger.debug("planning for API docs..")
        api_root = f"{config.pynchon['docs_root']}/api"
        plan += [f"mkdir -p {api_root}"]
        import IPython; IPython.embed()
        tmp = config.python["package"]["name"]
        plan += [
            "pynchon gen api toc"
            f' --package {tmp}'
            f" --output {api_root}/README.md"
        ]
        return plan


class PyPI(Plugin):
    """ """

    name = "pypi"
    config = PyPiConfig
    defaults = dict()
