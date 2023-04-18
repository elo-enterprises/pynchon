import click

@click.version_option()
@click.group("pynchon")
def entry():
    """pynchon: a utility for docs generation and template-rendering"""
