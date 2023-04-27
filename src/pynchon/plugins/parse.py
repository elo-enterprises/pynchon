"""
"""
# @groop("gen", parent=entry)
# def gen():
#     """
#     Generate docs
#     """
# from pynchon import constants
# from pynchon.bin import groups
# from pynchon.util import lme
#
# from .entry import entry
# from .common import kommand, groop
#
# LOGGER = lme.get_logger(__name__)
#
#
# @groop("parse", parent=entry)
# def parse():
#     """
#     Helpers for parsing output from other tools
#     """
#
#
# @kommand(
#     name="pyright",
#     parent=parse,
#     formatters=dict(markdown=constants.T_TOC_CLI),
#     options=[
#         # options.file_setupcfg,
#         # options.format,
#         # options.stdout,
#         # options.output,
#         # options.header,
#     ],
# )
# def parse_pyright():
#     """
#     Parses pyright output into a markdown-based report card
#     """
#     LOGGER.debug("hello pyright")
