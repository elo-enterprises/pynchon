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
