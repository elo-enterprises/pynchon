""" pynchon.plugins.python.platform
"""
import platform as stdlib_platform

from memoized_property import memoized_property

from pynchon import abcs, cli, models
from pynchon.util import lme, tagging, typing
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
            from pynchon.util import python

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

    @bootstrap.command("new")
    @cli.click.argument("name")
    def bootstrap_new(self):
        """shortcut for `pynchon cut new py/NAME`"""

    @cli.click.group("gen")
    def gen(self):
        """Generates code for python modules, packages, etc"""

    @cli.click.command("libcst-list")
    def _libcst_list(self):
        """libcst-codemods-list"""
        from pynchon.util.os import invoke
        out = invoke('python -mlibcst.tool list',strict=True)
        out=out.stdout
        print(f"\n{out}")

    def _goal_libcst_refresh(self, libcst_config):
        from pynchon.util import text

        min = text.to_json(libcst_config, minified=True)
        rsrc = ".libcst.codemod.yaml"
        cmd = f"printf '{min}' | python -mpynchon.util.text.dumpf yaml > {rsrc}"
        return self.goal(
            type="render",
            label="refresh libcst-config",
            resource=rsrc,
            command=cmd,
        )

    def plan(self):
        plan = super(self.__class__, self).plan()
        libcst_config = self["libcst"]
        if libcst_config:
            plan.append(self._goal_libcst_refresh(libcst_config))
        return plan

    @gen.command
    @cli.options.ignore_private
    @cli.options.ignore_missing
    @cli.click.option(
        "--modules", help="create docstrings for modules", default=False, is_flag=True
    )
    @cli.click.option(
        "--functions",
        help="create docstrings for functions",
        default=False,
        is_flag=True,
    )
    @cli.click.option(
        "--methods", help="create docstrings for methods", default=False, is_flag=True
    )
    def docstrings(
        self,
        ignore_missing: bool = False,
        ignore_private: bool = True,
        modules: bool = True,
        functions: bool = True,
        methods: bool = True,
        classes: bool = True,
    ):
        """Generates python docstrings"""
        self.logger.critical(locals())

    @cli.click.group("src")
    def src(self):
        """Generates code for python modules, packages, etc"""

    @src.command
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
