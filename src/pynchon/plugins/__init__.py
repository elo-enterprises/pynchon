""" pynchon.plugins
"""
from pynchon.abcs.plugin import Plugin
from pynchon.config.jinja import JinjaConfig
from pynchon.config.scaffold import ScaffoldConfig


class JinjaPlugin(Plugin):
    config = JinjaConfig


class Scaffolding(Plugin):
    config = ScaffoldConfig
