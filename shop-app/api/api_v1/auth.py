from fastapi import APIRouter
from core.config import settings
from .fastapi_users_routers import fastapi_users
from api.dependecies.authentication import (
    authentication_backend,
)

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_auth_router(authentication_backend),
)
