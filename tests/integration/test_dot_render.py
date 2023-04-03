import os
import shutil
from pynchon import util

ITEST_ROOT = os.path.dirname(__file__)
TEST_ROOT = os.path.dirname(os.path.dirname(__file__))
FIXTURE_ROOT = os.path.join(TEST_ROOT, 'fixtures')

def test_render_dot_inplace():
    dotfile = os.path.join(FIXTURE_ROOT, 'graph.dot')
    assert os.path.exists(dotfile)
    tmp = util.invoke(f'pynchon render dot --in-place {dotfile}')
    assert os.path.exists(dotfile.replace('.dot','.png'))
    outf = dotfile.replace('.dot','.png')
    util.invoke(f"rm {outf}")
