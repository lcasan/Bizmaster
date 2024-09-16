import click
from ... import schemas
from ...database import models
from ..commands import create
from ...database.connection import Session

@create.command()
@click.option('--name', prompt = 'Insert the client\'s name', help = 'The client\'s name') 
def client(name):
    models.Client.create(
        schema = schemas.Client( name = name),
        sess = Session
    )

@create.command()
@click.option('--name', prompt = 'Insert the provider\'s name', help = 'The provider\'s name') 
def provider(name):
    models.Provider.create(
        schema = schemas.Provider( name = name),
        sess = Session
    )


@create.command()
@click.option('--name', prompt = 'Insert the product\'s name', help = 'The product\'s name') 
@click.option('--provider_id', type=int, prompt = 'Insert the provider\'s id', help = 'The provider\'s id') 
@click.option('--amount', type=int, prompt = 'Insert the product\'s amount', help = 'The product\'s amount') 
def product(name, provider_id, amount):
    product = models.Product.create(
        schema = schemas.Product( name = name),
        sess = Session
    )

    models.Provide.create(
        schema = schemas.Provide(
            provider_id = provider_id,
            product_id = product.id,
            amount = amount,
        ),
        sess = Session
    )
