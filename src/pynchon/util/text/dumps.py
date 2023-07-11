""" pynchon.util.text.dumps """
import json as modjson

import yaml as modyaml

from pynchon.util import lme, text

LOGGER = lme.get_logger(__name__)


class JSONEncoder(modjson.JSONEncoder):
    """ """

    encoders = {}

    @classmethod
    def register_encoder(kls, type=None, fxn=None):
        kls.encoders[type] = fxn

    def encode(self, obj):
        """
        :param obj:
        """
        result = None
        if callable(getattr(obj, "json", None)):
            return obj.json()
        for _type, fxn in self.encoders.items():
            if isinstance(obj, (_type,)):
                LOGGER.warning(f"{obj} matches {_type}, using {fxn}")
                return fxn(obj)
        return super().encode(obj)

    # FIXME: use multimethod
    def default(self, obj):
        if callable(getattr(obj, "dict", None)):
            return obj.dict()
        if callable(getattr(obj, "as_dict", None)):
            return obj.as_dict()
        else:
            enc = self.encoders.get(type(obj), str)
            return enc(obj)


def yaml(file=None, content=None, obj=None):
    """
    Parse JSON input and returns (or writes) YAML
    """
    content = content or text.loadf.loadf(file=file, content=content)
    obj = obj or modjson.loads(content)
    content = modyaml.dump(obj)
    return content


def json(obj, cls=None, minified=False, indent: int = 2) -> str:
    """ """
    indent = None if minified else indent
    # from pynchon.abcs.path import JSONEncoder
    cls = cls if cls is not None else JSONEncoder
    return modjson.dumps(obj, indent=indent, cls=cls)


JSONEncoder.register_encoder(type=map, fxn=list)
