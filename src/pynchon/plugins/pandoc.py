""" pynchon.plugins.pandoc
"""

from fleks import cli

from fleks.util import tagging  # noqa

from pynchon import abcs, events, models  # noqa
from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)


class Pandoc(models.Planner):
    """Tool for working with Pandoc"""

    class config_class(abcs.Config):
        config_key: typing.ClassVar[str] = "pandoc"
        docker_image: str = typing.Field(default="pandoc/extra:latest")
        pdf_args: typing.List = typing.Field(
            default=["--toc", "--variable fontsize=10pt"]
        )
        goals: typing.List[typing.Dict] = typing.Field(default=[], help="")

    name = "pandoc"
    cli_name = "pandoc"
    cli_label = "Tool"
    # contribute_plan_apply = False

    def _get_cmd_base(self, *args):
        docker_image = self["docker_image"]
        return (
            "docker run -v `pwd`:/workspace -w /workspace "
            f"{docker_image} {' '.join(args)}"
        )

    def _get_cmd(self, *args, **kwargs):
        """ """
        cmd_t = self._get_cmd_base(" ".join(args))
        pdf_args = " ".join(self["pdf_args"])
        zip_kws = " ".join(["{k}={v}" for k, v in kwargs.items()])
        cmd_t += f" {pdf_args} {zip_kws}"
        return cmd_t

    @cli.click.command(
        context_settings=dict(
            ignore_unknown_options=True,
            allow_extra_args=True,
        )
    )
    def run(self, *args, **kwargs):
        """Passes given command through to the pandoc docker-image"""
        import sys

        command = sys.argv[sys.argv.index(self.click_group.name) + 2 :]
        command = self._get_cmd(" ".join(command))
        LOGGER.warning(command)
        plan = super().plan(goals=[self.goal(type="render", command=command)])
        result = self.apply(plan=plan)
        raise SystemExit(0 if result.ok else 1)

    @tagging.tags(click_aliases=["markdown.to-pdf"])
    @cli.options.output_file
    @cli.click.argument("file")
    def md_to_pdf(
        self,
        file: str = None,
        output: str = None,
    ):
        """
        Converts markdown files to PDF with pandoc
        """
        output = abcs.Path(output or f"{abcs.Path(file).stem}.pdf")
        # cmd = f"docker run -v `pwd`:/workspace -w /workspace {docker_image} {file} {pdf_args} -o {output}"
        return self.run(file, o=output)
        # plan = super().plan(
        #     goals=[
        #         self.goal(resource=output.absolute(),
        #         type="render", command=cmd)]
        # )
        # return self.apply(plan=plan)
