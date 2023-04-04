"""
tests for .dot generation / rendering.

Relevant subcommands:
 * `pynchon gen dot files ..`
 * `pynchon dot render ..`
"""
import os

from pynchon import util

ITEST_ROOT = os.path.dirname(__file__)
TEST_ROOT = os.path.dirname(os.path.dirname(__file__))
FIXTURE_ROOT = os.path.join(TEST_ROOT, "fixtures")


def test_gen_dot_files():
    script = os.path.join(FIXTURE_ROOT, "scripts", "gen_dot.py")
    util.invoke(f"pynchon gen dot files --script {script}")
    outf = script.replace(".py", ".dot")
    util.invoke(f"rm {outf}")


def test_render_dot_inplace():
    dotfile = os.path.join(FIXTURE_ROOT, "graph.dot")
    assert os.path.exists(dotfile)
    tmp = util.invoke(f"pynchon render dot --in-place {dotfile}")
    assert os.path.exists(dotfile.replace(".dot", ".png"))
    outf = dotfile.replace(".dot", ".png")
    util.invoke(f"rm {outf}")
