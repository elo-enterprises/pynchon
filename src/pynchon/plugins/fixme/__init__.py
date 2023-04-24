""" pynchon.plugins.fixme
"""
import click

from pynchon import constants, abcs
from pynchon.bin import common, groups, options
from pynchon.models import Plugin

class FixMeConfig(abcs.Config):
    config_key='fixme'

class FixMe(Plugin):
    """ """

    name = "fixme"
    config_kls = FixMeConfig
    defaults = dict()

    def plan(self, config):
        plan = super(self.__class__, self).plan(config)
        plan += [f"pynchon gen fixme --output {config.pynchon['docs_root']}/FIXME.md"]
        return plan

    # @staticmethod
    # def init_cli(kls):
    #     """"""
    #
    #     @common.kommand(
    #         name="fixme",
    #         parent=groups.gen,
    #         formatters=dict(markdown=constants.T_FIXME),
    #         options=[
    #             options.format_markdown,
    #             click.option(
    #                 "--output",
    #                 "-o",
    #                 default="docs/FIXME.md",
    #                 help=("output file to write.  (optional)"),
    #             ),
    #             options.stdout,
    #             options.header,
    #         ],
    #     )
    #     def gen_fixme(output, format, stdout, header):
    #         """
    #         Generate FIXME.md files, aggregating references to all FIXME's in code-base
    #         """
    #         from pynchon.api import project
    #         from pynchon.util.os import invoke
    #
    #         config = project.get_config()
    #         src_root = config.pynchon['src_root']
    #         exclude_patterns = config.pynchon.get('exclude_patterns', [])
    #         cmd = invoke(f'grep --line-number -R FIXME {src_root}')
    #         assert cmd.succeeded
    #         items = []
    #         for line in cmd.stdout.split('\n'):
    #             line = line.strip()
    #             if not line or line.startswith('Binary file'):
    #                 continue
    #             bits = line.split(":")
    #             file = bits.pop(0)
    #             line_no = bits.pop(0)
    #             items.append(dict(file=file, line=':'.join(bits), line_no=line_no))
    #         return dict(items=items)
