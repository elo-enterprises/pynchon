""" pynchon.util.shfmt.__main__
"""
import sys

if __name__ == '__main__':
    from . import *

    cmd = sys.argv[-1]
    result = bash_fmt(cmd)
