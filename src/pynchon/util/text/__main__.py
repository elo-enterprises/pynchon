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
    pynchon.util.text CLI
    """
entry=cli
from .render.__main__ import j2cli

@cli.group('loads')
def loads() -> None:
    """ load string to ~JSON """

@cli.group('loadf')
def loadf() -> None:
    """ load file-content to ~JSON """

@cli.group('json')
def _json() -> None:
    """
    helpers for working with json
    """


# @cli.group('j2')
# def j2() -> None:
#     """
#     helpers for interacting with `j2`.
#     (assumes j2cli is installed already)
#     """


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
        obj = text.loadf_json(file=file)
        out = {**out, **obj}
    print(text.to_json(out))
loadf.add_command(click.command('json')(json_load))

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
    out = text.json5_loadc(
        files=files,
        wrapper_key=wrapper_key,
        pull=pull,
        push_data=push_data,
        push_file_data=push_file_data,
        push_json_data=push_json_data,
        push_command_output=push_command_output,
        under_key=under_key,
    )
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
    print(msg, file=open(output, 'w'))

    if should_print and output != '/dev/stdout':
        print(msg)
# entry.add_command(click.Command(json5_load, name='load-json5'))
# loadf.add_command(click.command(json5_load, name='json5'))


if __name__ == '__main__':
    cli()
