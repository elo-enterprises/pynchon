""" pynchon.util.text
    Utilities for parsing, generating or manipulating text
"""

import json

from pynchon.abcs import JSONEncoder

from . import loadf, loads  # noqa

# from . import dumpf, dumps # noqa

# from pynchon.util import typing, lme
# from pynchon.util.importing import module_builder
# module_builder(
#     __name__,
#     import_mods=['.loadf', '.loads',])


def to_json(obj, cls=JSONEncoder, indent: int = 2) -> str:
    """ """
    return json.dumps(obj, indent=indent, cls=cls)


jsonify = to_json


def indent(txt: str, level: int = 2) -> str:
    """
    indents text, or if given an object, stringifies and then indents
    """
    import pprint

    if not isinstance(txt, (str, bytes)):
        txt = pprint.pformat(txt)
    return '\n'.join([(' ' * level) + line for line in txt.split('\n') if line.strip()])
