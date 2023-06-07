""" tests.units.test_config
"""


from pynchon.config import initialized
from pynchon.util import lme, text

LOGGER = lme.get_logger(__name__)


def test_pynchon_ready():
    assert initialized.git
    assert "root" in initialized.git
    assert initialized.pynchon
    assert "working_dir" in initialized.pynchon
    # assert initialized.jinja
    tmp = initialized.pynchon

    LOGGER.critical(text.to_json(tmp))
