""" pynchon.util.files.diff
"""
import difflib

from pynchon import cli

from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)


def diff_report(diff, logger=LOGGER.debug):
    """ """
    # FIXME: use rich.syntax
    import pygments
    import pygments.lexers
    import pygments.formatters

    tmp = pygments.highlight(
        diff,
        lexer=pygments.lexers.get_lexer_by_name('udiff'),
        formatter=pygments.formatters.get_formatter_by_name('terminal16m'),
    )
    logger(f"scaffold drift: \n\n{tmp}\n\n")


@cli.arguments.file1
@cli.arguments.file2
def diff_percent(file1: str = None, file2: str = None):
    """
    calculates file-delta, returning a percentage
    """
    with open(file1, 'r') as src:
        with open(file2, 'r') as dest:
            src_c = src.read()
            dest_c = dest.read()
    sm = difflib.SequenceMatcher(None, src_c, dest_c)
    return 100 * (1.0 - sm.ratio())


@cli.arguments.file1
@cli.arguments.file2
def diff(file1: str = None, file2: str = None):
    """
    calculates a file-delta, returning a unified diff
    """
    with open(file1, 'r') as src:
        with open(file2, 'r') as dest:
            src_l = src.readlines()
            dest_l = dest.readlines()
    xdiff = difflib.unified_diff(
        src_l,
        dest_l,
        lineterm='',
        n=0,
    )
    return ''.join(xdiff)
