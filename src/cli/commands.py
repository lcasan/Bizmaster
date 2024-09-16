import click 

@click.group()
def cli():
    pass

@cli.group()
def create():
    pass

@cli.group()
def show():
    pass


from .subcommands.create import *
from .subcommands.show import *