""" pynchon.plugins.files
"""
from pynchon import abcs, models


class SrcHeaders(models.Planner):
    """Plans changes for files under {src_root}"""

    name = 'src-headers'
    cli_name = 'src-file'

    class config_class(abcs.Config):
        config_key = 'src-headers'


# # -*- coding: utf-8 -*-
#
# """Module documentation goes here
#    and here
#    and ...
# """
