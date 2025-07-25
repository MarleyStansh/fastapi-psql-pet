from .users import get_user_db
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from core.authentication.user_manager import UserManager


async def get_user_manager(
    user_db: SQLAlchemyUserDatabase = Depends(get_user_db),
):
    yield UserManager(user_db)
