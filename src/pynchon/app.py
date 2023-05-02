""" pynchon.app
"""

import sys
import atexit

import enlighten
from rich.text import Text
from rich.console import Console, Theme
from memoized_property import memoized_property

from pynchon.util import lme

LOGGER = lme.get_logger(__name__)

import blinker


class Events:
    lifecycle = blinker.signal('lifecyle')
    bootstrap = blinker.signal('bootstrap')


events = Events()


class AppBase(object):
    pass


class AppConsole(AppBase):
    Text = Text
    Theme = Theme
    # docs = manager.term.link(
    #     'https://python-enlighten.readthedocs.io/en/stable/examples.html',
    #     'Read the Docs')

    def __init__(self, **kwargs):
        """ """
        self.console = Console()

    # # FIXME: use multi-dispatch over kwargs and define `lifecyle` repeatedly
    # def lifecycle_stage(self, sender, stage=None, **kwargs):
    #     """ """
    #     if stage:
    #         tmp = getattr(sender, '__name__', str(sender))
    #         # LOGGER.critical(f"STAGE ({tmp}): {stage}")
    #         self.status_bar.update(stage=stage)

    @memoized_property
    def status_bar(self):
        """ """
        tmp = self.manager.status_bar(
            status_format=u'{app}{fill}{stage}:{fill}{msg}{fill}{elapsed}',
            color='bold_underline_bright_white_on_lightslategray',
            justify=enlighten.Justify.LEFT,
            app='Pynchon',
            stage='...',
            msg='...',
            autorefresh=True,
            min_delta=0.1,
        )

        atexit.register(
            lambda: self.events.lifecycle.send(self, stage="\o/", msg='')
        )  # noqa: W605
        return tmp

    #
    # @memoized_property
    # def lifecycle_bar(self):
    #     """ """
    #     tmp = self.manager.status_bar(
    #         status_format=u'{fill}{msg}{fill}',
    #         color='bold_underline_bright_red_on_lightslategray',
    #         justify=enlighten.Justify.CENTER,
    #         msg='222',
    #         autorefresh=True,
    #         min_delta=0.1,
    #     )
    #
    #     atexit.register(
    #         lambda: self.events.lifecycle.send(self, msg="\o/")
    #     )  # noqa: W605
    #     return tmp

    @memoized_property
    def manager(self):
        tmp = enlighten.get_manager()
        atexit.register(lambda: self.manager.stop())
        return tmp


class AppExitHooks(AppBase):
    """ """

    # https://stackoverflow.com/questions/9741351/how-to-find-exit-code-or-reason-when-atexit-callback-is-called-in-python

    # def uninstall(self):
    def install_exit_hooks(self) -> None:
        self.events.lifecycle.send(self, msg='Installing exit handlers')
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

    def sys_exit_handler(self):
        if self.exit_code is not None and not self.exit_code == 0:
            tmp = f"death by sys.exit({self.exit_code})"
            self.events.lifecycle.send(self, stage=tmp)
            # status.update(stage=tmp)

    def exit_handler(self):
        """ """
        handled = self.sys_exit_handler()
        handled = handled or self.exc_exit_handler()
        handled = handled or self.def_exit_handler()
        return handled

    def exc_exit_handler(self):
        """ """
        if self.exception is not None:
            text = f"Exception: {self.exception}"
            text = self.Text(text)
            text.stylize('bold red', 0, 6)
            self.console.print(text)
            self.events.lifecycle.send(self, stage='❌')

    def def_exit_handler(self):
        """ """
        # LOGGER.info("ok")
        return True


class AppEvents(AppBase):
    def __init__(self, **kwargs):
        """ """
        self.events = events
        events.lifecycle.connect(self.lifecycle_msg)
        events.lifecycle.connect(self.lifecycle_stage)

    # FIXME: use multi-dispatch over kwargs and define `lifecyle` repeatedly
    def lifecycle_stage(self, sender, stage=None, **kwargs):
        """ """
        if stage:
            tmp = getattr(sender, '__name__', str(sender))
            # LOGGER.critical(f"STAGE ({tmp}): {stage}")
            self.status_bar.update(stage=stage)

    # FIXME: use multi-dispatch over kwargs and define `lifecyle` repeatedly
    def lifecycle_msg(self, sender, msg=None, **kwargs):
        """ """
        if msg:
            tmp = getattr(sender, 'name', getattr(sender, '__name__', str(sender)))
            LOGGER.critical(f"LIFECYCLE ({tmp}): {msg}")
            self.status_bar.update(msg=msg)


class App(AppConsole, AppEvents, AppExitHooks):
    def __init__(self, **kwargs):
        """ """
        AppConsole.__init__(self, **kwargs)
        AppEvents.__init__(self, **kwargs)
        self.exit_code = None
        self.exception = None
        self.install_exit_hooks()
        # self.logger = ..


app = App()
