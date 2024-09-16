import click
from rich.table import Table
from rich.console import Console
from ..commands import show
from sqlalchemy import select
from ...database.connection import Session
from ...database.models import Client, Provider

@show.command()
@click.option('--select', default='all')
def client(select):
    # Create table:
    table = Table(title = 'Clients')

    table.add_column('Id', style = 'cyan')
    table.add_column('Name', style = 'green')

    if select == 'all':
        clients = Client.read(sess = Session)
        for client in clients:
            table.add_row(str(client[0].id), str(client[0].name))

    # Console
    console = Console()
    console.print(table)


@show.command()
@click.option('--select', default='all')
def provider(select):
    # Create table:
    table = Table(title = 'Providers')

    table.add_column('Id', style = 'cyan')
    table.add_column('Name', style = 'magenta')

    # Query
    if select == 'all':
        providers = Provider.read(sess = Session)
        for provider in providers:
            table.add_row(str(provider[0].id), str(provider[0].name))
    
    # Console
    console = Console()
    console.print(table)