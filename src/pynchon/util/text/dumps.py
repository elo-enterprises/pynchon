""" pynchon.util.text.dumps """
import json as modjson

from pynchon.util import lme

LOGGER = lme.get_logger(__name__)

import yaml as modyaml

from pynchon.util import text


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

        for type, fxn in self.encoders.items():
            if isinstance(obj, (type,)):
                LOGGER.warning(f"{obj} matches {type}, using {fxn}")
                return fxn(obj)

        def default():
            return super(JSONEncoder, self).encode(obj)

        try:
            toJSON = getattr(obj, "toJSON", default) or default
        except (Exception,) as exc:
            toJSON = default
        return toJSON()

    # FIXME: use multimethod
    def default(self, obj):
        toJSON = getattr(obj, "toJSON", None)
        # jsonify = getattr(obj, "json", None)
        as_dict = getattr(obj, "as_dict", None)
        if as_dict is not None and callable(as_dict):
            LOGGER.warning(f"{type(obj)} brings custom as_dict()")
            return obj.as_dict()
        # elif jsonify is not None and callable(jsonify):
        #     LOGGER.warning(f"{type(obj)} brings custom json()")
        #     return obj.json()
        elif toJSON is not None:
            assert callable(toJSON)
            LOGGER.warning(f"{type(obj)} brings custom toJSON()")
            return obj.toJSON()
        elif isinstance(obj, map):
            return list(obj)
        else:
            LOGGER.warning(f"coercing {obj} to string")
            # import IPython; IPython.embed()
            return str(obj)
        return super().default(obj)


def yaml(file=None, content=None, obj=None):
    """
    Parse JSON input and returns (or writes) YAML
    """
    content = content or text.loadf.loadf(file=file, content=content)
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
