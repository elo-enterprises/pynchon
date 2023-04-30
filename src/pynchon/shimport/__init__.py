""" {{pkg}}.util.importing
"""
from importlib import import_module

from . import module as mod_module
from .module import *

module = mod_module.wrapper
lazy = lazy_import
registry =registry_builder
