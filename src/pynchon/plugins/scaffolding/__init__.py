""" pynchon.plugins.scaffolding
"""
import difflib
from pynchon.util.os import invoke
from pynchon import abcs
from pynchon.util import lme, typing, files  # , files
from pynchon.models import Plugin

from .config import ScaffoldingConfig

LOGGER = lme.get_logger(__name__)


class ScaffoldingItem(abcs.AttrDict):
    warnings = []

    @property
    def exists(self):
        import os

        return os.path.exists(self.src)

    def validate(self):
        if not self.exists and self.src not in ScaffoldingItem.warnings:
            LOGGER.critical(f"Scaffolding source @ {self.src} does not exist!")
            ScaffoldingItem.warnings.append(self.src)

    def __init__(
        self, name='unnamed scaffold', scope='*', pattern=None, src=None, **kwargs
    ):
        assert pattern is not None
        assert src is not None
        super(ScaffoldingItem, self).__init__(
            name=name, scope=scope, src=src, pattern=pattern, **kwargs
        )
        self.validate()


class Scaffolding(Plugin):
    """ """

    priority = 0
    name = "scaffolding"
    cli_name = 'scaffold'
    defaults = dict()
    config_kls = ScaffoldingConfig

    @property
    def plugin_config(self):
        return self.get_current_config()

    def match(self, pattern=None):
        """
        returns files that match for all scaffolds
        """
        if pattern:
            return files.find_globs([pattern], quiet=True)
        else:
            matches = []
            for scaffold in self.scaffolds:
                LOGGER.debug(
                    f"scaffold @ `{scaffold.pattern}` with scope {scaffold.scope}:"
                )
                matched_scaffold = ScaffoldingItem(
                    **{**scaffold, **dict(matches=self.match(pattern=scaffold.pattern))}
                )
                matches.append(matched_scaffold)
            return matches

    @property
    def matches(self):
        return self.match()

    def stat(self):
        """status of current scaffolding"""
        ignore_keys = 'diff'.split()
        diff = self.diff(quiet=True)
        modified = [
            dict([k, v] for k, v in s.items() if k not in ignore_keys)
            for s in diff['modified']
        ]
        return dict(errors=diff['errors'], modified=modified)

    @property
    def scaffolds(self):
        """ """
        result = self.plugin_config.get('scaffolds', [])
        return [ScaffoldingItem(**x) for x in result]

    def list(self):
        """list available scaffolds"""
        return self.scaffolds

    def diff(self, quiet:bool=False):
        """diff with known scaffolding"""
        result = dict(errors=[], modified=[])
        for matched_scaffold in self.matches:
            for fname in matched_scaffold.matches:
                if matched_scaffold.exists:
                    diff = invoke(f'diff {fname} {matched_scaffold.src}')
                    if diff.succeeded:
                        LOGGER.debug(f"no diff detected for {fname}")
                    else:
                        with open(matched_scaffold.src, 'r') as src:
                            with open(fname, 'r') as dest:
                                src_l = src.readlines()
                                dest_l = dest.readlines()
                        xdiff = difflib.unified_diff(
                            src_l, dest_l, lineterm='', n=0,)
                        with open(matched_scaffold.src, 'r') as src:
                            with open(fname, 'r') as dest:
                                src_c = src.read()
                                dest_c = dest.read()
                        sm = difflib.SequenceMatcher(None, src_c, dest_c)
                        this_diff=''.join(xdiff)
                        result['modified'].append(
                            dict(
                                src=matched_scaffold.src,
                                fname=fname,
                                percent_diff=f'{100*(1.0-sm.ratio())}%',
                                # diff=this_diff,
                                # diff=diff.stdout
                            )
                        )
                        import pygments
                        import pygments.lexers
                        import pygments.formatters
                        tmp=pygments.highlight(
                            this_diff,
                            lexer=pygments.lexers.get_lexer_by_name('udiff'),
                            formatter=pygments.formatters.get_formatter_by_name('terminal16m'))
                        LOGGER.debug(f"scaffold drift: \n\n{tmp}\n\n")
                else:
                    result['errors'].append(fname)
        return result

    def plan(self, config) -> typing.List[str]:
        """ """
        plan = super(Scaffolding, self).plan(config)
        for fname in self.diff():
            plan += [f"echo {fname} different!"]
        return plan
