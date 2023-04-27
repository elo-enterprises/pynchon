""" pynchon.util.text CLI
"""
import os
import json

import click

from pynchon.bin import options
from pynchon.util import lme, text, typing
from pynchon.util.os import invoke

LOGGER = lme.get_logger(__name__)


@click.group()
def cli() -> None:
    """
    CLI for interacting with pynchon.util.text
    """


@cli.group('json5')
def json5() -> None:
    """helpers for working with json5"""


@cli.group('json')
def _json() -> None:
    """
    helpers for working with json
    """


@cli.group('j2')
def j2() -> None:
    """
    helpers for interacting with `j2`.
    assumes j2cli is installed already.
    """


@j2.command('render')
@options.option_output
@options.option_print
@click.option('--context', help='context file.  must be JSON')
@click.argument("file", nargs=1)
def j2_render(
    output: str, should_print: bool, file: str, context: str, format: str = 'json'
) -> None:
    """
    renders the named file, using the given context-file.
    """
    cmd = f'j2 --format {format} {file} {context}'
    result = invoke(cmd)
    if not result.succeeded:
        LOGGER.critical(f'failed to execute: {cmd}')
        raise SystemExit(1)
    result = result.stdout
    assert result
    tmp = file.replace('.j2', '')
    if tmp.endswith('.json') or tmp.endswith('.json5'):
        LOGGER.debug(f"target @ {file} appears to be specifying json.")
        LOGGER.debug("loading as if json5 before display..")
        result = text.load_json5(content=result)
        result = json.dumps(result, indent=2)
    msg = result
    print(msg, file=open(output, 'w'))
    if should_print and output != '/dev/stdout':
        print(msg)


@_json.command('load')
@click.argument("files", nargs=-1)
def json_load(
    files: typing.List[str],
) -> None:
    """
    loads json5 file(s) and outputs json.
    if multiple files are provided, files will
    be merged with overwrites in the order provided
    """
    out: typing.Dict[str, typing.Any] = {}
    for file in files:
        obj = text.load_json(file=file)
        out = {**out, **obj}
    print(json.dumps(out, indent=2))


@json5.command('load')
@click.option(
    '--wrap-with-key',
    'wrapper_key',
    help='when set, wraps output as `{WRAPPER_KEY:output}`',
    # var='WRAPPER_KEY',
    default='',
)
@options.option_output
@options.option_print
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
def json5_load(
    output: str = '',
    should_print: bool = False,
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
    loads json5 file(s) and outputs json.
    if multiple files are provided, files will
    be merged with overwrites in the order provided
    """
    out: typing.Dict[str, typing.Any] = {}
    for file in files:
        obj = text.load_json5(file=file)
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
            push = text.load_json5(content=push_json_data)
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
            msg = json.dumps(out, indent=2)
        else:
            msg = str(out)
    else:
        msg = json.dumps(out, indent=2)
    print(msg, file=open(output, 'w'))
    if should_print and output != '/dev/stdout':
        print(msg)


if __name__ == '__main__':
    cli()
