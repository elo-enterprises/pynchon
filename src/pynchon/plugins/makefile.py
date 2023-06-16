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

    # @memoized_property
    # def database(self) -> typing.List:
    #     return api.parsers.makefile.database()

    @property
    def parsed(self) -> typing.Dict:
        return api.parsers.makefile.parse(
            # database=self.database,
            fpath=self.fpath
        )

    @cli.click.group
    def render(self):
        """generate"""

    @render.command("mermaid")
    def _diagram(self):
        """ """
        tmpl = api.render.get_template(
            self.plugin_templates_root / "mermaid-graph.mmd.j2"
        )
        print(tmpl.render(**dict(title="bar")))

    @cli.click.flag("--graph", "only_graph", help="Return only the prerequisites-graph")
    def parse(self, only_graph: bool = False):
        """placeholder"""
        out = self.parsed
        if only_graph:
            out = {t: out[t]["prereqs"] for t in out}
        return out

    def bootstrap(self):
        """placeholder"""
        raise NotImplementedError()
