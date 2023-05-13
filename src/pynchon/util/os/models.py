""" pynchon.util.os.models
"""
import os
import subprocess

from pynchon.util import lme

LOGGER = lme.get_logger(__name__)

from pynchon.fleks import meta


class InvocationResult(meta.NamedTuple, metaclass=meta.namespace):
    cmd: str = ""
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
    stderr: str = ""
    pid: int = -1

    def __rich__(self):
        from pynchon import app
        from pynchon.util import shfmt

        if self.log_command:
            # LOGGER.warning('shfmt: ' + shfmt.bash_fmt(self.cmd))
            msg = f"running command: (system={self.system})\n\t{self.cmd}"
            # self.log_command and LOGGER.warning(msg)

            fmt = shfmt.bash_fmt(self.cmd)
            syntax = app.Syntax(
                f"# {self.cmd}\n\n{fmt}", "bash", line_numbers=False, word_wrap=True
            )
            panel = app.Panel(
                syntax,
                title=__name__,
                subtitle=app.Text("✔", style="green")
                if self.success
                else app.Text("❌", style="red"),
            )
            lme.CONSOLE.print(panel)


class Invocation(meta.NamedTuple, metaclass=meta.namespace):
    cmd: str = ""
    stdin: str = ""
    interactive: bool = False
    large_output: bool = False
    log_command: bool = True
    environment: dict = {}
    log_stdin: bool = True
    system: bool = False
    load_json: bool = False

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
            self.log_stdin and LOGGER.debug(msg.format(self.stdin))
            exec_kwargs.update(
                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            exec_cmd = subprocess.Popen(self.cmd, **exec_kwargs)
            exec_cmd.stdin.write(self.stdin.encode("utf-8"))
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
        # return exec_cmd
        return InvocationResult(
            **{
                **self._dict,
                **dict(
                    pid=exec_cmd.pid,
                    failed=exec_cmd.failed,
                    failure=exec_cmd.failure,
                    success=exec_cmd.success,
                    succeeded=exec_cmd.succeeded,
                    stdout=exec_cmd.stdout,
                    stderr=exec_cmd.stderr,
                    json=self.load_json and exec_cmd.json,
                ),
            }
        )
