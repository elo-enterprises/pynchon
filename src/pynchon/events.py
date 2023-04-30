""" pynchon.events
"""
from blinker import signal

lifecycle = signal('lifecycle')
bootstrap = signal('bootstrap')

# https://mcfletch.github.io/pydispatcher/
    # from pydispatch import dispatcher
    #
    # metaKey = "moo"
    # MyNode = object()
    # event = {"sample": "event"}
    #
    # def callback(event=None):
    #     """Handle signal being sent"""
    #     print("Signal received", event)
    # dispatcher.connect(callback, sender=MyNode, signal=metaKey)
    # dispatcher.send(metaKey, MyNode, event=event)
# https://pypi.org/project/pymitter/
    # from pymitter import EventEmitter
    # ee = EventEmitter()
    #
    # # decorator usage
    # @ee.on("my_event")
    # def handler1(arg):
    #     print("handler1 called with", arg)
    #
    # # callback usage
    # def handler2(arg):
    #     print("handler2 called with", arg)
    #
    # ee.on("my_other_event", handler2)
    #
    # ee.emit("my_event", "foo")
    # # -> "handler1 called with foo"
    #
    # ee.emit("my_other_event", "bar")
    # # -> "handler2 called with bar"
    #
    # ee.emit("my_third_event", "baz")
    # # -> "handler3 called with baz"

# https://pypi.org/project/pluggy/
    # import pluggy
    #
    # hookspec = pluggy.HookspecMarker("myproject")
    # hookimpl = pluggy.HookimplMarker("myproject")
    #
    # class MySpec:
    #     """A hook specification namespace."""
    #     @hookspec
    #     def myhook(self, arg1, arg2):
    #         """My special little hook that you can customize."""
    #
    # class Plugin_1:
    #     """A hook implementation namespace."""
    #
    #     @hookimpl
    #     def myhook(self, arg1, arg2):
    #         print("inside Plugin_1.myhook()")
    #         return arg1 + arg2
    #
    # class Plugin_2:
    #     """A 2nd hook implementation namespace."""
    #
    #     @hookimpl
    #     def myhook(self, arg1, arg2):
    #         print("inside Plugin_2.myhook()")
    #         return arg1 - arg2
    #
    # # create a manager and add the spec
    # pm = pluggy.PluginManager("myproject")
    # pm.add_hookspecs(MySpec)
    #
    # # register plugins
    # pm.register(Plugin_1())
    # pm.register(Plugin_2())
    #
    # # call our ``myhook`` hook
    # results = pm.hook.myhook(arg1=1, arg2=2)
    # print(results)
# https://pypi.org/project/blinker/
    # >>> from blinker import signal
    # >>> started = signal('round-started')
    # >>> def each(round):
    # ...     print(f"Round {round}")
    # >>> started.connect(each)
    # >>> def round_two(round):
    # ...     print("This is round two.")
    # >>> started.connect(round_two, sender=2)
    # >>> for round in range(1, 4):
    # ...     started.send(round)
    # Round 1!
    # Round 2!
    # This is round two.
    # Round 3!
