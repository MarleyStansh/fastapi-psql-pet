from fastapi import APIRouter
from core.config import settings
from .fastapi_users_routers import fastapi_users
from core.schemas.user import UserUpdate, UserRead


router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"],
)

# /{id}
# /me
router.include_router(
    fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)
