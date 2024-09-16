from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .models import Base

engine = create_engine('sqlite:///db.db')

Session = sessionmaker(
    bind = engine,
    expire_on_commit = False,
    class_ = Session
)