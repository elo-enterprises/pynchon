""" pynchon.plugins.makefile
"""
from memoized_property import memoized_property

from pynchon.util.os import invoke

from pynchon import abcs, cli, events, models  # noqa
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
        return abcs.Path(self[:"src.root"]) / "Makefile"

    @memoized_property
    def database(self) -> typing.List:
        tmp = self.fpath.parents[0]
        cmd = f"ls Makefile && make --print-data-base -pqRrs -f Makefile"
        resp = invoke(cmd).stdout
        resp = resp.split("\n")
        return resp

    @property
    def parsed(self) -> typing.Dict:
        resp = self.database
        vstart = resp.index("# Variables")
        vend = resp.index("", vstart + 2)
        vars = resp[vstart:vend]
        resp = resp[vend:]
        irstart = resp.index("# Implicit Rules")
        frstart = resp.index("# Files")
        tend = resp.index("# files hash-table stats:")
        irend = frstart - 1
        implicit_targets_section = resp[irstart:irend]
        file_targets_section = resp[frstart:tend]
        def test(x): return all(
            [
                ":" in x.strip(),
                not x.startswith("#"),
                not x.startswith("."),
                not x.startswith("\t"),
            ]
        )
        file_target_names = list(filter(test, file_targets_section))
        implicit_target_names = list(filter(test, implicit_targets_section))
        targets = file_target_names + implicit_target_names
        out = {}
        for tline in targets:
            t, childs = tline.split(":")
            type = "implicit" if tline in implicit_targets_section else "file"
            # NB: line nos are from reformatted output, not original file
            line_start = resp.index(tline)
            line_end = resp.index("", line_start)
            body = resp[line_start:line_end]
            zzz = "#  recipe to execute (from '"
            pline = [x for x in body if zzz in x]
            pline = pline[0] if pline else None
            file = pline.split(zzz)[-1] if pline else None
            # import IPython; IPython.embed()
            lineno = pline and pline.split("', line ")[-1].split("):")[0]
            lineno = lineno and int(lineno)
            if file:
                file = file[: file.index("', line ")]
                try:
                    file = abcs.Path(file).relative_to(abcs.Path(".").absolute())
                except ValueError:
                    pass
            prereqs = [x for x in childs.split() if x.strip()]
            out[t] = dict(
                file=file,
                line=lineno,
                # line_start=line_start,
                # line_end=line_end,
                lineno=lineno,
                body=body,
                type=type,
                docs=[x[len("\t@#") :] for x in body if x.startswith("\t@#")],
                # alias=len(prereqs)==1 and not body,
                prereqs=prereqs,
            )
        return out

    @cli.click.group
    def gen(self):
        """generate"""

    @gen.command("diagram")
    # @cli.click.option('--template','makefile/mermaid.mmd.j2')
    # ls src/pynchon/templates/includes/pynchon/plugins/makefile/mermaid-graph.mmd.j2
    def _diagram(self):
        """ """
        # from pynchon.api import rende
        from pynchon import api

        tmpl = api.render.get_template(
            f"{self.plugin_templates_prefix}/mermaid-graph.mmd.j2"
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
