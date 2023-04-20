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
            import pyjson5

            contents = []
            for src in self.config_source:
                if src.name.endswith('.toml'):
                    LOGGER.debug(f"Loading from toml: {src}")
                    tmp = python.load_pyprojecttoml(path=src)
                    tmp = tmp.get("tool", {}).get("pynchon", {})
                    contents.append(tmp)
                elif src.name.endswith('.json5'):
                    LOGGER.debug(f"Loading from json5: {src}")
                    with open(src.absolute(), "r") as fhandle:
                        contents.append(pyjson5.loads(fhandle.read()))

            return contents

        # toml_path = self.config_folder / "pyproject.toml"
        # json5_path = self.config_folder / "pynchon.json5"
        # json5_path_hidden = self.config_folder / ".pynchon.json5"
        contents = {}
        for conf in load_config():
            contents.update(conf)
        contents.update(dict(config_source=self.config_source))

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
        config_candidates = [
            self.config_folder / "pynchon.json5",
            self.config_folder / ".pynchon.json5",
            self.config_folder / "pyproject.toml",
        ]
        subproject = initialized['project']['subproject']
        subproject_root = subproject and subproject['root']
        if subproject_root:
            config_candidates += [
                subproject_root / "pynchon.json5",
                subproject_root / ".pynchon.json5",
                subproject_root / "pyproject.toml",
            ]
        config_candidates = [p for p in config_candidates if p.exists()]
        return config_candidates

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
