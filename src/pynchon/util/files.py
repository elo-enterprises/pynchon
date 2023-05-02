""" pynchon.util.files
"""
import re
import glob
import difflib
import functools

from pynchon.abcs import Path
from pynchon.util.os import invoke

from . import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)


def diff_report(diff, logger=LOGGER.debug):
    """ """
    import pygments
    import pygments.lexers
    import pygments.formatters

    tmp = pygments.highlight(
        diff,
        lexer=pygments.lexers.get_lexer_by_name('udiff'),
        formatter=pygments.formatters.get_formatter_by_name('terminal16m'),
    )
    logger(f"scaffold drift: \n\n{tmp}\n\n")


def diff_percent(f1, f2):
    """ """
    with open(f1, 'r') as src:
        with open(f2, 'r') as dest:
            src_c = src.read()
            dest_c = dest.read()
    sm = difflib.SequenceMatcher(None, src_c, dest_c)
    return 100 * (1.0 - sm.ratio())


def diff(f1, f2):
    """ """
    with open(f1, 'r') as src:
        with open(f2, 'r') as dest:
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
    path = Path(path).absolute()
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
        Path(src_root).joinpath("**/*"),
    ]
    quiet or LOGGER.info(f"finding src under {globs}")
    globs = [glob.glob(str(x), recursive=True) for x in globs]
    matches = functools.reduce(lambda x, y: x + y, globs)
    matches = [str(x.absolute()) for x in map(Path, matches) if not x.is_dir()]
    # LOGGER.debug(matches)
    matches = [
        m for m in matches if not any([p.match(str(m)) for p in exclude_patterns])
    ]
    return matches


# def find_globs(
#     globs: typing.List[str],
#     quiet: bool = False,
# ) -> typing.List[str]:
#     quiet or LOGGER.debug(f"matching globs: {globs}")
#     globs = [glob.glob(str(x), recursive=True) for x in globs]
#     matches = functools.reduce(lambda x, y: x + y, globs)
#     return matches


import pydantic

from pynchon import abcs


@pydantic.validate_arguments
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
            result.append(Path(m))
    return result


# def find_j2s(conf) -> list:
#     """ """
#     from pynchon import abcs, config
#
#     project = config.project.get("subproject", config.project)
#     project_root = project.get("root", config.git["root"])
#     globs = [
#         Path(project_root).joinpath("**/*.j2"),
#     ]
#     LOGGER.debug(f"finding .j2s under {globs}")
#     globs = [glob.glob(str(x), recursive=True) for x in globs]
#     matches = functools.reduce(lambda x, y: x + y, globs)
#     includes = []
#     for i, m in enumerate(matches):
#         for d in config.jinja.includes:
#             if abcs.Path(d).has_file(m):
#                 includes.append(m)
#             else:
#                 LOGGER.warning(f"'{d}'.has_file('{m}') -> false")
#     j2s = [Path(m).relative_to(".") for m in matches if m not in includes]
#     return j2s
