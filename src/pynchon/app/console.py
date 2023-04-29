""" pynchon.app
"""
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

from .events import events

events.status = status

# docs = manager.term.link(
#     'https://python-enlighten.readthedocs.io/en/stable/examples.html',
#     'Read the Docs')
# manager.status_bar(
#     'footer-pynchon',
#     position=1, fill='-',
#     justify=enlighten.Justify.CENTER)

# https://stackoverflow.com/questions/9741351/how-to-find-exit-code-or-reason-when-atexit-callback-is-called-in-python
