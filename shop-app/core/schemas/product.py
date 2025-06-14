from typing import ClassVar
from pydantic import (
    BaseModel,
    ConfigDict,
)


class ProductBase(BaseModel):
    name: str
    price: int
    description: str


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: int

    # model_config: ClassVar = ConfigDict(
    #     from_attributes=True,
    # )


class ProductUpdate(ProductBase):
    pass
