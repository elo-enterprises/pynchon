""" pynchon.core
"""
import os

from pynchon import __version__, abcs
from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)

from pynchon import constants
from pynchon.util import tagging


class Config(abcs.Config):
    """ """

    priority = 1
    config_key = "pynchon"
    defaults = dict(
        version=__version__,
        src_root=abcs.Path("."),
        plugins=list(set(constants.DEFAULT_PLUGINS)),
    )

    def validate_plugins(self, plugin_list: typing.List = []):
        """ """
        # LOGGER.warning('skipping plugin validation..')
        defaults = set(constants.DEFAULT_PLUGINS)
        user_provided = set(plugin_list)
        intersection = defaults.intersection(user_provided)
        diff = defaults - intersection
        if diff:
            msg = "implied plugins are not mentioned explicitly"
            self.logger.warning(f"{msg}:\n  {diff}")

    def validate(self, k, v):
        if not isinstance(k, str) or (isinstance(k, str) and '{{' in k):
            raise ValueError(f"Top-level keys should be simple strings! {k}")
        if isinstance(v, str) and '{{' in v:
            raise ValueError(f"No templating in top level! {v}")
        raw_plugin_configs = {}
        if k == 'plugins':
            self.validate_plugins(v)
        elif isinstance(v, (dict,)):
            raw_plugin_configs[k] = v
        else:
            # LOGGER.info(f'skipping validation for top-level `{k}` @ {v}')
            pass

    def __init__(self, **core_config):
        if not core_config:
            self.logger.critical("core config is empty!")
        self.logger.debug('Validating..')
        for k, v in core_config.items():
            self.validate(k, v)
        super(Config, self).__init__(**core_config)

    @property
    def root(self) -> str:
        """
        pynchon root:
            * user-config
            * os-env
            * {{git.root}}
        """
        from pynchon import config

        root = self.get("root")
        root = root or os.environ.get("PYNCHON_ROOT")
        root = root or config.GIT.get("root")
        return root and abcs.Path(root)

    @tagging.tags(conflict_strategy='override')
    @property
    def plugins(self):
        result = sorted(
            list(set(self.get('plugins', []) + self.__class__.defaults['plugins']))
        )
        self['plugins'] = result
        return result

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
