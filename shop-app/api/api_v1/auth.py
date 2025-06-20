from fastapi import APIRouter
from core.config import settings
from .fastapi_users_routers import fastapi_users
from api.dependecies.authentication import (
    authentication_backend,
)
from core.schemas.user import UserCreate, UserRead

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)

# /login/
# /logout/
router.include_router(
    fastapi_users.get_auth_router(authentication_backend),
)

# /register/
router.include_router(
    fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
)

# /request-verify-token #
# /verify
router.include_router(
    fastapi_users.get_verify_router(
        UserRead,
    )
)
