"""
"""
import json

from pynchon.abcs import visitor


def test_traversed():
    # visited=[]
    def visit(value=None, path=None):
        print(f"[{path}: {value}]")
        # visited.append([path,value])
        return value
    obj = dict(
        foo=dict(
            bar='bar',
            baz=dict(
                boom='bonk',
                list=['a','b','c'])))
    traversed = visitor.traverse(obj, visitor=visit)
    paths = traversed['paths']
    assert paths==['.foo', '.foo.bar', '.foo.baz', '.foo.baz.boom', '.foo.baz.list', '.foo.baz.list.0', '.foo.baz.list.1', '.foo.baz.list.2']
    print(json.dumps(traversed.visits,indent=2))
from pynchon.util import lme

LOGGER= lme.get_logger(__name__)

import pydash

from pynchon.api import render


class TemplatedDict(dict):
    def get_path(self,path):
        return pydash.get(self, path)

    def set_path(self,path,val):
        return pydash.set_with(self, path, val)

    @property
    def traversal(self):
        traversed = visitor.traverse(
            self,
            visitor_kwargs=dict(
                filter_value=self.is_templated,
                accumulate_paths=True))
        return traversed

    @property
    def unresolved(self):
        return self.traversal.visits

class JinjaDict(TemplatedDict):

    def render_path(self, path, strict=False):
        """ """
        strict and True
        value = self.get_path(path)
        resolved = render.j2_loads(
            text=value, context=self,
            templates=[],)
        self.set_path(path, resolved)
        LOGGER.debug(f"resolved {path} as {resolved}")

    def is_templated(self, v):
        return all([
            isinstance(v, (str,)),
            v and '{{' in v])

def test_visit_kls():
    obj = JinjaDict(
        bonk="bonk{{dot}}",
        dot="3",
        docs_root="docs",
        jinja= {
          "includes": ["{{docs_root}}/includes"]}
    )
    traversed = obj.traversal
    # expected = ['.docs_root', '.jinja', '.jinja.includes', '.jinja.includes.0']
    # assert traversed.paths==expected
    templated=obj.unresolved
    assert set(templated)==set(['.jinja.includes.0','.bonk'])
    import jinja2
    while templated:
        for i, path in enumerate(templated):
            tmp = templated.pop(i)
            try:
                obj.render_path(path)
            except (jinja2.exceptions.UndefinedError,) as exc:
                # move it to the end
                templated.append(tmp)
            else:
                # templated = templated
                break
        else:
            break

    assert not obj.unresolved
    assert obj['jinja']['includes']==["docs/includes"]

    print(json.dumps(traversed,indent=2))
