""" pynchon.cli.arguments
"""
from pynchon.cli import click

file = click.argument("file", nargs=1)
file1 = click.argument("file1", nargs=1)
file2 = click.argument("file2", nargs=1)
