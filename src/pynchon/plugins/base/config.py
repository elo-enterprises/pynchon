""" pynchon.config.base
"""
import os

from pynchon import __version__, abcs
from pynchon.util import lme, typing
from pynchon.config import initialized

LOGGER = lme.get_logger(__name__)


class BaseConfig(abcs.Config):
    """ """

    priority = 1
    config_key = "pynchon"
    defaults = dict(
        version=__version__,
        plugins=[
            "git",
            "jinja",
            "project",
            "scaffolding",
            'python',
        ],
    )

    def validate(self, k, v):
        if not isinstance(k, str) or (isinstance(k, str) and '{{' in k):
            raise ValueError(f"Top-level keys should be simple strings! {k}")
        if isinstance(v, str) and '{{' in v:
            raise ValueError(f"No templating in top level! {v}")

        raw_plugin_configs = {}
        if k == 'plugins':
            LOGGER.warning('skipping plugin validation..')
        elif isinstance(v, (dict,)):
            raw_plugin_configs[k] = v
            # from pynchon.plugins import registry
            # if k in 'plugins globals'.split():
            #     continue
            # if k not in registry:
            #     err = f'top level keys with complex values should correspond to plugins! {k}'
            #     raise ValueError(err)
        else:
            LOGGER.info(f'skipping validation for top-level {k},{v}')

    def __init__(self, **core_config):
        LOGGER.debug('validating..')
        for k, v in core_config.items():
            self.validate(k, v)
        super(BaseConfig, self).__init__(**core_config)

    @property
    def root(self) -> str:
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
    def plugins(self):
        return sorted(
            list(set(self.get('plugins', []) + self.__class__.defaults['plugins']))
        )

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
