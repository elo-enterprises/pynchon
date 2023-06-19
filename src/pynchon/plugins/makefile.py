""" pynchon.plugins.makefile
"""

from pynchon import abcs, api, cli, events, models  # noqa
from pynchon.util import lme, tagging, typing  # noqa
from pynchon.util.makefile import parse as makefile_parse

LOGGER = lme.get_logger(__name__)


class Make(models.Provider):
    """Makefile parser"""

    class config_class(abcs.Config):
        config_key = "makefile"
        
        @property 
        def file(self):
            # from pynchon.config import project 
            tmp = abcs.Path('.').absolute()
            return tmp/"Makefile"
    
    name = "makefile"
    cli_name = "makefile"
    cli_label = "Meta"

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
        return self.parse()

    @cli.click.group
    def render(self):
        """Subcommands for rendering"""

    @render.command("mermaid")
    @cli.click.option(
        "--title", help="diagram title", 
        default="Makefile Targets")
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

    @cli.click.flag("--graph", "only_graph", help="Returns only the prerequisites-graph")
    @cli.click.argument(
        "makefile", 
        # help="Return only the prerequisites-graph"
        default='',
        required=False,
        )
    def parse(self, makefile:str=None, only_graph: bool = False):
        """Parse Makefile to JSON.  Includes DAGs for targets, target-body, and target-type details """
        makefile=makefile or self.config['file']
        out = makefile_parse(makefile=makefile)
        if only_graph:
            out = {t: out[t]["prereqs"] for t in out}
        return out

    # def bootstrap(self):
    #     """ placeholder """
    #     raise NotImplementedError()
