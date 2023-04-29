""" pynchon.app
"""
import enlighten
from rich.text import Text
from rich.console import Console, Theme
from memoized_property import memoized_property
from .events import events
from .atexit import ExitHooks
# from .console import manager, status

class App():
    Text = Text
    Theme=Theme

    @memoized_property
    def status_bar(self):
        """
        """
        return self.manager.status_bar(
            status_format=u'{app}{fill}{stage}{fill}{elapsed}',
            color='bold_underline_bright_white_on_lightslategray',
            justify=enlighten.Justify.CENTER,
            app='Pynchon',
            stage='...',
            autorefresh=True,
            min_delta=0.1,
        )

    @memoized_property
    def manager(self):
        return enlighten.get_manager()

    def __init__(self):
        self.events = events
        events.status = self.status_bar
        # self.logger = ..
        self.exit_hooks = ExitHooks(app=self)
        self.exit_hooks.install()
        self.console=Console()
        # self.init_status_bar()
        import atexit
        atexit.register(lambda: [self.status_bar.update(stage="\o/"), self.manager.stop()])  # noqa: W605

    def init_status_bar(self):
        return self.status_bar


app = App()
