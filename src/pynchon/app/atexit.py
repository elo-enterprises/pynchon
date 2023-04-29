"""
"""
import sys
import atexit

from rich.text import Text
from rich.console import Console, Theme

from .events import events


class ExitHooks(object):
    """ """

    def __init__(self):
        self.exit_code = None
        self.exception = None

    def hook(self):
        self._orig_exit = sys.exit
        self._orig_exc_handler = self.exc_handler
        sys.exit = self.exit
        sys.excepthook = self.exc_handler

    def exit(self, code=0):
        self.exit_code = code
        self._orig_exit(code)

    def exc_handler(self, exc_type, exc, *args):
        self.exception = exc
        self._orig_exc_handler(self, exc_type, exc, *args)


def exit_handler():
    """ """
    if hooks.exit_code is not None and not hooks.exit_code == 0:
        events.status.update(stage=f"death by sys.exit({hooks.exit_code})")
    elif hooks.exception is not None:
        console = Console()
        text = Text(f"death by exception: {hooks.exception}")
        text.stylize('bold magenta', 0, 6)
        console.print(text)
        events.status.update(
            # color='bold_underline_bright_white_on_red',
            stage='❌'
        )
    else:
        # print("natural death")
        pass


hooks = ExitHooks()
hooks.hook()
atexit.register(exit_handler)
