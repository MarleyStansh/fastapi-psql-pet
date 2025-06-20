from typing import TYPE_CHECKING
from fastapi_users.db import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)

from .base import Base
from core.types import UserIdType
from .mixins import IntIdPkMixin

from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, IntIdPkMixin, SQLAlchemyBaseUserTable[UserIdType]):
    pass

    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyUserDatabase(session, cls)
