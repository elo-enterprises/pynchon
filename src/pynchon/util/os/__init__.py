""" pynchon.util.os
"""
from pynchon import shimport

from . import models

psutil = shimport.lazy("psutil")


def filter_pids(**kwargs):
    """ """
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
    Dependency-free replacement for the `invoke` module,
    which fixes annoyances with subprocess.POpen and os.system.

    :param cmd: str:
    :param **kwargs:

    """
    invoc = models.Invocation(cmd=cmd, **kwargs)
    result = invoc()
    result.__rich__()
    return result


#
# incremental reads:
#   https://stackoverflow.com/questions/41462957/python-subprocess-communicate-freezes-when-reading-output
# import subprocess
# from time import time
# class Wrapper():
#     def call(self, cmd):
#         p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         O = ''
#         E = ''
#         last = time()
#         while p.poll() is None:
#             if time() - last > 5:
#                 print('Process is still running')
#                 last = time()
#             tmp = p.stdout.read(1).decode('utf-8')
#             if tmp:
#                 O += tmp
#             tmp = p.stderr.read(1).decode('utf-8')
#             if tmp:
#                 E += tmp
#         ret = p.poll(), O + p.stdout.read().decode('utf-8'), E+p.stderr.read().decode('utf-8') # Catch remaining output
#         p.stdout.close() # Always close your file handles, or your OS might be pissed
#         p.stderr.close()
#         return ret


def slurp_json(cmd: str, **kwargs):
    result = invoke(f"{cmd} > .tmp.{id(cmd)}")
    assert result.succeeded
    from pynchon.util.text import loadf

    return loadf.json(f".tmp.{id(cmd)}")
