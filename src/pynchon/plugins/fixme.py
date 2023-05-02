""" pynchon.plugins.fixme
"""
from fnmatch import fnmatch

from pynchon import constants, abcs, models
from pynchon.cli import click, options, common
from pynchon.util import typing, lme
from pynchon.util.os import invoke

LOGGER = lme.get_logger(__name__)


class FixMeConfig(abcs.Config):
    config_key = 'fixme'


class FixMe(models.Planner):
    """Generates {docs_root}/FIXME.md from source"""

    name = "fixme"
    config_class = FixMeConfig
    defaults = dict()

    def plan(self, config: dict = None) -> typing.List:
        """...."""
        from pynchon.config import pynchon

        config = config or self.__class__.get_current_config()
        plan = super(self.__class__, self).plan(config)
        plan += [f"pynchon fixme gen --output {pynchon['docs_root']}/FIXME.md"]
        return plan

    @classmethod
    def asdasdinit_cli(kls):
        """"""
        parent = kls.click_group
        T_FIXME = constants.ENV.get_template(
            "pynchon/plugins/plugins/fixme/FIXME.md.j2"
        )

        @common.kommand(
            name="gen",
            parent=parent,
            formatters=dict(markdown=T_FIXME),
            options=[
                options.format_markdown,
                click.option(
                    "--output",
                    "-o",
                    default="docs/FIXME.md",
                    help=("output file to write.  (optional)"),
                ),
                options.stdout,
                options.header,
            ],
        )
        def gen(output, format, stdout, header):
            """
            Generate FIXME.md files, aggregating references to all FIXME's in code-base
            """
            config = kls.project_config
            src_root = config.pynchon['src_root']
            exclude_patterns = config.fixme.get('exclude_patterns', [])
            cmd = invoke(f'grep --line-number -R FIXME {src_root}')
            assert cmd.succeeded
            items = []
            skipped = {}
            for line in cmd.stdout.split('\n'):
                line = line.strip()
                if not line or line.startswith('Binary file'):
                    continue
                bits = line.split(":")
                file = bits.pop(0)
                path = abcs.Path(file)
                for g in exclude_patterns:
                    if fnmatch(file, g):
                        skipped[g] = skipped.get(g, []) + [file]
                        break
                else:
                    line_no = bits.pop(0)
                    items.append(dict(file=file, line=':'.join(bits), line_no=line_no))
            for g in skipped:
                msg = f"exclude_pattern @ `{g}` skipped {len(skipped[g])} matches"
                LOGGER.warning(msg)
            return dict(items=items)
