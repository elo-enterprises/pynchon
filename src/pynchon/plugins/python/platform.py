""" pynchon.plugins.python.platform
"""
import platform as stdlib_platform

from memoized_property import memoized_property

from pynchon import abcs, cli, models
from pynchon.util import lme, python, tagging, typing
from pynchon.util.os import invoke

LOGGER = lme.get_logger(__name__)


@tagging.tags(click_aliases=["py"])
class PythonPlatform(models.Planner):
    """Context for python-platform"""

    class config_class(abcs.Config):
        config_key = "python"
        defaults = dict(
            version=stdlib_platform.python_version(),
            libcst={},
        )

        @memoized_property
        def is_package(self) -> bool:
            return python.is_package(".")

        @property
        def package(self) -> typing.Dict:
            """ """
            if self.is_package:
                return PackageConfig()
            else:
                return {}

    priority = 2
    name = "python"

    @cli.click.group
    def bootstrap(self):
        """helpers for bootstrapping python projects"""

    @bootstrap.command("libcst")
    def bootstrap_libcst(self):
        """bootstrap .libcst.codemod.yaml"""
        # @cli.click.option('--libcst',help='bootstrap .libcst.codemod.yaml', default=False, is_flag=True)

    # @bootstrap.command("new")
    # @cli.click.argument("name")
    # def bootstrap_new(self):
    #     """shortcut for `pynchon cut new py/NAME`"""

    # def plan(self):
    #     plan = super(self.__class__, self).plan()
    #     libcst_config = self["libcst"]
    #     if libcst_config:
    #         plan.append(self._goal_libcst_refresh(libcst_config))
    #     return plan

    # @cli.click.group("src")
    # def src(self):
    #     """Generates code for python modules, packages, etc"""

    # @src.command
    @tagging.tags(click_parent_plugin="src")
    def sorted(self):
        """Sorts code-ordering with `ssort`"""
        plan = super(self.__class__, self).plan()
        src_root = self[:"src.root":]
        plan.append(
            self.goal(
                type="code-gen",
                resource=src_root,
                command=f"pip install ssort==0.11.6 && ssort {src_root}",
            )
        )
        return self.apply(plan)


class PackageConfig(abcs.Config):
    """WARNING: `parent` below prevents moving this class elsewhere"""

    parent = PythonPlatform.config_class
    config_key = "package"

    @property
    def name(self) -> str:
        """ """
        from pynchon.util import python

        result = python.load_setupcfg().get("metadata", {}).get("name")
        return result

    @memoized_property
    def version(self) -> str:
        """ """
        cmd = invoke("python setup.py --version 2>/dev/null", log_command=False)
        return cmd.succeeded and cmd.stdout.strip()
