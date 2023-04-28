""" pynchon.app
"""
import sys
import atexit

import enlighten
from pynchon import abcs

manager = enlighten.get_manager()
status = manager.status_bar(
    status_format=u'{app}{fill}{stage}{fill}{elapsed}',
    color='bold_underline_bright_white_on_lightslategray',
    justify=enlighten.Justify.CENTER,
    app='Pynchon',
    stage='...',
    autorefresh=True,
    min_delta=0.1,
)
atexit.register(lambda: [status.update(stage="\o/"), manager.stop()])  # noqa: W605
events = abcs.AttrDict(status=status)

# docs = manager.term.link(
#     'https://python-enlighten.readthedocs.io/en/stable/examples.html',
#     'Read the Docs')
# manager.status_bar(
#     'footer-pynchon',
#     position=1, fill='-',
#     justify=enlighten.Justify.CENTER)

# https://stackoverflow.com/questions/9741351/how-to-find-exit-code-or-reason-when-atexit-callback-is-called-in-python


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
        from rich.text import Text
        from rich.console import Console, Theme

        console = Console()
        #     theme=Theme({
        #         "info": "dim cyan",
        #         "warning": "magenta",
        #         "danger": "bold red"
        #     })
        # )
        # console.print(f"death by exception: {hooks.exception}",style='danger')
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
#
# # test
# sys.exit(1)
