""" pynchon.plugins.deck
"""
from pynchon import abcs, cli, events, models  # noqa
from pynchon.util import lme, tagging, typing  # noqa

LOGGER = lme.get_logger(__name__)


class Deck(models.ResourceManager):
    """Tool for working with markdown based slide-decks"""

    class config_class(abcs.Config):
        config_key: typing.ClassVar[str] =  "deck"
        defaults = dict(
            pandoc_docker="pandoc/core",
            pandoc_engine="dzslides",
            pandoc_args="",
            apply_hooks=["open-after"],
            include_patterns=["*.md"],
        )

    name = "deck"
    cli_name = "deck"
    cli_label = "Tool"
    contribute_plan_apply = True

    def plan(self, **kwargs):
        plan = super().plan()
        root = self["root"]
        root = abcs.Path(root)
        if not root.exists():
            plan.append(
                self.goal(resource=root, type="mkdir", command=f"mkdir -p {root}")
            )
        for rsrc in self.list():
            output = rsrc.parents[0] / (rsrc.stem + ".html")
            proot = self[:"pynchon.root"]
            output = output.relative_to(proot)
            relr = rsrc.relative_to(proot)
            fargs = {
                **self.config,
                **dict(
                    relr=relr, pandoc_args=" ".join(self["pandoc_args"]), output=output
                ),
            }
            plan.append(
                self.goal(
                    resource=output.absolute(),
                    type="gen",
                    command=(
                        "docker run -v `pwd`:/workspace "
                        "-w /workspace "
                        "{pandoc_docker} "
                        "-t {pandoc_engine} -s {relr} -o {output} {pandoc_args}"
                    ).format(**fargs),
                )
            )
        return plan
