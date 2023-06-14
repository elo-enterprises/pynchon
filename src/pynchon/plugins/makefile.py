""" pynchon.plugins.makefile
"""
from pynchon import abcs, cli, events, models  # noqa
from pynchon.util import lme, tagging, typing  # noqa
from pynchon.util.os import invoke

LOGGER = lme.get_logger(__name__)


class Make(models.Provider):
    """ Makefile parser """

    class config_class(abcs.Config):
        config_key = "makefile"

    name = "makefile"
    cli_name = "makefile"
    cli_label = "Meta"
    @property
    def fpath(self):
        return abcs.Path(self[:'src.root'])/'Makefile'

    @cli.click.group
    def gen(self):
        """ generate """

    @gen.command('diagram')
    def _diagram(self):
        """ """

    def parse(self):
        """ placeholder """
        tmp=self.fpath.parents[0]
        cmd = f'ls Makefile && make --print-data-base -pqRrs -f Makefile'
        resp = invoke(cmd).stdout
        resp=resp.split('\n')
        vstart=resp.index('# Variables')
        vend=resp.index('',vstart+2)
        vars = resp[vstart:vend]
        resp=resp[vend:]
        irstart = resp.index('# Implicit Rules')
        frstart=resp.index('# Files')
        tend = resp.index('# files hash-table stats:')
        irend = frstart-1
        implicit_targets=resp[irstart:irend]
        file_targets = resp[frstart:tend]
        file_target_names = [
            x for x in file_targets if all([
                ':' in x.strip(),
                 not x.startswith('#'),
                 not x.startswith('.'),
                 not x.startswith('\t'),
                ])
                ]
        implicit_target_names = [
            x for x in implicit_targets if all([
                ':' in x.strip(),
                 not x.startswith('#'),
                 not x.startswith('\t'),
                ])]
        targets = [t.split(':') for t in file_target_names+implicit_target_names]
        out={}
        for t,childs in targets:
            xxx=':'.join([t,childs])
            out[t]=dict(
                type='implicit' if xxx in implicit_targets else 'file',
                # alias=len(prereqs)==1 and not implementation
                prereqs=[x for x in childs.split() if x.strip()])
        return out

    def bootstrap(self):
        """ placeholder """
        raise NotImplementedError()
