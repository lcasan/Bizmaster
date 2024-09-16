import click
from ..commands import show
from sqlalchemy import select
from ...database.connection import Session
from ...database.models import Client, Provider

@show.command()
@click.option('--select', default='all')
def client(select):
    if select == 'all':
        clients = Client.read(sess = Session)
        for client in clients:
            print(client[0])


@show.command()
@click.option('--select', default='all')
def provider(select):
    if select == 'all':
        providers = Provider.read(sess = Session)
        for provider in providers:
            print(provider[0])