""" pynchon.plugins.python.api
"""
from pynchon import abcs, cli, models
from pynchon.util import typing, tagging, lme

LOGGER = lme.get_logger(__name__)

class PythonApiConfig(abcs.Config):
    config_key = "python-cli"
    defaults = dict(
        skip_private_methods=True,
        skip_patterns=[],
    )
@tagging.tags(click_aliases=['pa'])
class PythonAPI(models.ShyPlanner):
    """Tools for generating python-api docs"""
    name = "python-api"
    config_class = PythonApiConfig

    @cli.click.group
    def gen(self):
        """Generates API docs from python modules, packages, etc"""

    class config_class(abcs.Config):
        config_key = 'python-api'
        defaults = dict()

    @cli.options.file
    @cli.options.header
    # @options.output
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
    def toc(self,
    package=None,
    should_print=None,
    file=None,
    exclude=None,
    output=None,
    stdout=None,
    header=None):
        """
        Generate table-of-contents
        """
        from pynchon.util import complexity
        from pynchon.api import render
        T_TOC_API = render.get_template(
            "pynchon/plugins/python/api/TOC.md.j2")
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
        print(result, file=open(output, 'w'))
        if should_print and output != '/dev/stdout':
            print(result)


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
