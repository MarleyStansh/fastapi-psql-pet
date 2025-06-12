from fastapi import APIRouter, status
from core.config import settings
from .crud import products as product_crud
from sqlalchemy.ext.asyncio import AsyncSession
from core.schemas import ProductRead, ProductCreate
from fastapi import Depends
from core.models import db_helper

router = APIRouter(prefix=settings.api.v1.products, tags=["Users"])


@router.get("", response_model=list[ProductRead])
async def get_products(
    session: AsyncSession = Depends(db_helper.session_getter),
):
    products = await product_crud.get_all_products(
        session=session,
    )
    return products


@router.post("", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_create: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    product = await product_crud.create_product(
        session=session,
        product_create=product_create,
    )
    return product
