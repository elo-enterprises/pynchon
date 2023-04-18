""" pynchon.util.config
"""
import configparser

from tomli import loads as toml_loads  # noqa
from tomli_w import dumps as toml_dumps  # noqa


def ini_loads(path):
    """ """
    parser = configparser.ConfigParser()
    parser.read(path)
    confdict = {section: dict(parser.items(section)) for section in parser.sections()}
    return confdict


# config = configparser.ConfigParser()
#     # parser.read(path)
#     # out = dict()
#     # # config.get('section_a', 'string_val')
#     # for sect in parser.sections():
#     #     out[sect] = dict(parser.items(sect))
#     # return out
#     dictionary = {}
#     for section in config.sections():
#         dictionary[section] = {}
#         for option in config.options(section):
#             dictionary[section][option] = config.get(section, option)
#     import IPython; IPython.embed()
#     return dictionary
