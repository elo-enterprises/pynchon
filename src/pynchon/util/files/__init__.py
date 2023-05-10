""" pynchon.util.files
"""
import re
import glob
import functools

from pynchon import abcs, cli

from pynchon.util import lme, typing, os  # noqa

from .diff import diff_report, diff_percent, diff  # noqa

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
    return os.invoke(cmd)


def find_suffix(root: str = '', suffix: str = '') -> typing.StringMaybe:
    assert root and suffix
    return os.invoke(f"{root} -type f -name *.{suffix}").stdout.split("\n")


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
    logger: object = None,
    quiet: bool = False,
) -> typing.List[str]:
    """ """
    logger = logger or LOGGER
    quiet or logger.info(f"finding files matching {globs}")
    globs = [glob.glob(str(x), recursive=True) for x in globs]
    matches = functools.reduce(lambda x, y: x + y, globs)
    for i, m in enumerate(matches):
        for d in includes:
            if abcs.Path(d).has_file(m):
                includes.append(m)
    result = []
    for m in matches:
        assert m
        if m not in includes:
            result.append(abcs.Path(m))
    return result


def ansible_docker(
    local: bool = True,
    volumes: dict = {},
    container: str = "alpinelinux/ansible",
    entrypoint: str = 'ansible',
    e: dict = {},
    module_name: str = None,
    extra: typing.List[str] = [],
) -> typing.List[str]:
    """ """
    vextras = [f"-v {k}:{v}" for k, v in volumes.items()]
    cmd = (
        [
            "docker run",
            "-w /workspace",
            "-v `pwd`:/workspace",
        ]
        + vextras
        + [
            "-e ANSIBLE_STDOUT_CALLBACK=json",
            "-e ANSIBLE_CALLBACKS_ENABLED=json",
            "-e ANSIBLE_LOAD_CALLBACK_PLUGINS=1",
            f"--entrypoint {entrypoint} ",
            f"{container}",
        ]
    )
    local and cmd.append("local -i local, -c local")
    e and [cmd.append(f"-e {k}={v}") for k, v in e.items()]
    module_name and cmd.append(f"--module-name {module_name}")

    return cmd + extra


def dumps(content: str = None, file: str = None, logger=LOGGER.info):
    logger(f"\n{content}")
    with open(file, 'w') as fhandle:
        fhandle.write(content)
    logger(f'Wrote "{file}"')


def block_in_file(
    target_file: str,
    block_file: str,
    create: str = "no",
    insertbefore: str = "BOF",
    backup: str = "yes",
    marker: str = '# {mark} ANSIBLE MANAGED BLOCK - pynchon',
):
    """ """
    dest = ".tmp.ansible.blockinfile.out"
    assert "'" not in marker
    target_file = abcs.Path(target_file).absolute()
    block_file = abcs.Path(block_file).absolute()
    assert target_file.exists()
    assert block_file.exists()
    os.invoke(f'cp {target_file} {dest}')
    blockinfile_args = [
        f"marker='{marker}'",
        f"dest={dest}",
        f"backup={backup}",
        'block=\\"{{ lookup(\'file\', fname)}}\\"',
        f"create={create} insertbefore={insertbefore} ",
    ]
    blockinfile_args = ' '.join(blockinfile_args)
    cmd_components = ansible_docker(
        local=True,
        volumes={block_file: block_file},
        e=dict(fname=block_file),
        module_name='blockinfile',
        extra=[
            f'--args "{blockinfile_args}"',
        ],
    )
    cmd = ' '.join(cmd_components)
    result = os.invoke(cmd, system=True)
    assert result.succeeded, result.stderr
    os.invoke(f'mv {dest} {target_file}')
    # result = os.invoke(cmd,load_json=True)
    # return dict(ansible=dict(stats=result.json['stats']))
    # LOGGER.debug(result.stdout)
    # LOGGER.debug(result.stderr)
    # return result.json['stats']
    assert result.succeeded, result.stderr
    return True
