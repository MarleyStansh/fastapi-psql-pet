from fastapi import APIRouter
from core.config import settings

from fastapi import (
    APIRouter,
    Body,
    Depends,
    Request,
    status,
    BackgroundTasks,
)
from pydantic import EmailStr

from fastapi_users import exceptions, models
from fastapi_users.manager import BaseUserManager

from .utils.send_email import send_token_email
from api.dependecies.authentication import (
    get_user_manager,
)

router = APIRouter()


@router.post(
    "/request-verify-token",
    status_code=status.HTTP_202_ACCEPTED,
    name="verify:request-token",
)
async def request_verify_token(
    request: Request,
    background_tasks: BackgroundTasks,
    email: EmailStr = Body(..., embed=True),
    user_manager: BaseUserManager[models.UP, models.ID] = Depends(get_user_manager),
):
    try:
        user = await user_manager.get_by_email(email)
        token = await user_manager.request_verify(user, request)
        background_tasks.add_task(
            send_token_email,
            recipient=user.email,
            subject="Your verification on site.com",
            token=token,
            verification=True,
        )
    except (
        exceptions.UserNotExists,
        exceptions.UserInactive,
        exceptions.UserAlreadyVerified,
    ):
        pass
    return None


@router.post(
    "/forgot-password",
    status_code=status.HTTP_202_ACCEPTED,
    name="reset:forgot_password",
)
async def forgot_password(
    request: Request,
    background_tasks: BackgroundTasks,
    email: EmailStr = Body(..., embed=True),
    user_manager: BaseUserManager[models.UP, models.ID] = Depends(get_user_manager),
):
    try:
        user = await user_manager.get_by_email(email)
    except exceptions.UserNotExists:
        return None

    try:
        token = await user_manager.forgot_password(user, request)
        background_tasks.add_task(
            send_token_email,
            recipient=user.email,
            subject="Password reset on site.com",
            token=token,
            password_reset=True,
        )
    except exceptions.UserInactive:
        pass

    return None
