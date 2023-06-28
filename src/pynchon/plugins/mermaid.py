""" pynchon.plugins.mermaid
"""
import os

from pynchon.util.os import invoke

from pynchon import abcs, cli, events, models  # noqa
from pynchon.util import files, lme, tagging, typing  # noqa

LOGGER = lme.get_logger(__name__)
IMG = "ghcr.io/mermaid-js/mermaid-cli/mermaid-cli"


class Mermaid(models.Planner):
    """ Mermaid Plugin """

    class config_class(abcs.Config):
        config_key: typing.ClassVar[str] =  "mermaid"

    name = "mermaid"
    cli_name = "mermaid"
    
    @property 
    def working_dir(self):
        """ """
        return abcs.Path(".").absolute()

    def list(self):
        """ 
        Find mermaid diagrams under `{{project_root}}/**/*.mmd` 
        """
        includes = "**/*.mmd"
        search = [
            abcs.Path(self.project_root).joinpath(includes),
        ]
        self.logger.debug(f"search pattern is {search}")
        result = files.find_globs(search)
        return result

    @cli.options.in_place
    @cli.options.output
    @cli.click.option("--img", default="nshine/dot")
    @cli.click.option("--output-mode")
    @cli.click.argument("file", nargs=1)
    def render(
        self,
        img: str = "??",
        file: str = "",
        in_place: bool = True,
        output_mode: str = "svg",
        output: str = "",
    ):
        """ 
        Renders mermaid diagram to image
        """
        if in_place:
            assert not output
            output = os.path.splitext(file)[0] + f".{output_mode}"
        assert output
        # cmd = f"cat {file} | docker run --rm --entrypoint dot -i {img} -T{output_mode} > {output}"
        wd = self.working_dir
        file = abcs.Path(file).absolute().relative_to(wd)
        output = abcs.Path(output).absolute().relative_to(wd)
        uid = os.getuid()
        cmd = f"docker run -v {wd}:/workspace -w /workspace -u {uid} {IMG} -i {file} -o {output} --backgroundColor efefef"
        LOGGER.critical(cmd)
        result = invoke(cmd, strict=True)
        # assert result.succeeded
        # return result.succeeded
        return True

    def plan(
        self,
        config=None,
    ) -> models.Plan:
        """ Run planning for this plugin """
        plan = super(self.__class__, self).plan(config=config)
        self.logger.debug("planning for rendering for .mmd mermaid files..")
        cmd_t = (
            f"pynchon {self.cli_name} " + "render {rsrc} --in-place --output-mode png"
        )
        for rsrc in self.list():
            plan.append(
                self.goal(
                    resource=rsrc,
                    command=cmd_t.format(rsrc=rsrc),
                    type="render",
                )
            )
        return plan

    # cli_label = "Tool"
    # def run(self):


# mmdc -i input.mmd -o output.png -t dark -b transparent
# https://github.com/mermaid-js/mermaid-cli
