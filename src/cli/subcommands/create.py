import click
from ... import schemas
from ...database import models
from ..commands import create
from ...database.connection import Session

# Client
@create.command()
@click.option('--name', prompt = 'Insert the client\'s name', help = 'The client\'s name') 
def client(name):
    models.Client.create(
        schema = schemas.Client( name = name),
        sess = Session
    )

# Provider
@create.command()
@click.option('--name', prompt = 'Insert the provider\'s name', help = 'The provider\'s name') 
def provider(name):
    models.Provider.create(
        schema = schemas.Provider( name = name),
        sess = Session
    )

# Product
@create.command()
@click.option('--name', prompt = 'Insert the product\'s name', help = 'The product\'s name') 
@click.option('--provider_id', type=int, prompt = 'Insert the provider\'s id', help = 'The provider\'s id') 
@click.option('--amount', type=int, prompt = 'Insert the product\'s amount', help = 'The product\'s amount') 
@click.option('--price', type = float, prompt = 'Insert the price\'s product', help = 'The price\'s product') 
def product(name, provider_id, amount, price):
    product = models.Product.create(
        schema = schemas.Product( name = name, amount = amount),
        sess = Session
    )

    models.Stock.create(
        schema = schemas.Stock(
            provider_id = provider_id,
            product_id = product.id,
            amount = amount,
            price = price
        ),
        sess = Session
    )