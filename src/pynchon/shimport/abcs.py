""" shimport.abc
"""

import itertools

from pynchon.util import typing


# FIXME: move to fleks?
class FilterResult(typing.List[typing.Any]):
    """ """

    def __str__(self):
        return '<{self.__class__.__name__}>'

    __repr__ = __str__

    def map(self, fxn, logger: object = None):
        """ """
        return FilterResult(list(map(fxn, self)))

    def starmap(self, fxn, logger: object = None):
        """ """
        return FilterResult(list(itertools.starmap(fxn, self)))

    def prune(self, **kwargs):
        """ """
        return FilterResult(filter(None, [x.prune(**kwargs) for x in self]))

    def filter(self, **kwargs):
        """ """
        return FilterResult([x.filter(**kwargs) for x in self])
