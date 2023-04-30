"""
"""
import functools
import collections

EventType = collections.namedtuple('Event', 'type msg data')
LifeCycle = functools.partial(EventType, type='app-lifecycle')
ConfigFinalized = functools.partial(EventType, type='config-finalized')
PluginFinalized = functools.partial(EventType, type='plugin-finalized')


class Engine(object):
    """ """

    def push(self, **kwargs):
        event = EventType(**kwargs)
        raise NotImplementedError(event)

    def subscribe(self, fxn, type: str = None):
        """ """


DEFAULT_ENGINE = Engine()
push = DEFAULT_ENGINE.push
