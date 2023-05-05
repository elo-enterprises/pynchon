""" pynchon.util.shfmt.__main__
"""
import sys
import pprint


if __name__ == '__main__':
    from . import *
    cmd = sys.argv[-1]
    # sys.stdin.read()
    result = bash_fmt_display(cmd)
