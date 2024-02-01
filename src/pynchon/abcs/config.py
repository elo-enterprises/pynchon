""" pynchon.abcs.config
"""

from pynchon.util.text import dumps

dumps.JSONEncoder.register_encoder(type=Config, fxn=lambda x: dumps.json(x.dict()))
