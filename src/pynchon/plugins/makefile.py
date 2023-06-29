""" pynchon.plugins.makefile
"""

from pynchon import abcs, api, cli, events, models  # noqa
from pynchon.util import lme, tagging, typing  # noqa
from pynchon.util.makefile import parse as makefile_parse

LOGGER = lme.get_logger(__name__)


class Make(models.Planner):
    """Makefile parser"""

    priority = 6  # before mermaid

    class config_class(abcs.Config):
        config_key: typing.ClassVar[str] = "makefile"

        @property
        def file(self):
            # from pynchon.config import project
            tmp = abcs.Path(".").absolute()
            return tmp / "Makefile"

    name = "makefile"
    cli_name = "makefile"
    cli_label = "Meta"

    @property
    def plugin_templates_root(self):
        """ """
        return abcs.Path(self.plugin_templates_prefix)

    @property
    def output_file(self):
        default = abcs.Path(self[:"docs.root":]) / "img" / "Makefile.mmd"
        return self["output_file"::default]

    def plan(self):
        """Runs a plan for this plugin"""
        plan = super(self.__class__, self).plan()
        input_file = self["file"]
        diagram_title = (
            abcs.Path(self["diagram_title"::input_file])
            .absolute()
            .relative_to(abcs.Path(".").absolute())
        )
        output_file = self.output_file
        output_folder = output_file.parents[0]
        if not output_folder.exists():
            plan.append(
                self.goal(
                    resource=output_file, type="mkdir", command=f"mkdir {output_folder}"
                )
            )
        plan.append(
            self.goal(
                resource=output_file,
                type="render",
                command=f"pynchon makefile render mermaid --title {diagram_title} --output {output_file} {input_file} ",
            )
        )
        return plan

    def get_template_file(self, relpath: str = ""):
        tfile = self.plugin_templates_root / relpath
        return api.render.get_template(str(tfile))

    @property
    def parsed(self) -> typing.Dict:
        """ """
        return self.parse()

    @cli.click.group
    def render(self):
        """Subcommands for rendering"""

    @render.command("mermaid")
    @cli.click.option("--title", help="diagram title", default="Makefile Targets")
    @cli.click.option(
        "--template",
        help="mermaid template to use",
        default="mermaid-graph.mmd.j2",
    )
    @cli.options.output
    @cli.click.argument("makefile", default="Makefile")
    def _render_mermaid(
        self, output: str = "", makefile: str = "", title: str = "", template: str = ""
    ):
        """Renders mermaid diagram for makefile targets"""
        tmpl = self.get_template_file(template)
        LOGGER.warning("writing to file: {output}")
        if output in ["-", "/dev/stdout", ""]:
            import sys

            fhandle = sys.stdout
        else:
            fhandle = open(output, "w")
        print(
            api.render.clean_whitespace(
                tmpl.render(
                    **dict(
                        title=title,
                        parsed=self.parse(makefile=makefile),
                    )
                )
            ),
            file=fhandle,
        )

    @cli.click.flag(
        "--graph", "only_graph", help="Returns only the prerequisites-graph"
    )
    @cli.click.argument(
        "makefile",
        # help="Return only the prerequisites-graph"
        default="",
        required=False,
    )
    def parse(self, makefile: str = "", only_graph: bool = False):
        """Parse Makefile to JSON.  Includes DAGs for targets, target-body, and target-type details"""
        makefile = makefile or self.config["file"]
        out = makefile_parse(makefile=makefile)
        if only_graph:
            out = {t: out[t]["prereqs"] for t in out}
        return out

    # def bootstrap(self):
    #     """ placeholder """
    #     raise NotImplementedError()
