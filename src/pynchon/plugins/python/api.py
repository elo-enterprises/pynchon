""" pynchon.plugins.python.api
"""
from pynchon import abcs, cli, models
from pynchon.api import render
from pynchon.util import complexity, lme, tagging, typing

LOGGER = lme.get_logger(__name__)


@tagging.tags(click_aliases=["pa"])
class PythonAPI(models.ShyPlanner):
    """Generators for Python API docs"""

    class config_class(abcs.Config):
        config_key = "python-api"
        defaults = dict(
            skip_private_methods=True,
            skip_patterns=[],
        )

    name = "python-api"

    @cli.click.group("gen")
    def gen(self):
        """Generates API docs from python modules, packages, etc"""

    # FIXME: not bound correctly: missing 1 req pos arg 'self'
    @gen.command("toc")
    @cli.options.file
    @cli.options.header
    @cli.options.should_print
    @cli.options.package
    @cli.click.option(
        "--output",
        "-o",
        default="docs/api/README.md",
        help=("output file to write.  (optional)"),
    )
    @cli.click.option(
        "--exclude",
        default="",
        help=("comma-separated list of modules to exclude (optional)"),
    )
    def toc(
        self,
        package=None,
        should_print=None,
        file=None,
        exclude=None,
        output=None,
        stdout=None,
        header=None,
    ):
        """Generate table-of-contents

        :param package: Default value = None)
        :param should_print: Default value = None)
        :param file: Default value = None)
        :param exclude: Default value = None)
        :param output: Default value = None)
        :param stdout: Default value = None)
        :param header: Default value = None)

        """

        T_TOC_API = render.get_template("pynchon/plugins/python/api/TOC.md.j2")
        module = complexity.get_module(package=package, file=file)
        result = complexity.visit_module(
            module=module,
            module_name=package,
            template=T_TOC_API,
            exclude=exclude.split(","),
        )
        header = f"{header}\n\n" if header else ""
        result = dict(
            header=f"## API for '{package}' package\n\n{header}" + "-" * 80,
            blocks=result,
        )
        result = result["header"] + "\n".join(result["blocks"])
        print(result, file=open(output, "w"))
        if should_print and output != "/dev/stdout":
            print(result)

    def plan(self, config=None) -> typing.List:
        """

        :param config: Default value = None)

        """
        config = config or self.project_config
        plan = super(self.__class__, self).plan(config)
        docs_root = self[:"docs.root":]
        api_docs_root = f"{docs_root}/api"
        if not abcs.Path(api_docs_root).exists():
            plan.append(
                models.Goal(
                    command=f"mkdir -p {api_docs_root}", resource=None, type="gen"
                )
            )
        pkg = self[:"python.package.name":None]
        pkg_arg = pkg and f"--package {pkg}"
        src_root = self[:"src.root":]
        src_arg = src_root and f"--file {src_root}"
        input = f"{pkg_arg or src_arg}"
        outputf = f"{api_docs_root}/README.md"
        output = f"--output {outputf}"
        cmd_t = "pynchon python-api gen toc"
        plan.append(
            models.Goal(
                resource=outputf,
                command=f"{cmd_t} {input} {output}",
                type="gen",
            )
        )
        return plan
