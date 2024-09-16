from src.database import models
from src.database.connection import engine
from src.cli.commands import cli

if __name__  == '__main__':
    models.Base.metadata.create_all(engine)
    cli()