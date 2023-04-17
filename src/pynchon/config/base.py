""" pynchon.config.base
"""
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
            "git",
            "jinja",
            "scaffold",
            "dot",
        ],
    )
    override_from_base = False

    def __init__(self, **kwargs):
        """ " """
        super(BaseConfig, self).__init__(**kwargs)
        file, config = python.load_pyprojecttoml(path=initialized["git"]["root"])
        config = config.get("tool", {}).get("pynchon", {})
        if config:
            for k, v in config.items():
                self[k] = v
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

    # @property
    # def src_root(self):
    #     return self.get(
    #         "src_root",
    #         git['root'])
    #
    @property
    def docs_root(self) -> typing.StringMaybe:
        """ """
        result = self.get("docs_root")
        if result:
            return result
        git = initialized["git"]
        if git["root"].joinpath("docs"):
            return git["root"].joinpath("docs")
        # git_root.joinpath('docs')
        # if 'docs_root' in self: # set in pyproject.toml
        #     return abcs.Path(self["docs_root"]).relative_to(pynchon['config_key'])
        # else:
        #     tmp = abcs.Path(self.working_dir.joinpath("docs"))
        #     if tmp.exists():
        #         return abcs.Path(tmp)

    @property
    def working_dir(self):
        """ """
        return abcs.Path(".").absolute()
