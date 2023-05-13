""" pynchon.events
"""
import blinker  # noqa
from blinker import signal  # noqa

from pynchon.util import lme

LOGGER = lme.get_logger(__name__)
lifecycle = blinker.signal("lifecyle")
bootstrap = blinker.signal("bootstrap")


# FIXME: use multi-dispatch over kwargs and define `lifecyle` repeatedly
def lifecycle_plugin(sender, plugin):
    """
    :param sender:
    :param plugin:
    """
    if plugin:
        tmp = getattr(sender, "__name__", getattr(sender, "name", str(sender)))
        tmp = f"{tmp}: PLUGIN: {plugin}"
        lifecycle.send(sender, msg=plugin)


def lifecycle_config(sender, config):
    """

    :param sender:
    :param config:

    """
    if config:
        tmp = getattr(sender, "__name__", getattr(sender, "name", str(sender)))
        tmp = f"{tmp}: CONFIG: {config}"
        lifecycle.send(sender, msg=config)


def lifecycle_applying(sender, applying=None, **kwargs):
    """ """
    if applying:
        tmp = getattr(sender, "__name__", getattr(sender, "name", str(sender)))
        tmp = f"{tmp}: APPLY: {applying}"
        lifecycle.send(lifecycle_applying, stage=tmp)


def lifecycle_stage(sender, stage=None, **unused):
    """
    :param sender:
    :param stage:  (Default value = None)
    """
    if stage:
        tmp = getattr(sender, "__name__", str(sender))
        from pynchon.app import app

        app.status_bar.update(stage=stage)


def lifecycle_msg(sender, msg=None, **unused):
    """
    :param sender: param msg:  (Default value = None)
    :param msg:  (Default value = None)
    """
    if msg:
        tmp = getattr(sender, "name", getattr(sender, "__name__", str(sender)))
        LOGGER.info(f"lifecycle :{tmp}: {msg}")


def _lifecycle(sender, **signals):
    """ """
    from pynchon import events as THIS

    for k in signals:
        dispatch = getattr(THIS, f"lifecycle_{k}", None)
        assert dispatch
        dispatch(sender, **signals)


lifecycle.connect(_lifecycle)
