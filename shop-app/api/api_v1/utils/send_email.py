from email.message import EmailMessage
from core.config import settings

import aiosmtplib


async def send_token_email(
    recipient: str,
    subject: str,
    token: str,
    verification: bool | None = None,
    password_reset: bool | None = None,
):
    admin_email = settings.api.v1.email.admin_email

    message = EmailMessage()
    message["From"] = admin_email
    message["To"] = recipient
    message["Subject"] = subject
    if verification:
        message.set_content(
            settings.api.v1.email.verif_message(
                email=recipient,
                token=token,
            )
        )
    elif password_reset:
        message.set_content(
            settings.api.v1.email.passw_reset_message(
                email=recipient,
                token=token,
            )
        )

    await aiosmtplib.send(
        message,
        sender=admin_email,
        recipients=[recipient],
        hostname=settings.api.v1.email.host,
        port=settings.api.v1.email.port,
    )
