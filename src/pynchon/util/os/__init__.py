""" pynchon.util.os
"""
from . import models

def invoke(cmd: str, **kwargs):
    """
    dependency-free replacement for the `invoke` module,
    which fixes problems with subprocess.POpen and os.system.
    """
    invoc = models.Invocation(cmd=cmd, **kwargs)
    result = invoc()
    result.__rich__()
    return result
