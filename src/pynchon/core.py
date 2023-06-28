""" pynchon.core
"""
import os

from pynchon import __version__, abcs, constants
from pynchon.util import lme, tagging, typing

LOGGER = lme.get_logger(__name__)

count = 0


def validate(kls=None, self=None, vdata=None):
    """
    :param vdata=None:
    :param self=None:
    :param kls=None:
    """
    global count
    count += 1
    if count > 1:
        raise Exception()

    def validate_plugins(plugin_list: typing.List = []):
        """

        :param plugin_list: typing.List:  (Default value = [])
        :param plugin_list: typing.List:  (Default value = [])

        """
        defaults = set(constants.DEFAULT_PLUGINS)
        user_provided = set(plugin_list)
        intersection = defaults.intersection(user_provided)
        diff = defaults - intersection
        if diff:
            msg = "implied plugins are not mentioned explicitly!"
            vdata.warnings[msg].append(diff)

    def validate_config(k, v):
        if not isinstance(k, str) or (isinstance(k, str) and "{{" in k):
            raise ValueError(f"Top-level keys should be simple strings! {k}")
        if isinstance(v, str) and "{{" in v:
            raise ValueError(f"No templating in top level! {v}")
        raw_plugin_configs = {}
        if k == "plugins":
            validate_plugins(v)
        elif isinstance(v, (dict,)):
            raw_plugin_configs[k] = v
        else:
            # LOGGER.info(f'skipping validation for top-level `{k}` @ {v}')
            pass

    for k, v in dict(self).items():
        validate_config(k, v)
DEFAULT_PLUGINS = list(set(constants.DEFAULT_PLUGINS))

class Config(abcs.Config):
    """ """
    priority: typing.ClassVar[int] = 1
    config_key: typing.ClassVar[str] = "pynchon"
    class Config:
        # fields = {
        #     '_root': 'root',
        # }
        arbitrary_types_allowed = True
        #https://github.com/pydantic/pydantic/discussions/5159
        frozen = True

    # defaults = dict(
    #     version=__version__,
    #     # plugins=DEFAULT_PLUGINS,
    # )
    __class_validators__ = []
    __instance_validators__ = [
        validate,
    ]

    def __init__(self, **core_config):
        if not core_config:
            LOGGER.critical("core config is empty!")
        super().__init__(**core_config)

    @property
    def root(self) -> str:
        """{pynchon.root}:
        * user-config
        * os-env
        * {{git.root}}
        """
        from pynchon import config
        root = self.__dict__.get('_root')
        root = root or os.environ.get("PYNCHON_ROOT")
        root = root or config.GIT.get("root")
        root = root or self.working_dir
        return root and abcs.Path(root)

    @tagging.tagged_property(conflict_strategy="override")
    def plugins(self):
        """{pynchon.plugins}:
        value here ultimately determines much of the
        rest of the apps bootstrap/runtime. value is
        always decided here, and must merge user-input
        from config files, plus any overrides on cli,
        plus pynchon's core set of default plugins.
        """
        defaults = DEFAULT_PLUGINS
        return defaults
        # result = sorted(list(set(self["plugins"] + defaults)))
        # self["plugins"] = result
        # return result

    @property
    def working_dir(self):
        """working dir at the time of CLI invocation"""
        return abcs.Path(".").absolute()
