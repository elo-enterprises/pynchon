""" pynchon.plugins.python.platform
"""
import platform as stdlib_platform

from memoized_property import memoized_property

from pynchon import abcs, models
from pynchon.util import typing, lme
from pynchon.util.os import invoke

LOGGER = lme.get_logger(__name__)


class PythonPlatform(models.Provider):
    """Context for python-platform"""

    priority = 2
    name = 'python'

    class config_class(abcs.Config):
        config_key = "python"
        defaults = dict(
            version=stdlib_platform.python_version(),
        )

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


class PackageConfig(abcs.Config):
    parent = PythonPlatform.config_class
    config_key = "package"

    @property
    def name(self) -> str:
        """ """
        from pynchon.util import python

        return python.load_setupcfg().get("metadata", {}).get("name")

    @memoized_property
    def version(self) -> str:
        """ """
        # self.logger.debug("resolving project version..")
        cmd = invoke("python setup.py --version 2>/dev/null", log_command=False)
        return cmd.succeeded and cmd.stdout.strip()
