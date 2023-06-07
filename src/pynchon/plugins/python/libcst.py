""" pynchon.plugins.python.libcst
"""
from pynchon import abcs, cli, events, models  # noqa
from pynchon.util import lme, python, tagging, typing  # noqa
from pynchon.util.os import invoke

LOGGER = lme.get_logger(__name__)
F_CODEMOD_YAML = ".libcst.codemod.yaml"


class LibCST(models.Planner):
    """
    Code-transforms via libcst[1]
    """

    class config_class(abcs.Config):
        config_key = "python-libcst"

    name = "python-libcst"
    cli_name = "python-libcst"
    cli_label = "Tool"

    @cli.click.group("gen")
    def gen(self):
        """Generates code for python modules, packages, etc"""

    @tagging.tags(click_parent_plugin="src")
    @cli.click.argument("transform_name", nargs=1)
    @cli.click.argument("src_root", default="", nargs=1)
    def run_transform(self, transform_name="docstrings.simple.module", src_root=""):
        """Runs the given libcst transform on {src.root}"""
        src_root = src_root or self[:"src.root":]
        return invoke(
            f"python -m libcst.tool codemod {transform_name} {src_root}", system=True
        )

    @tagging.tags(click_parent_plugin="src")
    # @cli.click.command("list-codegen")
    def list_transforms(self):
        """Lists known libcst transforms"""
        out = invoke("python -mlibcst.tool list", strict=True)
        out = out.stdout
        print(f"\n{out}")

    def _goal_libcst_refresh(self, libcst_config):
        from pynchon.util import text

        min = text.to_json(libcst_config, minified=True)
        rsrc = F_CODEMOD_YAML
        cmd = f"printf '{min}' | python -mpynchon.util.text.dumpf yaml > {rsrc}"
        return self.goal(
            type="render",
            label="refresh libcst-config",
            resource=rsrc,
            command=cmd,
        )

    def plan(self):
        plan = super(self.__class__, self).plan()
        libcst_config = self[F_CODEMOD_YAML]
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
