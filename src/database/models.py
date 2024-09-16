from sqlalchemy.orm import (
    DeclarativeBase,
    mapped_column,
    Mapped,
    Session,
    relationship
)
from pydantic import BaseModel

from sqlalchemy import (
    ForeignKey,
    String,
    Integer,
    select
)

import datetime 

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(
        primary_key = True
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now(),
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now(),
        onupdate=datetime.datetime.now()
    )

    @classmethod
    def create(cls, schema:BaseModel, sess:Session):
        with sess() as sess:
            clsIns = cls(**schema.dict())
            sess.add(clsIns)
            sess.commit()
            
            print(f'{cls.__name__} created !!!')
            return clsIns
    
    @classmethod
    def read(cls, sess:Session):
        with sess() as sess:
            result = sess.execute(select(cls).order_by(cls.id))
            return result.all()

class Client(Base):
    __tablename__ = 'client'

    name: Mapped[str] = mapped_column(String(30))
    
    def __str__(self):
        return f"| {self.id:<2} | {self.name:<30} |"

class Product(Base):
    __tablename__ = 'product'

    name: Mapped[str] = mapped_column(String(30))
    amount: Mapped[int] = mapped_column(Integer)

class Provider(Base):
    __tablename__ = 'provider'

    name: Mapped[str] = mapped_column(String(30))
    product: Mapped[list[Product]] = relationship(secondary='provide')

    def __str__(self):
        return f"| {self.id:<2} | {self.name:<30} |"

class Provide(Base):
    __tablename__ = "provide"
    provider_id: Mapped[int] = mapped_column(ForeignKey("provider.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    amount: Mapped[int] = mapped_column(default = 0)