""" pynchon.util.os
"""
import os
import subprocess
from collections import namedtuple

from . import lme

LOGGER = lme.get_logger(__name__)

from pynchon.fleks import meta


class Invocation(meta.NamedTuple, metaclass=meta.namespace):
    cmd: str = ''
    stdin: str = ""
    interactive: bool = False
    large_output: bool = False
    log_command: bool = True
    environment: dict = {}
    log_stdin: bool = True
    system: bool = False
    load_json: bool = False

    def __enter__(self, *args, **kwargs):
        msg = "running command: (system={})\n\t{}".format(self.system, self.cmd)
        self.log_command and LOGGER.warning(msg)
        self.log_command and lme.CONSOLE.print(self)

    def __exit__(self, *args, **kwargs):
        pass

    def __rich__(self):
        from rich.syntax import Syntax

        from pynchon.util import shfmt

        if self.log_command:
            # LOGGER.warning('shfmt: ' + shfmt.bash_fmt(self.cmd))
            return Syntax(shfmt.bash_fmt(self.cmd), 'bash', word_wrap=True)
            # return Syntax(self.cmd, 'bash', word_wrap=True)

    def __call__(self):
        if self.system:
            assert not self.stdin and not self.interactive
            error = os.system(self.cmd)
            # FIXME: subclass namedtuple here
            # result = namedtuple(
            #     "InvocationResult",
            #     ["failed", "failure", "success", "succeeded", "stdout", "stdin"],
            # )
            return InvocationResult(
                **{
                    **self._dict,
                    **dict(
                        failed=bool(error),
                        failure=bool(error),
                        success=not bool(error),
                        succeeded=not bool(error),
                        stdout="<os.system>",
                        stdin="<os.system>",
                    ),
                }
            )
        exec_kwargs = dict(
            shell=True,
            env={**{k: v for k, v in os.environ.items()}, **self.environment},
        )
        if self.stdin:
            msg = "command will receive pipe:\n{}"
            self.log_stdin and LOGGER.debug(msg.format(((self.stdin))))
            exec_kwargs.update(
                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            exec_cmd = subprocess.Popen(cmd, **exec_kwargs)
            exec_cmd.stdin.write(stdin.encode("utf-8"))
            exec_cmd.stdin.close()
            exec_cmd.wait()
        else:
            if not self.interactive:
                exec_kwargs.update(
                    stdout=subprocess.PIPE,
                    # stderr=subprocess.PIPE
                )
            exec_cmd = subprocess.Popen(self.cmd, **exec_kwargs)
            exec_cmd.wait()
        if exec_cmd.stdout:
            exec_cmd.stdout = (
                "<LargeOutput>"
                if self.large_output
                else exec_cmd.stdout.read().decode("utf-8")
            )
        else:
            exec_cmd.stdout = "<Interactive>"
        if exec_cmd.stderr:
            exec_cmd.stderr = exec_cmd.stderr.read().decode("utf-8")
        exec_cmd.failed = exec_cmd.returncode > 0
        exec_cmd.succeeded = not exec_cmd.failed
        exec_cmd.success = exec_cmd.succeeded
        exec_cmd.failure = exec_cmd.failed
        if self.load_json:
            assert exec_cmd.succeeded, exec_cmd.stderr
            import json

            exec_cmd.json = json.loads(exec_cmd.stdout)
        return exec_cmd


class InvocationResult(meta.NamedTuple, metaclass=meta.namespace):
    cmd: str = ''
    stdin: str = ""
    interactive: bool = False
    large_output: bool = False
    log_command: bool = True
    environment: dict = {}
    log_stdin: bool = True
    system: bool = False
    load_json: bool = False
    json: dict = False
    failed: bool = None
    failure: bool = None
    succeeded: bool = None
    success: bool = None
    stdout: str = ""


def invoke(cmd: str, **kwargs):
    """
    dependency-free replacement for the `invoke` module,
    which fixes problems with subprocess.POpen and os.system.
    """
    invoc = Invocation(cmd=cmd, **kwargs)
    with invoc:
        pass
    result = invoc()
    return result
