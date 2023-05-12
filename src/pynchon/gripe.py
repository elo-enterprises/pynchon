""" pynchon.gripe
"""
import os
import pathlib

import grip
import psutil
from flask import Flask, send_from_directory
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from pynchon import abcs, cli
from pynchon.util.os import filter_pids

from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)
logfile: str = '.tmp.gripe.log'


def _current_flask_procs() -> typing.List[psutil.Process]:
    """ """
    return filter_pids(name='flask')


def _is_my_grip(g) -> bool:
    return g.cwd() == str(abcs.Path('.').absolute())


class Server:
    """ """

    @property
    def proc(self) -> psutil.Process:
        """ """
        tmp = [g for g in _current_flask_procs() if _is_my_grip(g)]
        if tmp:
            result = tmp[0]
            return result

    @property
    def live(self) -> bool:
        """ """
        return bool(self.proc)

    @property
    def port(self):
        """ """
        if self.proc:
            conns = self.proc.connections()
            return conns and conns[0].laddr.port

    @property
    def raw_file_server(self):
        """ """
        raw_file_server = Flask(__name__)
        raw_file_server.debug = True

        @raw_file_server.route('/<path:path>')
        def raw(path):
            raw_file_server.logger.critical(path)
            return send_from_directory(pathlib.Path('.').absolute(), path)

        return raw_file_server

    @property
    def app(self):
        """ """
        compound = Flask(__name__)
        compound.wsgi_app = DispatcherMiddleware(
            grip.create_app(user_content=True), {'/__raw__': self.raw_file_server}
        )
        return compound


server = Server()
app = server.app


def _do_serve(background=True, port='6149'):
    bg = '&' if background else ''
    return os.system(
        f'flask --app pynchon.gripe:app run --port {port}>> {logfile} 2>&1 {bg}',
    )


@cli.click.group
def entry():
    """
    CLI for actions on gripe servers.
    """
    pass


def _list():
    """Lists running servers for this working-dir"""
    result = _current_flask_procs()
    LOGGER.critical(result)
    return result


@cli.click.option('--fg', help='run in foreground', is_flag=True, default=False)
@cli.click.option(
    '--force', help='force kill if already running', is_flag=True, default=False
)
@cli.click.option(
    '--port',
    help='port to listen on.  (leave empty to use next available)',
    default='6149',
)
def start(
    fg: bool = None, ls: bool = None, force: bool = None, port: str = None
) -> object:
    """Starts a webserver for working-dir"""

    LOGGER.critical("trying to serve files")
    background = not fg
    should_start = ls or True
    grips = _list()
    if grips:
        LOGGER.critical(f"{len(grips)} copies of flask are already started")
        for p in grips:
            if _is_my_grip(p):
                LOGGER.critical(f"flask @ pid {p.pid} is already serving this project")
                if force:
                    LOGGER.critical("`force` was passed; killing it anyway..")
                    p.kill()
                else:
                    LOGGER.critical("Skipping startup.")
                    should_start = False
                break
        else:
            LOGGER.critical("No flasks are serving this project.")
    result = should_start and _do_serve(port=port, background=background)
    LOGGER.critical(result)
    return result


def stop(grips=[], grip=None):
    """Stops server (if any) for this working-dir"""
    grips = grips or (grip and [grip]) or _list()
    if not grips:
        LOGGER.critical(f"no copies of flask are started here")
    else:
        for p in grips:
            if _is_my_grip(p):
                LOGGER.critical(f"flask @ pid {p.pid} started here")
                LOGGER.critical("killing it..")
                p.kill()
    return True


def restart():
    """Restarts server for this working-dir"""
    _list()
    stop()
    import time

    time.sleep(1.5)
    start()


entry.command('restart')(restart)
entry.command('stop')(stop)
entry.command('ls')(_list)
entry.command('list')(_list)
entry.command('start')(start)

if __name__ == '__main__':
    entry()
