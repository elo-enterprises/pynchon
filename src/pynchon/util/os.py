""" pynchon.util.os
"""
import os
import subprocess
from collections import namedtuple

from . import lme

LOGGER = lme.get_logger(__name__)


def invoke(
    cmd=None,
    stdin="",
    interactive: bool = False,
    large_output: bool = False,
    log_command: bool = True,
    environment: dict = {},
    log_stdin: bool = True,
    system: bool = False,
    load_json: bool = False,
):
    """
    dependency-free replacement for the `invoke` module,
    which fixes problems with subprocess.POpen and os.system.
    """
    log_command and LOGGER.info(
        "running command: (system={})\n\t{}".format(system, cmd)
    )
    if system:
        assert not stdin and not interactive
        error = os.system(cmd)
        result = namedtuple(
            "InvocationResult",
            ["failed", "failure", "success", "succeeded", "stdout", "stdin"],
        )
        result.failed = result.failure = bool(error)
        result.success = result.succeeded = not bool(error)
        result.stdout = result.stdin = "<os.system>"
        return result
    exec_kwargs = dict(
        shell=True, env={**{k: v for k, v in os.environ.items()}, **environment}
    )
    if stdin:
        msg = "command will receive pipe:\n{}"
        log_stdin and LOGGER.debug(msg.format(((stdin))))
        exec_kwargs.update(
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        exec_cmd = subprocess.Popen(cmd, **exec_kwargs)
        exec_cmd.stdin.write(stdin.encode("utf-8"))
        exec_cmd.stdin.close()
        exec_cmd.wait()
    else:
        if not interactive:
            exec_kwargs.update(
                stdout=subprocess.PIPE,
                # stderr=subprocess.PIPE
            )
        exec_cmd = subprocess.Popen(cmd, **exec_kwargs)
        exec_cmd.wait()
    if exec_cmd.stdout:
        exec_cmd.stdout = (
            "<LargeOutput>" if large_output else exec_cmd.stdout.read().decode("utf-8")
        )
    else:
        exec_cmd.stdout = "<Interactive>"
    if exec_cmd.stderr:
        exec_cmd.stderr = exec_cmd.stderr.read().decode("utf-8")
    exec_cmd.failed = exec_cmd.returncode > 0
    exec_cmd.succeeded = not exec_cmd.failed
    exec_cmd.success = exec_cmd.succeeded
    exec_cmd.failure = exec_cmd.failed
    if load_json:
        assert exec_cmd.succeeded
        import json

        exec_cmd.json = json.loads(exec_cmd.stdout)
    return exec_cmd
