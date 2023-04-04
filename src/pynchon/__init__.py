""" pynchon
"""
import importlib
import inspect
import logging
import os
import sys

import click
import jinja2

# NB: this should have been set by CI immediately
# before pypi-upload.  but the `except` below might
# be triggered by local development.
try:
    from ._version import __version__
except ImportError:
    __version__ = "0.0.0+local"
