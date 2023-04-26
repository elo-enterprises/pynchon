""" pynchon.plugins.fixme
"""
from fnmatch import fnmatch

import click

from pynchon import constants, abcs
from pynchon.bin import common, groups, options
from pynchon.util import typing, lme
from pynchon.models import Plugin
from pynchon.util.os import invoke

LOGGER = lme.get_logger(__name__)

T_FIXME = constants.ENV.get_template("FIXME.md.j2")


class FixMeConfig(abcs.Config):
    config_key = 'fixme'


class FixMe(Plugin):
    """ """

    name = "fixme"
    config_kls = FixMeConfig
    defaults = dict()

    def plan(self, config: dict = None) -> typing.List:
        """ """
        from pynchon.config import pynchon

        config = config or self.__class__.get_current_config()
        plan = super(self.__class__, self).plan(config)
        plan += [f"pynchon fixme gen --output {pynchon['docs_root']}/FIXME.md"]
        return plan

    @staticmethod
    def init_cli(kls):
        """"""
        plugin_main = Plugin.init_cli(kls)

        @common.kommand(
            name="gen",
            parent=plugin_main,
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
                for g in exclude_patterns:
                    if fnmatch(file, g):
                        skipped[g] = skipped.get(g, []) + [file]
                        break
                else:
                    line_no = bits.pop(0)
                    items.append(dict(file=file, line=':'.join(bits), line_no=line_no))
            for g in skipped:
                LOGGER.warning(
                    f"exclude_pattern @ `{g}` skipped {len(skipped[g])} matches"
                )
            return dict(items=items)
