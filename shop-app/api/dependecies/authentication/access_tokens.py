from typing import TYPE_CHECKING
from fastapi import Depends
from core.models import db_helper, AccessToken

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_token_db(
    session: "AsyncSession" = Depends(db_helper.session_getter),
):
    yield AccessToken.get_db(session=session)
