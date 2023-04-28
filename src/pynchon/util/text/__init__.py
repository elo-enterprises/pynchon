""" pynchon.util.text
    Utilities for parsing, generating or manipulating text
"""

import os
import re
import json
import pprint as _pprint

import json5

from pynchon.util import typing, lme

LOGGER = lme.get_logger(__name__)


def to_json(obj):
    """ """
    from pynchon import abcs

    return json.dumps(obj, indent=2, cls=abcs.JSONEncoder)


jsonify = to_json


def load_json(file: str = '', content: str = '') -> dict:
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
        data = json.loads(content)
        # data = pyjson5.loads(content)
    # except (pyjson5.Json5EOF,) as exc:
    except (ValueError,) as exc:
        LOGGER.critical(f"Cannot parse json from {file}!")
        raise
    return data


def load_json5(file: str = '', content: str = '') -> dict:
    """
    loads json5 to python dictionary from given file or string
    """
    if file:
        assert not content
        if not os.path.exists(file):
            raise ValueError(f'file @ {file} is missing!')
        with open(file, 'r') as fhandle:
            content = fhandle.read()
    try:
        data = json5.loads(content)
    # except (pyjson5.Json5EOF,) as exc:
    except (ValueError,) as exc:
        LOGGER.critical(f"Cannot parse json5 from {file or 'content'}!")
        content_lines = content.split('\n')
        if 'at column' in exc.args[0]:
            line_no = exc.args[0].split()[0].split(':')[-1]
            line_no = int(line_no)
            err_lines = '\n'.join(content_lines[line_no - 3 : line_no + 3])
        else:
            err_lines = None
            line_no = None
        LOGGER.warning(f"error: {exc}")
        err_lines and LOGGER.warning(f"lines nearby:\n\n {err_lines}")
        raise
    return data

def json5_loadc(
    output: str = '',
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
        obj = text.loadf_json5(file=file)
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
            push = text.loads_json5(content=push_json_data)
        elif push_file_data:
            err = f'file@{push_file_data} doesnt exist'
            assert os.path.exists(push_file_data), err
            with open(push_file_data, 'r') as fhandle:
                push = fhandle.read()
        out[under_key] = push

    if wrapper_key:
        # NB: must remain after push
        out = {wrapper_key: out}

    return out

def indent(txt: str, level: int = 2) -> str:
    """
    indents text, or if given an object, stringifies and then indents
    """
    if not isinstance(txt, (str, bytes)):
        txt = _pprint.pformat(txt)
    return '\n'.join([(' ' * level) + line for line in txt.split('\n') if line.strip()])
