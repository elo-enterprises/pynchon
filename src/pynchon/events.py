""" pynchon.events
"""
import blinker  # noqa
from blinker import signal  # noqa

lifecycle = blinker.signal('lifecyle')
bootstrap = blinker.signal('bootstrap')
