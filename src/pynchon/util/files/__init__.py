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
@cli.click.option(
    '--clean',
    is_flag=True,
    default=False,
    help='when provided, prepend_file will be removed afterwards',
)
def prepend(
    prepend_file: str = None,
    target_file: str = None,
    clean: bool = False,
):
    """
    prepends given file contents to given target
    """
    clean = '' if not clean else f' && rm {prepend_file}'
    cmd = ' '.join(
        [
            "printf '%s\n%s\n'",
            f'"$(cat {prepend_file})" "$(cat {target_file})"',
            f'> {target_file} {clean}',
        ]
    )
    return invoke(cmd)


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


def block_in_file(
    target_file,
    block_file,
    create="no",
    insertbefore="BOF",
    backup="yes",
    marker='# {mark} ANSIBLE MANAGED BLOCK - pynchon',):
    """
    """
    from pynchon.util.os import invoke
    assert "'" not in marker
    from pynchon import abcs
    target_file = abcs.Path(target_file)
    assert target_file.exists()
    target_file=target_file.absolute()
    dest=".tmp.ansible.blockinfile.out"
    invoke(f'cp {target_file} {dest}')
    block_file = abcs.Path(block_file)
    assert block_file.exists()
    block_file=block_file.absolute()
    args = [
        f"marker='{marker}'",
        f"dest={dest}",
        'block=\\"{{ lookup(\'file\', fname)}}\\"',
        f"create={create} insertbefore={insertbefore} ",
        f"backup={backup}",]
    args = ' '.join(args)
    cmd = [
        "docker run",
        "-w /workspace",
        "-v `pwd`:/workspace",
        f"-v {block_file}:{block_file}",
        # f"-v {target_file}:{target_file}",
        "-e ANSIBLE_STDOUT_CALLBACK=json",
        "-e ANSIBLE_CALLBACKS_ENABLED=json",
        "-e ANSIBLE_LOAD_CALLBACK_PLUGINS=1",
        "--entrypoint ansible alpinelinux/ansible",
        "local -i local, -c local",
        f"-e fname={block_file}",
        "-mblockinfile",
        "--args",
        '"'+args+'"',
    ]
    cmd=' '.join(cmd)
    LOGGER.critical(cmd)
    result = invoke(cmd,system=True)
    assert result.succeeded
    invoke(f'mv {dest} {target_file}')
    assert result.succeeded
    # result = invoke(cmd,load_json=True)
    # return dict(ansible=dict(stats=result.json['stats']))
    # LOGGER.debug(result.stdout)
    # LOGGER.debug(result.stderr)
    # return result.succeeded
    # {} #result.suceeded #json['stats']
