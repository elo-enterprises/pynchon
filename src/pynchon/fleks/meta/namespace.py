class Namespace:
    """ """

    def toJSON(self, *args):
        """

        :param *args:

        """
        from pynchon.util import text

        return text.to_json(self._dict, *args)

    @property
    def _dict(self):
        """ """
        return self._asdict()

    def items(self):
        """ """
        return self._dict.items()

    def keys(self):
        """ """
        return self._dict.keys()

    def values(self):
        """ """
        return self._dict.values()


def namespace(name, bases, namespace):
    """

    :param name: param bases:
    :param namespace:
    :param bases:

    """
    for k in dir(Namespace):
        if k.startswith("__"):
            continue
        v = getattr(Namespace, k)
        if k not in namespace:
            namespace[k] = v
    return type(name, bases, namespace)
