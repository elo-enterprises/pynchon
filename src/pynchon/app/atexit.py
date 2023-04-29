"""
"""
import sys
import atexit

class ExitHooks(object):
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
