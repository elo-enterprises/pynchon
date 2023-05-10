""" pynchon.util.os
"""
from . import models


def filter_pids(**kwargs):
    """ """
    import psutil

    procs = [psutil.Process(p) for p in psutil.pids()]
    survivors = []
    for p in procs:
        for k, v in kwargs.items():
            tmp = getattr(p, k)
            if callable(tmp):
                tmp = tmp()
            if v != tmp:
                break
        else:
            survivors.append(p)
    return survivors


def invoke(cmd: str, **kwargs):
    """
    dependency-free replacement for the `invoke` module,
    which fixes problems with subprocess.POpen and os.system.
    """
    invoc = models.Invocation(cmd=cmd, **kwargs)
    result = invoc()
    result.__rich__()
    return result
