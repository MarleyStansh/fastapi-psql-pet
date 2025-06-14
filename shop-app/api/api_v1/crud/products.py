from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product
from core.schemas import ProductCreate, ProductUpdate
from fastapi.exceptions import HTTPException
from fastapi import Depends


async def get_all_products(
    session: AsyncSession,
) -> Sequence[Product]:
    stmt = select(Product).order_by(Product.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_product(
    session: AsyncSession,
    product_create: ProductCreate,
) -> Product:
    product = Product(**product_create.model_dump())
    session.add(product)
    await session.commit()
    # await session.refresh()
    return product


async def get_product_by_id(
    session: AsyncSession,
    product_id: int,
) -> Product:
    product = await session.get(Product, product_id)
    if not product:
        raise HTTPException(
            status_code=404, detail="The requested product is not found."
        )
    return product


async def update_product(
    new_product: ProductUpdate,
    session: AsyncSession,
    product: Product,
    partial: bool = False,
):
    print(new_product.model_dump(exclude_unset=partial))
    for name, value in new_product.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)
    await session.commit()
    return product
