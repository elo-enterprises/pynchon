""" pynchon.models.plugins.pynchon """
import collections

from pynchon.plugins import util as plugins_util

from . import validators

from pynchon import api, cli, events, fleks, shimport  # noqa
from pynchon.util import lme, tagging, typing  # noqa


LOGGER = lme.get_logger(__name__)
classproperty = typing.classproperty
pydash = shimport.lazy("pydash")
config_mod = shimport.lazy("pynchon.config")


@tagging.tags(cli_label="<<Abstract>>")
class PynchonPlugin(fleks.Plugin):
    """Pynchon-specific plugin-functionality"""

    name = "<<Abstract>>"
    cli_label = "<<Abstract>>"
    config_class = None
    __class_validators__ = [
        validators.require_conf_key,
        validators.warn_config_kls,
    ]

    @classproperty
    def siblings(kls):
        """ """
        result = []
        from pynchon.plugins import registry

        for plugin in registry.keys():
            if plugin == kls.name:
                continue
            result.append(plugins_util.get_plugin_obj(plugin))
        result = sorted(result, key=lambda p: p.priority)

        class Siblings(collections.OrderedDict):
            def collect_config_list(self, key):
                """collects the named key across all sibling-plugins"""
                out = []
                for name, plugin_obj in self.items():
                    out += plugin_obj[key::[]]
                return out

            def collect_config_dict(self, key):
                """collects the named key across all sibling-plugins"""
                out = {}
                for name, plugin_obj in self.items():
                    out.update(plugin_obj[key::{}])
                return out

        return Siblings([p.name, p] for p in result)

    @typing.classproperty
    def instance(kls):
        """class-property: the instance for this plugin"""
        return plugins_util.get_plugin_obj(kls.name)

    @classproperty
    def plugin_templates_prefix(kls):
        return f"pynchon/plugins/{kls.name}"

    @typing.classproperty
    def project_config(self):
        """class-property: finalized project-config"""
        return api.project.get_config()

    @classmethod
    def get_config_key(kls):
        default = kls.name.replace("-", "_")
        config_kls = getattr(kls, "config_class", None)
        return getattr(config_kls, "config_key", default) or default

    @classmethod
    def get_current_config(kls):
        """get the current config for this plugin"""
        conf_class = getattr(kls, "config_class", None)
        if conf_class is None:
            return {}
        conf_key = kls.get_config_key()
        result = getattr(config_mod, conf_key)
        return result

    @property
    def plugin_config(self):
        """ """
        return self.get_current_config()

    @property
    def config(self):
        """ """
        return self.cfg()

    def cfg(self):
        """Shows current config for this plugin"""
        kls = self.__class__
        conf_class = getattr(kls, "config_class", None)
        conf_class_name = conf_class.__name__ if conf_class else "(None)"
        LOGGER.debug(f"config class: {conf_class_name}")
        LOGGER.debug("current config:")
        result = kls.get_current_config()
        return result

    def __getitem__(self, key: str):
        """shortcut for accessing local plugin-config

        :param key: str:
        """
        if isinstance(key, (slice,)):
            start, stop, step = key.start, key.stop, key.step
            try:
                if start:
                    result = self[start]
                if stop:
                    result = self % stop
            except (KeyError,) as exc:
                if step is not None:
                    return step
                else:
                    raise
            else:
                return result
        else:
            try:
                return self.config[key]
            except (KeyError,) as exc:
                fallback = pydash.get(self.config, key)
                if fallback:
                    return fallback
                else:
                    raise

    def __floordiv__(self, key: str, strict=False):
        """

        :param key: str:
        :param strict: Default value = False)
        """
        # return self.__mod__(key, strict=strict)
        from pynchon import api

        assert key
        key = key[1:] if key.startswith("/") else key
        return api.render.get_template(f"{self.plugin_templates_prefix}/{key}")

    def __mod__(self, key: str, strict=True):
        """shortcut for accessing global pynchon-config

        :param key: str:
        :param strict: Default value = True)

        """
        try:
            return self.project_config[key]
        except (KeyError,) as exc:
            fallback = pydash.get(self.project_config, key, None)
            if fallback:
                return fallback
            else:
                if strict:
                    raise