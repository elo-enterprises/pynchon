""" pynchon.util.text.loadf

    Helpers for loading data structures from files
"""
import os

from pynchon.cli import click, options
from pynchon.util import text
from pynchon.util.os import invoke
from pynchon.util.text import loads

from pynchon.util import lme, typing  # noqa


LOGGER = lme.get_logger(__name__)


def ini(*args, **kwargs):
    """parses ini file and returns JSON"""
    raise NotImplementedError()


def yaml(*args, **kwargs):
    """parses yaml file and returns JSON"""
    raise NotImplementedError()


def toml(*args, **kwargs):
    """parses toml file and returns JSON"""
    raise NotImplementedError()


# @click.argument("file", nargs=1)
# def json5(file: str = '',) -> dict:
#     """
#     loads json5 from file
#     """
#     assert file
#     if not os.path.exists(file):
#         raise ValueError(f'file @ {file} is missing!')
#     with open(file, 'r') as fhandle:
#         content = fhandle.read()
#     data = loads.json5(content)
#     return data


@click.option(
    '--wrap-with-key',
    'wrapper_key',
    help='when set, wraps output as `{WRAPPER_KEY:output}`',
    default='',
)
@options.output
@options.should_print
@click.option('--pull', help='when provided, this key will be output', default='')
@click.option(
    '--push-data', help='(string) this raw data will be added to output', default=''
)
@click.option(
    '--push-file-data',
    help='(filename) contents of file will be added to output',
    default='',
)
@click.option(
    '--push-json-data',
    help='(string) jsonified data will be added to output',
    default='',
)
@click.option(
    '--push-command-output', help="command's stdout will be added to output", default=''
)
@click.option('--under-key', help='required with --push commands', default='')
@click.argument("files", nargs=-1)
def json5(
    output: str = '',
    should_print: bool = False,
    file: str = '',
    files: typing.List[str] = [],
    wrapper_key: str = '',
    pull: str = '',
    push_data: str = '',
    push_file_data: str = '',
    push_json_data: str = '',
    push_command_output: str = '',
    under_key: str = '',
) -> None:
    """
    Parses JSON-5 file(s) and outputs json.

    If multiple files are provided, files will
    be merged (with overwrites) in the order provided.

    Pipe friendly.

    Several other options are available for common post-processing tasks.
    """
    # out = _json5_loadc(
    #     files=files,
    #     wrapper_key=wrapper_key,
    #     pull=pull,
    #     push_data=push_data,
    #     push_file_data=push_file_data,
    #     push_json_data=push_json_data,
    #     push_command_output=push_command_output,
    #     under_key=under_key,
    # )
    """
    loads json5 file(s) and outputs json.
    if multiple files are provided, files will
    be merged with overwrites in the order provided
    """
    out: typing.Dict[str, typing.Any] = {}
    for file in files:
        with open(file, 'r') as fhandle:
            obj = loads.json5(fhandle.read())
        out = {**out, **obj}

    push_args = [push_data, push_file_data, push_json_data, push_command_output]
    if any(push_args):
        assert under_key
        assert under_key not in out, f'content already has key@{under_key}!'
        assert (
            sum([1 for x in push_args if x]) == 1
        ), 'only one --push arg can be provided!'
        if push_data:
            assert isinstance(push_data, (str,))
            push = push_data
        elif push_command_output:
            cmd = invoke(push_command_output)
            if cmd.succeeded:
                push = cmd.stdout
            else:
                err = cmd.stderr
                LOGGER.critical(err)
                raise SystemExit(1)
        elif push_json_data:
            push = loads.json5(content=push_json_data)
        elif push_file_data:
            err = f'file@{push_file_data} doesnt exist'
            assert os.path.exists(push_file_data), err
            with open(push_file_data, 'r') as fhandle:
                push = fhandle.read()
        out[under_key] = push

    if wrapper_key:
        # NB: must remain after push
        out = {wrapper_key: out}

    if pull:
        out = out[pull]
        # similar to `jq -r`.
        # we don't want quoted strings, but
        # if the value is complex, we need json-encoding
        if not isinstance(out, (str,)):
            msg = text.to_json(out)
        else:
            msg = str(out)
    else:
        msg = text.to_json(out)
    output = output or '/dev/stdout'
    print(msg, file=open(output, 'w'))
    if should_print and output != '/dev/stdout':
        print(msg)


@options.strict
@click.argument("file", nargs=1)
def json(file: str = '', content: str = '', strict: bool = True) -> dict:
    """
    loads json to python dictionary from given file or string
    """
    if file:
        assert not content
        if not os.path.exists(file):
            raise ValueError(f'file @ {file} is missing!')
        with open(file, 'r') as fhandle:
            content = fhandle.read()
    try:
        data = loads.json(content)
        # data = pyjson5.loads(content)
    # except (pyjson5.Json5EOF,) as exc:
    except (ValueError,) as exc:
        LOGGER.critical(f"Cannot parse json from {file}!")
        raise
    return data
