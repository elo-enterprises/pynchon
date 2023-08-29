""" pynchon.util.text.dumps """
import json as modjson

import yaml as modyaml

from pynchon.util import lme, text

LOGGER = lme.get_logger(__name__)

from fleks import models 
json=models.to_json
JSONEncoder=models.JSONEncoder
from pynchon import abcs 
JSONEncoder.register_encoder(type=abcs.Path,fxn=lambda v: str(v))
def yaml(file=None, content=None, obj=None):
    """
    Parse JSON input and returns (or writes) YAML
    """
    content = content or text.loadf.loadf(file=file, content=content)
    obj = obj or modjson.loads(content)
    content = modyaml.dump(obj)
    return content





