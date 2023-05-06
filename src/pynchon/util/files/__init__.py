""" pynchon.util.files
"""
import re
import glob
import difflib
import functools

from pynchon import abcs, cli
from pynchon.cli import click, options
from pynchon.util.os import invoke
from pynchon.util.tagging import tags

from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)


@cli.click.argument('prepend_file', nargs=1)
@cli.click.argument('target_file', nargs=1)
def prepend(
    prepend_file: str,
    target_file: str = None,
    # template_context:dict={},
):
    """
    prepends given file contents to given target
    """
    invoke(
        f'''printf '%s\n%s\n' "$(cat {prepend_file})" "$(cat {target_file})" > {target_file}'''
    )


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


def find_suffix(root: str = '', suffix: str = '') -> typing.StringMaybe:
    assert root and suffix
    return invoke(f"{root} -type f -name *.{suffix}").stdout.split("\n")


def get_git_root(path: str = ".") -> typing.StringMaybe:
    """ """
    path = abcs.Path(path).absolute()
    tmp = path / ".git"
    if tmp.exists():
        return tmp
    elif not path:
        return None
    else:
        try:
            return get_git_root(path.parents[0])
        except IndexError:
            LOGGER.critical("Could not find a git-root!")


def find_src(
    src_root: str,
    exclude_patterns=[],
    quiet: bool = False,
) -> list:
    """ """
    exclude_patterns = set(list(map(re.compile, exclude_patterns)))
    globs = [
        abcs.Path(src_root).joinpath("**/*"),
    ]
    quiet or LOGGER.info(f"finding src under {globs}")
    globs = [glob.glob(str(x), recursive=True) for x in globs]
    matches = functools.reduce(lambda x, y: x + y, globs)
    matches = [str(x.absolute()) for x in map(abcs.Path, matches) if not x.is_dir()]
    # LOGGER.debug(matches)
    matches = [
        m for m in matches if not any([p.match(str(m)) for p in exclude_patterns])
    ]
    return matches


@typing.validate_arguments
def find_globs(
    globs: typing.List[abcs.Path],
    includes=[],
    quiet: bool = False,
) -> typing.List[str]:
    """ """
    # from pynchon import abcs
    # from pynchon.plugins import registry
    #
    # obj = registry['jinja']['obj']
    # config import
    quiet or LOGGER.info(f"finding files matching {globs}")
    globs = [glob.glob(str(x), recursive=True) for x in globs]
    matches = functools.reduce(lambda x, y: x + y, globs)

    for i, m in enumerate(matches):
        for d in includes:
            if abcs.Path(d).has_file(m):
                includes.append(m)
            # else:
            #     LOGGER.warning(f"'{d}'.has_file('{m}') -> false")
    result = []
    for m in matches:
        assert m
        if m not in includes:
            result.append(abcs.Path(m))
    return result
