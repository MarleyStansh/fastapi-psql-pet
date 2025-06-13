from fastapi import APIRouter, status, Depends
from core.config import settings
from .crud import products as product_crud
from sqlalchemy.ext.asyncio import AsyncSession
from core.schemas import ProductRead, ProductCreate, ProductUpdate, ProductUpdatePartial
from fastapi import Depends
from core.models import db_helper

router = APIRouter(prefix=settings.api.v1.products, tags=["Products"])


@router.get("/", response_model=list[ProductRead])
async def get_products(
    session: AsyncSession = Depends(db_helper.session_getter),
):
    products = await product_crud.get_all_products(
        session=session,
    )
    return products


@router.post("/", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_create: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    product = await product_crud.create_product(
        session=session,
        product_create=product_create,
    )
    return product


@router.get("/{product_id}/")
async def get_product_by_id(
    product_id: int,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    product = await product_crud.get_product_by_id(
        session=session,
        product_id=product_id,
    )
    return product


@router.put(
    "/{product_id}/",
    status_code=status.HTTP_201_CREATED,
    responses={201: {"model": ProductRead}},
)
async def update_product(
    new_product: ProductUpdate,
    session: AsyncSession = Depends(db_helper.session_getter),
    product: ProductRead = Depends(get_product_by_id),
):
    product = await product_crud.update_product(
        new_product=new_product,
        session=session,
        product=product,
    )
    await session.commit()
    return product


@router.patch("/{product_id}/")
async def update_product_partial(
    new_product: ProductUpdatePartial,
    session: AsyncSession = Depends(db_helper.session_getter),
    product: ProductRead = Depends(get_product_by_id),
):
    product = await product_crud.update_product(
        new_product=new_product,
        session=session,
        product=product,
        partial=True,
    )
    await session.commit()
    return product
