""" pynchon.plugins.python.api
"""
from pynchon import abcs, models
from pynchon.util import typing, lme

LOGGER = lme.get_logger(__name__)


class PythonAPI(models.ShyPlanner):
    """Tools for generating python-api docs"""

    # @common.groop("api", parent=groups.gen)
    # def gen_api() -> None:
    #     """
    #     Generate API docs from python modules, packages, etc
    #     """

    name = "python-api"

    class config_class(abcs.Config):
        config_key = 'python-api'
        defaults = dict()

    @classmethod
    def init_cli(kls):
        """pynchon.bin.api"""
        # import click
        #
        # from pynchon import util
        # from pynchon.plugins.Core import Core
        #
        # LOGGER = lme.get_logger(__name__)

        def markdown(**result):
            return result["header"] + "\n".join(result["blocks"])

        # @common.kommand(
        #     name="toc",
        #     parent=Core.gen_api,
        #     formatters=dict(markdown=markdown),
        #     options=[
        #         options.format_markdown,
        #         options.package,
        #         click.option(
        #             "--output",
        #             "-o",
        #             default="docs/api/README.md",
        #             help=("output file to write.  (optional)"),
        #         ),
        #         click.option(
        #             "--exclude",
        #             default="",
        #             help=("comma-separated list of modules to exclude (optional)"),
        #         ),
        #         options.file,
        #         options.stdout,
        #         options.header,
        #     ],
        # )
        # def toc(package, file, exclude, output, format, stdout, header):
        #     """
        #     Generate table-of-contents
        #     """
        #     module = util.get_module(package=package, file=file)
        #     result = util.visit_module(
        #         module=module,
        #         module_name=package,
        #         exclude=exclude.split(","),
        #     )
        #     header = f"{header}\n\n" if header else ""
        #     return dict(
        #         header=f"## API for '{package}' package\n\n{header}" + "-" * 80,
        #         blocks=result,
        #     )

    def plan(self, config=None) -> typing.List:
        """ """
        config = config or self.project_config
        plan = super(self.__class__, self).plan(config)
        api_root = f"{config.pynchon['docs_root']}/api"
        plan.append(
            models.Goal(command=f"mkdir -p {api_root}", resource=None, type='gen')
        )

        tmp = config.python["package"]["name"]
        plan.append(
            models.Goal(
                command="pynchon gen api toc"
                + f' --package {tmp}'
                + f" --output {api_root}/README.md",
                resource=None,
                type='gen',
            )
        )
        return plan
