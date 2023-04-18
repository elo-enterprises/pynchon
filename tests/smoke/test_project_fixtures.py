""" tests for `python -mlib605.databricks` CLI
"""
from pynchon.abcs import Path
from pynchon.util import testing
from pynchon.util.os import invoke

TEST_INFO = testing.get_test_info(__file__)
PROJECT_FIXTURES = TEST_INFO.fixtures.path/"projects"
def test_fixtures():
    project_folders = [d for d in PROJECT_FIXTURES.iterdir() if d.is_dir()]
    for p in project_folders:
        invoke(f"cd {p.absolute()} && PYNCHON_ROOT=. pynchon project config")
