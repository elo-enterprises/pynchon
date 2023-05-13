""" pynchon.util.text
    Utilities for parsing, generating or manipulating text
"""

import json

from . import loadf, loads  # noqa

# from . import dumpf, dumps # noqa

# from pynchon.util import typing, lme
# from pynchon.util.importing import module_builder
# module_builder(
#     __name__,
#     import_mods=['.loadf', '.loads',])


def to_json(obj, cls=None, indent: int = 2) -> str:
    """

    :param obj: param cls:  (Default value = JSONEncoder)
    :param indent: int:  (Default value = 2)
    :param cls:  (Default value = JSONEncoder)
    :param indent: int:  (Default value = 2)

    """
    from pynchon.abcs.path import JSONEncoder

    cls = cls or JSONEncoder

    return json.dumps(obj, indent=indent, cls=cls)


jsonify = to_json


def indent(txt: str, level: int = 2) -> str:
    """indents text, or if given an object, stringifies and then indents

    :param txt: str:
    :param level: int:  (Default value = 2)
    :param txt: str:
    :param level: int:  (Default value = 2)

    """
    import pprint

    if not isinstance(txt, (str, bytes)):
        txt = pprint.pformat(txt)
    return "\n".join([(" " * level) + line for line in txt.split("\n") if line.strip()])
