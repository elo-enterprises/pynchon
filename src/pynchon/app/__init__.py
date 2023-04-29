""" pynchon.app
"""

import sys
import atexit

from rich.text import Text
from rich.console import Console, Theme
from memoized_property import memoized_property

import enlighten

from .events import events


class AppConsole(object):
    Text = Text
    Theme = Theme
    # docs = manager.term.link(
    #     'https://python-enlighten.readthedocs.io/en/stable/examples.html',
    #     'Read the Docs')
    # manager.status_bar(
    #     'footer-pynchon',
    #     position=1, fill='-',
    #     justify=enlighten.Justify.CENTER)

    # https://stackoverflow.com/questions/9741351/how-to-find-exit-code-or-reason-when-atexit-callback-is-called-in-python
    @memoized_property
    def status_bar(self):
        """ """
        tmp = self.manager.status_bar(
            status_format=u'{app}{fill}{stage}{fill}{elapsed}',
            color='bold_underline_bright_white_on_lightslategray',
            justify=enlighten.Justify.CENTER,
            app='Pynchon',
            stage='...',
            autorefresh=True,
            min_delta=0.1,
        )
        atexit.register(lambda: tmp.update(stage="\o/"))  # noqa: W605
        return tmp

    @memoized_property
    def manager(self):
        tmp = enlighten.get_manager()
        atexit.register(lambda: self.manager.stop())
        return tmp


class AppExitHooks(object):
    """ """

    def __init__(self, app=None):
        self.exit_code = None
        self.exception = None
        self.app = app

    # def uninstall(self):
    def install(self):
        self._orig_exit = sys.exit
        self._orig_exc_handler = self.exc_handler
        sys.exit = self.exit
        sys.excepthook = self.exc_handler
        atexit.register(self.exit_handler)

    def exit(self, code=0):
        self.exit_code = code
        self._orig_exit(code)

    def exc_handler(self, exc_type, exc, *args):
        self.exception = exc
        self._orig_exc_handler(self, exc_type, exc, *args)

    def exit_handler(self):
        """ """
        if self.exit_code is not None and not self.exit_code == 0:
            self.app.events.status.update(stage=f"death by sys.exit({self.exit_code})")

        elif self.exception is not None:
            text = f"death by exception: {self.exception}"
            text = self.app.Text(text)
            text.stylize('bold red', 0, 6)
            self.app.console.print(text)
            self.app.events.status.update(
                # color='bold_underline_bright_white_on_red',
                stage='❌'
            )
        else:
            # print("natural death")
            pass


class App(
    AppConsole,
):
    def __init__(self):
        self.exit_hooks = AppExitHooks(app=self)
        self.exit_hooks.install()
        self.console = Console()
        self.events = events
        events.status = self.status_bar
        # self.logger = ..


app = App()
