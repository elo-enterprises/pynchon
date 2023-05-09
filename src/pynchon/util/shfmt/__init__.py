""" pynchon.util.shfmt
"""
from .grammar import generic_main, asjson, main, bashParser, Semantics


def fmt(text, filename='?'):
    semantics = Semantics()
    parser = bashParser()
    return parser.parse(
        text,
        parseinfo=True,
        filename=filename,
        semantics=semantics,
    )
bash_fmt=fmt
