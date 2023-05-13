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

    :param sender: param plugin:
    :param plugin:

    """
    if plugin:
        tmp = getattr(sender, "__name__", str(sender))
        tmp = f"{tmp}: PLUGIN: {plugin}"
        lifecycle.send(sender, msg=plugin)


def lifecycle_config(sender, config):
    """

    :param sender: param config:
    :param config:

    """
    if config:
        tmp = getattr(sender, "__name__", str(sender))
        tmp = f"{tmp}: CONFIG: {config}"
        lifecycle.send(sender, msg=config)


def lifecycle_applying(sender, applying=None, **kwargs):
    """

    :param sender: param applying:  (Default value = None)
    :param applying:  (Default value = None)
    :param **kwargs:

    """
    if applying:
        tmp = getattr(sender, "__name__", str(sender))
        tmp = f"{tmp}: APPLY: {applying}"
        lifecycle.send(lifecycle_applying, stage=tmp)


def lifecycle_stage(sender, stage=None, **kwargs):
    """

    :param sender: param stage:  (Default value = None)
    :param stage:  (Default value = None)
    :param **kwargs:

    """
    if stage:
        tmp = getattr(sender, "__name__", str(sender))
        from pynchon.app import app

        app.status_bar.update(stage=stage)


def lifecycle_msg(sender, msg=None, **kwargs):
    """

    :param sender: param msg:  (Default value = None)
    :param msg:  (Default value = None)
    :param **kwargs:

    """
    if msg:
        tmp = getattr(sender, "name", getattr(sender, "__name__", str(sender)))
        LOGGER.info(f"lifecycle :{tmp}: {msg}")


def _lifecycle(sender, **kwargs):
    from pynchon import events as THIS

    for k in kwargs:
        dispatch = getattr(THIS, f"lifecycle_{k}", None)
        assert dispatch
        dispatch(sender, **kwargs)


lifecycle.connect(_lifecycle)
# events.lifecycle.connect(self.lifecycle_stage)
# events.lifecycle.connect(self.lifecycle_applying)
# events.lifecycle.connect(self.lifecycle_plugin)
