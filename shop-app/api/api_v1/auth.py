from fastapi import APIRouter
from core.config import settings
from .fastapi_users_routers import fastapi_users
from api.dependecies.authentication import (
    authentication_backend,
)
from core.schemas.user import UserCreate, UserRead

from fastapi import APIRouter


from api.dependecies.authentication import (
    authentication_backend,
)
from .auth_custom_routers import router as custom_auth_router

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)

router.include_router(custom_auth_router)

# /login/
# /logout/
router.include_router(
    fastapi_users.get_auth_router(
        authentication_backend,
        # requires_verification=True,
    ),
)

# /register/
router.include_router(
    fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
)

# /request-verify-token
# /verify
router.include_router(
    fastapi_users.get_verify_router(
        UserRead,
    )
)

# /forgot-password
# /reset-password
router.include_router(
    fastapi_users.get_reset_password_router(),
)
