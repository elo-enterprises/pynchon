""" pynchon.abcs
"""
import pynchon

LOGGER = pynchon.get_logger(__name__)


class Config(dict):
    """ """

    def __init__(self, **kwargs):
        super(Config, self).__init__(**kwargs)
        props = [
            p
            for p in dir(self.__class__)
            if all(
                [
                    not p.startswith("_"),
                    isinstance(getattr(self.__class__, p), property),
                ]
            )
        ]
        for p in props:
            # LOGGER.debug(f'initializing property: {p}')
            # if p in kwargs:
            #     continue
            self[p] = getattr(self, p)

    # @property
    # def _pynchon_conf(self):
    #     from pynchon.api.pynchon import PynchonConfig
    #     return PynchonConfig()
