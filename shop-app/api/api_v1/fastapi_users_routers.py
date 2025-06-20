from core.types import UserIdType

from fastapi_users import FastAPIUsers

from core.models import User
from api.dependecies.authentication import (
    get_user_manager,
    authentication_backend,
)

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)
