""" pynchon.cli.options
"""
from pynchon.cli import click

quiet = click.flag("--quiet", "-q", default=False, help="Disable JSON output")
fail_fast = click.flag("--fail-fast", default=False, help="fail fast")
parallelism = click.option("--parallelism", "-p", default="1", help="Paralellism")
