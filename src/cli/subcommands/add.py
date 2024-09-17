import click
from rich.table import Table
from rich.console import Console
from ..commands import add
from ...database.connection import Session
from ...database import models
from ... import schemas

@add.command()
@click.option('--product_id', type = int, default = 0, help = 'id of product\'s stock')
@click.option('--provider_id', type = int, default = 0, help = 'id of provider')
@click.option('--amount', type = int, default = 0, help = 'Products amount to insert in the stock')
@click.option('--price', type = int, default = 0, help = 'Price of product to insert in the stock')
def product(product_id, provider_id, amount, price):
    product = models.Product.searchID(
        id = product_id,
        sess = Session
    )
    
    models.Product.update(
        id = product_id,
        schema = schemas.Product( name = product.name, amount = product.amount + amount),
        sess = Session
    )

    models.Stock.create(
        schema = schemas.Stock(
            product_id = product_id,
            provider_id = provider_id,
            amount = amount,
            price = price
        ),
        sess = Session 
    )