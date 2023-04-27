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


def snake_case(name: str) -> str:
    """ """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def indent(txt: str, level: int = 2) -> str:
    """
    indents text, or if given an object, stringifies and then indents
    """
    if not isinstance(txt, (str, bytes)):
        txt = _pprint.pformat(txt)
    return '\n'.join([(' ' * level) + line for line in txt.split('\n') if line.strip()])


DEFAULT_NORMALIZATION_RULES = {' ': '_', '/': '_', '-': '_'}


def normalize(
    txt: str = "",
    post: typing.List[typing.Callable] = [
        lambda _: _.lower(),
        lambda _: re.sub('_+', '_', _),
    ],
    rules: typing.List[typing.Callable] = DEFAULT_NORMALIZATION_RULES,
) -> str:
    """
    normalizes input text, with support for parametric rules/post-processing
    """
    tmp = txt
    for k, v in rules.items():
        tmp = tmp.replace(k, v)
    for fxn in post:
        tmp = fxn(tmp)
    return tmp
