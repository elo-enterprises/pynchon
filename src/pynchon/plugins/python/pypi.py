""" pynchon.plugins.python.pypi
"""
from pynchon import abcs, models
from pynchon.util import typing, lme

LOGGER = lme.get_logger(__name__)


class PyPiConfig(abcs.Config):
    config_key = "pypi"
    defaults: typing.Dict = dict(
        name="Public PyPI",
        docs_url="https://pypi.org/",
        base_url="https://pypi.org/project",
    )


class PyPI(models.Provider):
    """Context for PyPI"""

    name = "pypi"
    config_class = PyPiConfig
