""" pynchon.util.files
"""
import functools
import glob
import re

from pynchon import abcs, cli
from pynchon.util import lme, os, typing  # noqa

from .diff import diff, diff_percent, diff_report  # noqa

LOGGER = lme.get_logger(__name__)


@cli.click.argument("prepend_file", nargs=1)
@cli.click.argument("target_file", nargs=1)
@cli.click.option(
    "--clean",
    is_flag=True,
    default=False,
    help="when provided, prepend_file will be removed afterwards",
)
def prepend(
    prepend_file: str = None,
    target_file: str = None,
    clean: bool = False,
):
    """prepends given file contents to given target

    :param prepend_file: str:  (Default value = None)
    :param target_file: str:  (Default value = None)
    :param clean: bool:  (Default value = False)
    :param prepend_file: str:  (Default value = None)
    :param target_file: str:  (Default value = None)
    :param clean: bool:  (Default value = False)

    """
    clean = "" if not clean else f" && rm {prepend_file}"
    cmd = " ".join(
        [
            "printf '%s\n%s\n'",
            f'"$(cat {prepend_file})" "$(cat {target_file})"',
            f"> {target_file} {clean}",
        ]
    )
    return os.invoke(cmd)


def find_suffix(root: str = "", suffix: str = "") -> typing.StringMaybe:
    """
    :param root: str:  (Default value = '')
    :param suffix: str:  (Default value = '')
    """
    assert root and suffix
    return os.invoke(f"{root} -type f -name *.{suffix}").stdout.split("\n")


@functools.lru_cache(maxsize=None)
def get_git_root(path: str = ".") -> typing.StringMaybe:
    """
    :param path: str:  (Default value = ".")
    """
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
            LOGGER.warning(f"Could not find a git-root for '{path}'")


def find_src(
    src_root: str,
    exclude_patterns=[],
    quiet: bool = False,
) -> list:
    """

    :param src_root: str:
    :param exclude_patterns: Default value = [])
    :param quiet: bool:  (Default value = False)
    :param src_root: str:
    :param quiet: bool:  (Default value = False)

    """
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
    """

    :param globs: typing.List[abcs.Path]:
    :param includes: Default value = [])
    :param logger: object:  (Default value = None)
    :param quiet: bool:  (Default value = False)
    :param globs: typing.List[abcs.Path]:
    :param logger: object:  (Default value = None)
    :param quiet: bool:  (Default value = False)

    """
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
    volumes: dict = {},
    container: str = "alpinelinux/ansible",
    entrypoint: str = "ansible",
    local: bool = True,
    e: dict = {},
    module_name: str = None,
    extra: typing.List[str] = [],
) -> typing.List[str]:
    """

    :param volumes: dict:  (Default value = {})
    :param container: str:  (Default value = "alpinelinux/ansible")
    :param entrypoint: str:  (Default value = 'ansible')
    :param local: bool:  (Default value = True)
    :param e: dict:  (Default value = {})
    :param module_name: str:  (Default value = None)
    :param extra: typing.List[str]:  (Default value = [])
    :param volumes: dict:  (Default value = {})
    :param container: str:  (Default value = "alpinelinux/ansible")
    :param entrypoint: str:  (Default value = 'ansible')
    :param local: bool:  (Default value = True)
    :param e: dict:  (Default value = {})
    :param module_name: str:  (Default value = None)
    :param extra: typing.List[str]:  (Default value = [])

    """
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


def dumps(
    content: str = None, file: str = None, quiet: bool = True, logger=LOGGER.info
):
    """

    :param content: str:  (Default value = None)
    :param file: str:  (Default value = None)
    :param quiet: bool:  (Default value = True)
    :param logger: Default value = LOGGER.info)
    :param content: str:  (Default value = None)
    :param file: str:  (Default value = None)
    :param quiet: bool:  (Default value = True)

    """
    quiet or logger(f"\n{content}")
    with open(file, "w") as fhandle:
        fhandle.write(content)
    quiet or logger(f'Wrote "{file}"')


def block_in_file(
    target_file: str,
    block_file: str,
    create: str = "no",
    insertbefore: str = "BOF",
    backup: str = "yes",
    marker: str = "# {mark} ANSIBLE MANAGED BLOCK - pynchon",
    dest=".tmp.ansible.blockinfile.out",
):
    """

    :param target_file: str:
    :param block_file: str:
    :param create: str:  (Default value = "no")
    :param insertbefore: str:  (Default value = "BOF")
    :param backup: str:  (Default value = "yes")
    :param marker: str:  (Default value = '# {mark} ANSIBLE MANAGED BLOCK - pynchon')
    :param dest: Default value = ".tmp.ansible.blockinfile.out")
    :param target_file: str:
    :param block_file: str:
    :param create: str:  (Default value = "no")
    :param insertbefore: str:  (Default value = "BOF")
    :param backup: str:  (Default value = "yes")
    :param marker: str:  (Default value = '# {mark} ANSIBLE MANAGED BLOCK - pynchon')

    """
    assert "'" not in marker
    target_file = abcs.Path(target_file).absolute()
    block_file = abcs.Path(block_file).absolute()
    assert target_file.exists()
    assert block_file.exists()
    os.invoke(f"cp {target_file} {dest}")
    blockinfile_args = [
        "dest={{dest}}",
        f"marker='{marker}'",
        "backup={{backup}}",
        "block=\\\"{{ lookup('file', block_file)}}\\\"",
        "create={{create}} insertbefore={{insertbefore}} ",
    ]
    blockinfile_args = " ".join(blockinfile_args)
    cmd_components = ansible_docker(
        local=True,
        volumes={block_file: block_file},
        e=dict(
            dest=dest,
            insertbefore=insertbefore,
            backup=backup,
            create=create,
            block_file=block_file,
        ),
        module_name="blockinfile",
        extra=[
            f'--args "{blockinfile_args}"',
        ],
    )
    cmd = " ".join(cmd_components)
    result = os.invoke(cmd, system=True)
    assert result.succeeded, result.stderr
    os.invoke(f"mv {dest} {target_file}")
    assert result.succeeded, result.stderr
    return True
