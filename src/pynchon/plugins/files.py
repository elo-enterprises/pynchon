"""
"""
from pynchon import abcs, models


class FileHeaders(models.Planner):
    """Mutates {src} files to add header"""

    name = 'file-headers'

    class config_kls(abcs.Config):
        config_key = 'file-headers'
