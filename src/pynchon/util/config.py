""" pynchon.util.config
"""
import configparser

from tomli import loads as toml_loads  # noqa
from tomli_w import dumps as toml_dumps  # noqa


def ini_loads(path):
    """ """
    parser = configparser.ConfigParser()
    parser.read(path)
    out = dict()
    for sect in parser.sections():
        out[sect] = dict(parser.items(sect))
    return out
