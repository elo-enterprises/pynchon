""" pynchon.events
"""
import blinker
from blinker import signal

lifecycle = blinker.signal('lifecyle')
bootstrap = blinker.signal('bootstrap')
