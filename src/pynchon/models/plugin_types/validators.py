""" pynchon.models.validators

    FIXME: ntuple struct for vdata
"""
import collections

from pynchon import fleks

from pynchon.util import typing, lme  # noqa

LOGGER = lme.get_logger(__name__)


def require_conf_key(kls, strict=True, **vdata):
    """ """
    pconf_kls = getattr(kls, 'config_class', None)
    conf_key = getattr(pconf_kls, 'config_key', kls.name.replace('-', '_'))
    if not conf_key:
        msg = f'failed to determine conf-key for {kls}'
        LOGGER.critical(msg)
        if strict:
            raise fleks.meta.ClassMalformed(msg)
    return vdata


def warn_config_kls(kls, warnings=collections.defaultdict(list), **vdata):
    pconf_kls = getattr(kls, 'config_class', None)
    if pconf_kls is None:
        warnings["`config_kls` not set!"].append(kls)
    vdata.update(warnings=warnings)
    return vdata
