""" pynchon.config.base
"""
import os

from pynchon import __version__, abcs
from pynchon.util import lme, python, typing

LOGGER = lme.get_logger(__name__)
import pyjson5

from . import initialized


class BaseConfig(abcs.Config):
    """ """
    priority = 1
    config_key = "pynchon"
    defaults = dict(
        version=__version__,
        plugins=[
            # "git",
            # "jinja",
            # "scaffolding",
            # "dot",
            # "fixme",
            # "python-cli",
            # "python-api",
        ],
    )
    # override_from_base = False  # this is the base :)


    # def __init__(self, **kwargs):
    #     """ " """
    #     super(BaseConfig, self).__init__(**kwargs)
    #
    #     # for k, v in os.environ.items():
    #     #     if k.startswith("PYNCHON_"):
    #     #         var = k[len("PYNCHON_"):].lower()
    #     #         val = os.environ[k]
    #     #         if "," in val:
    #     #             val = val.split(",")
    #     #         LOGGER.debug(f"found {k}; assigning pynchon[{var}] = {val}")
    #     #         self[var] = val

    @property
    def root(self):
        """
        pynchon root:
            * user-config
            * os-env
            * {{git.root}}
        """
        root = self.get("root")
        root = root or os.environ.get("PYNCHON_ROOT")
        root = root or initialized["git"].get("root")
        return root and abcs.Path(root)

    @property
    def docs_root(self) -> typing.StringMaybe:
        """
        where documents go by default
            * user-config
            * {{pynchon.root}}/docs
        """
        result = self.get("docs_root")
        result = result or (self.root and self.root / "docs")
        return result

    @property
    def working_dir(self):
        """
        working dir at the time of CLI invocation
        """
        return abcs.Path(".").absolute()
