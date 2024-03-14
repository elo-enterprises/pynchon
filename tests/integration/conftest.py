import pathlib

import pytest


@pytest.fixture
def fixtures_dir():
    return pathlib.Path(__file__).parent.parent / "fixtures"


# def pytest_collect_file(parent, path):
#     p = pathlib.Path(str(path))
#     if p.suffix == '.py' and p.parent.name == 'scripts':
#         return Script(path, parent)
#
#
# class Script(pytest.File):
#     def collect(self):
#         yield ScriptItem(self.name, self)
#
#
# class ScriptItem(pytest.Item):
#     def runtest(self):
#         runpy.run_path(self.fspath)
#
#     def repr_failure(self, excinfo):
#         excinfo.traceback = excinfo.traceback.cut(path=self.fspath)
#         return super().repr_failure(excinfo)
