""" pynchon.plugins.python.pypi
"""
from pynchon import abcs, models
from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class PyPiConfig(abcs.Config):
    config_key: typing.ClassVar[str] =  "pypi"
    name:str = abcs.Field(default="Public PyPI")
    docs_url:str = abcs.Field(default="https://pypi.org/")
    base_url:str = abcs.Field(default="https://pypi.org/project")


class PyPI(models.Provider):
    """Context for PyPI"""

    name = "pypi"
    config_class = PyPiConfig
