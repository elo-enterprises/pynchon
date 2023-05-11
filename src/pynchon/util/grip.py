""" pynchon.util.grip
"""
import pathlib

import psutil
from grip import create_app
from flask import Flask, send_from_directory
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from pynchon import abcs, cli
from pynchon.util.os import invoke, filter_pids

from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)
logfile: str = '.tmp.grip.log'


def _current_flask_procs() -> typing.List[psutil.Process]:
    """ """
    return filter_pids(name='flask')


def _is_my_grip(g) -> bool:
    """ """
    return g.cwd() == str(abcs.Path('.').absolute())


class Server:
    def serve(self, background=True) -> psutil.Process:
        if self.proc:
            return self.proc

    @property
    def proc(self) -> psutil.Process:
        tmp = [g for g in _current_flask_procs() if _is_my_grip(g)]
        if tmp:
            result = tmp[0]
            return result

    @property
    def live(self) -> bool:
        return bool(self.proc)

    @property
    def port(self):
        if self.proc:
            conns = self.proc.connections()
            return conns and conns[0].laddr.port


server = Server()


grip_app = create_app(
    user_content=True,
)

raw_file_server = Flask(__name__)
raw_file_server.debug = True


@raw_file_server.route('/<path:path>')
def raw(path):
    raw_file_server.logger.critical(path)
    return send_from_directory(pathlib.Path('.').absolute(), path)


compound = Flask(__name__)
compound.wsgi_app = DispatcherMiddleware(grip_app, {'/__raw__': raw_file_server})


@cli.click.group
def entry():
    """ """


@entry.command('serve')
@cli.click.option('--fg', is_flag=True, default=False)
@cli.click.option('--force', is_flag=True, default=False)
@cli.click.option('--ls', is_flag=True, default=False)
@cli.click.option('--port', default='6149')
def serve(
    fg: bool = None, ls: bool = None, force: bool = None, port: str = None
) -> object:
    """ """

    def _do_serve():
        bg = '&' if background else ''
        # return invoke(f'grip >> {logfile} 2>&1 {bg}', system=True)
        return invoke(
            f'flask --app pynchon.util.grip:compound run --port {port}>> {logfile} 2>&1 {bg}',
            system=True,
        )

    LOGGER.critical("trying to serve files")
    background = not fg
    should_start = ls or True
    grips = _current_flask_procs()
    # if ls:
    #     LOGGER.critical(f'{grips}')
    #     return
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
    result = should_start and _do_serve()
    LOGGER.critical(result)
    return result


if __name__ == '__main__':
    entry()
