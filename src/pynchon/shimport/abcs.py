""" shimport.abc
"""
import itertools


class FilterResult(list):
    """ """

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
