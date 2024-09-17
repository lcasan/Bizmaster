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

@cli.group
def add():
    pass


from .subcommands.create import *
from .subcommands.show import *
from .subcommands.add import *