"""
"""
from pynchon import abcs, models


class FileHeaders(models.Planner):
    """Adds a standard file-header to project source-files"""

    name = 'file-headers'

    class config_kls(abcs.Config):
        config_key = 'file-headers'
