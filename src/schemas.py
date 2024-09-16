from pydantic import (
    BaseModel,
    Field
)


class Client(BaseModel):
    name: str = Field(
        max_length = 30
    )

class Provider(BaseModel):
    name: str = Field(
        max_length = 30
    )

class Product(BaseModel):
    name: str = Field(
        max_length = 30
    )

class Provide(BaseModel):
    provider_id: int
    product_id: int
    amount: int
    