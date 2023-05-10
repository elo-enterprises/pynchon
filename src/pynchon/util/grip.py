"""
"""
import psutil

from pynchon import abcs
from pynchon.util.os import invoke, filter_pids

from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)


def serving():
    """ """
    return bool(_is_my_grip())


def _current_grip_procs() -> typing.List[psutil.Process]:
    """ """
    return filter_pids(name='grip')


def _my_grip() -> psutil.Process:
    """ """
    tmp = [g for g in _current_grip_procs() if _is_my_grip(g)]
    if tmp:
        return tmp[0]


def _is_my_grip(g) -> bool:
    """ """
    return g.cwd() == str(abcs.Path('.').absolute())


def serve(
    background: bool = True, force: bool = False, logfile: str = '.tmp.grip.log'
) -> object:
    """ """

    def _do_serve():
        bg = '&' if background else ''
        invoke(f'grip >> {logfile} 2>&1 {bg}', system=True)

    grips = _current_grip_procs()
    if grips:
        LOGGER.warning(f"{len(grips)} copies of grip are already started")
        for p in grips:
            # p.cmdline()
            if _is_my_grip(p):
                LOGGER.warning(f"grip @ {p.pid} already serving this project")
                if force:
                    LOGGER.critical("`force` was passed; killing it anyway..")
                    p.kill()
                else:
                    LOGGER.debug("Skipping startup.")
                break
        else:
            LOGGER.warning("No grips are serving this project.")
            return _do_serve()
    else:
        return _do_serve()
