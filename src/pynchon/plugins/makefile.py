""" pynchon.plugins.makefile
"""

from pynchon import abcs, api, cli, events, models  # noqa
from pynchon.util import lme, tagging, typing  # noqa

LOGGER = lme.get_logger(__name__)


class Make(models.Provider):
    """Makefile parser"""

    class config_class(abcs.Config):
        config_key = "makefile"

    name = "makefile"
    cli_name = "makefile"
    cli_label = "Meta"

    @property
    def fpath(self):
        return abcs.Path(self[:"project.root"]) / "Makefile"

    @property
    def plugin_templates_root(self):
        """ """
        return abcs.Path(self.plugin_templates_prefix)

    def _get_template(self, relpath: str = ""):
        tfile = self.plugin_templates_root / relpath
        return api.render.get_template(str(tfile))

    @property
    def parsed(self) -> typing.Dict:
        """ """
        return api.parsers.makefile.parse(fpath=self.fpath)

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
    def _render_mermaid(self, title: str = "", template: str = ""):
        """Renders mermaid diagram for makefile targets"""
        tmpl = self._get_template(template)

        print(
            api.render.clean_whitespace(
                tmpl.render(
                    **dict(
                        title=title,
                        parsed=self.parse(),
                    )
                )
            )
        )

    @cli.click.flag("--graph", "only_graph", help="Return only the prerequisites-graph")
    def parse(self, only_graph: bool = False):
        """Parse Makefile to JSON.  (Includes DAGs for target)"""
        out = self.parsed
        if only_graph:
            out = {t: out[t]["prereqs"] for t in out}
        return out

    # def bootstrap(self):
    #     """ placeholder """
    #     raise NotImplementedError()
