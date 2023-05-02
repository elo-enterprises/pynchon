""" pynchon.util.text.loads

    Helpers for loading data structures from strings
"""
import json as json_mod

import pyjson5 as json5_mod

from pynchon.util import typing, lme

LOGGER = lme.get_logger(__name__)


def ini(content: str) -> typing.StringMaybe:
    """
    Parses `content` as ini-file.
    """
    raise NotImplementedError()


def yaml(content: str) -> typing.StringMaybe:
    """
    Parses `content` as yaml.
    """
    raise NotImplementedError()


def toml(content: str) -> typing.StringMaybe:
    """
    Parses `content` as toml.
    """
    raise NotImplementedError()


def json(content: str = '') -> typing.StringMaybe:
    """
    Parses `content` as JSON (strict).
    For most things, you're better using `loads.json5()`,
    since that's just a JSON superset with a more relaxed parser.
    """
    return json_mod.loads(content)


def json5(content: str = '', quiet=True) -> typing.StringMaybe:
    """
    Parses `content` as JSON5.
    This tries to give a better error message than defaults.
    """
    try:
        return json5_mod.loads(content)
    except (ValueError,) as exc:
        LOGGER.critical("Cannot parse json5!")
        quiet or LOGGER.critical(content)
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
