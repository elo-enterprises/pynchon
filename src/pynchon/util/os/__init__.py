""" pynchon.util.os
"""
from pynchon import shimport

from . import models

psutil = shimport.lazy("psutil")


def filter_pids(cmdline__contains: str = None, **kwargs):
    """ """
    procs = [psutil.Process(p) for p in psutil.pids()]
    survivors = []
    for p in procs:
        try:
            # special filters
            if cmdline__contains:
                cmdline = " ".join(p.cmdline())
                if cmdline__contains not in cmdline:
                    continue
            # normal filters
            for k, v in kwargs.items():
                tmp = getattr(p, k)
                if callable(tmp):
                    tmp = tmp()
                if v != tmp:
                    break
            else:
                survivors.append(p)
        except (psutil.AccessDenied, ):
            continue
        except (psutil.NoSuchProcess, ):
            continue
    return survivors


def invoke(cmd: str, **kwargs):
    """
    Dependency-free replacement for the `invoke` module,
    which fixes annoyances with subprocess.POpen and os.system.

    :param cmd: str:
    :param **kwargs:

    """
    invoc = models.Invocation(cmd=cmd, **kwargs)
    result = invoc()
    result.__rich__()
    return result


def slurp_json(cmd: str, **kwargs):
    """
    :param cmd: str:
    :param **kwargs:
    """
    result = invoke(f"{cmd} > .tmp.{id(cmd)}")
    assert result.succeeded
    from pynchon.util.text import loadf

    return loadf.json(f".tmp.{id(cmd)}")
