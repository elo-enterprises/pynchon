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

    @property
    def config_folder(self):
        return abcs.Path(os.environ.get("PYNCHON_ROOT", initialized["git"]["root"]))

    def __init__(self, **kwargs):
        """ " """
        super(BaseConfig, self).__init__(**kwargs)

        def load_config():
            """ """
            contents = {}
            if self.config_source:
                if self.config_source.name.endswith('.toml'):
                    LOGGER.debug(f"Loading from toml: {self.config_source}")
                    contents = python.load_pyprojecttoml(path=toml_path)
                    contents = contents.get("tool", {}).get("pynchon", {})

                elif self.config_source.name.endswith('.json5'):
                    LOGGER.debug(f"Loading from json5: {self.config_source}")
                    import pyjson5

                    with open(self.config_source.absolute(), "r") as fhandle:
                        contents = pyjson5.loads(fhandle.read())
            return contents

        toml_path = self.config_folder / "pyproject.toml"
        json5_path = self.config_folder / "pynchon.json5"
        json5_path_hidden = self.config_folder / ".pynchon.json5"
        contents = {**load_config(), **dict(config_source=self.config_source)}

        if contents:
            for k, v in contents.items():
                self[k] = v
        else:
            LOGGER.critical("could not load any configuration!")
        # for k, v in os.environ.items():
        #     if k.startswith("PYNCHON_"):
        #         var = k[len("PYNCHON_"):].lower()
        #         val = os.environ[k]
        #         if "," in val:
        #             val = val.split(",")
        #         LOGGER.debug(f"found {k}; assigning pynchon[{var}] = {val}")
        #         self[var] = val

    @property
    def config_source(self):
        """ """
        if os.environ.get('PYNCHON_CONFIG', None):
            return abcs.Path(os.environ['PYNCHON_CONFIG'])
        toml_path = self.config_folder / "pyproject.toml"
        json5_path = self.config_folder / "pynchon.json5"
        json5_path_hidden = self.config_folder / ".pynchon.json5"
        if json5_path.exists():
            return json5_path
        if json5_path_hidden.exists():
            return json5_path_hidden
        if toml_path.exists():
            return toml_path

    @property
    def root(self):
        """ """
        return abcs.Path(
            self.get("root", os.environ.get("PYNCHON_ROOT", initialized["git"]["root"]))
        )

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
