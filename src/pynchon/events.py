""" pynchon.events
"""
from blinker import signal

lifecycle = signal('lifecycle')
bootstrap = signal('bootstrap')
