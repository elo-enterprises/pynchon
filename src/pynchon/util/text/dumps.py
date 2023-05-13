"""
"""
import yaml as modyaml
import json as modjson
from pynchon.util import text

def yaml(file=None, content=None, obj=None):
    """
    Parse JSON input and returns (or writes) YAML
    """
    content = content or text.loadf.loadf(file=file,content=content)
    obj = obj or modjson.loads(content)
    content = modyaml.dump(obj)
    return content

def json(obj, cls=None, minified=False, indent: int = 2) -> str:
    """
    :param indent: int:  (Default value = 2)
    :param cls:  (Default value = JSONEncoder)
    """
    indent = None if minified else indent
    from pynchon.abcs.path import JSONEncoder

    cls = cls or JSONEncoder

    return modjson.dumps(obj, indent=indent, cls=cls)
