""" pynchon.util.os.pids
"""
import shimport

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
        except (psutil.AccessDenied,):
            continue
        except (psutil.NoSuchProcess,):
            continue
    return survivors