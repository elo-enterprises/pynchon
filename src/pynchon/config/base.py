""" pynchon.config.base
"""
import os

from pynchon import __version__, abcs
from pynchon.util import lme, python, typing

LOGGER = lme.get_logger(__name__)
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

    def __init__(self, **kwargs):
        """ " """
        super(BaseConfig, self).__init__(**kwargs)
        file, config = python.load_pyprojecttoml(
            path=abcs.Path(os.environ.get("PYNCHON_ROOT", initialized["git"]["root"]))
        )
        config = config.get("tool", {}).get("pynchon", {})
        if config:
            for k, v in config.items():
                self[k] = v
            self["config_source"] = file.absolute()
        else:
            LOGGER.warning("could not load pyproject.toml")
        # for k, v in os.environ.items():
        #     if k.startswith("PYNCHON_"):
        #         var = k[len("PYNCHON_"):].lower()
        #         val = os.environ[k]
        #         if "," in val:
        #             val = val.split(",")
        #         LOGGER.debug(f"found {k}; assigning pynchon[{var}] = {val}")
        #         self[var] = val

    @property
    def root(self):
        """ """
        return abcs.Path(self.get("root", os.environ.get("PYNCHON_ROOT")))

    @property
    def docs_root(self) -> typing.StringMaybe:
        """ """
        result = self.get("docs_root")
        if result:
            return result
        root = self.root or initialized["git"]["root"]
        return root / "docs"

    @property
    def working_dir(self):
        """ """
        return abcs.Path(".").absolute()
