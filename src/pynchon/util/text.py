""" pynchon.util.text
"""

import json


def to_json(obj):
    """ """
    from pynchon import abcs

    return json.dumps(obj, indent=2, cls=abcs.JSONEncoder)
