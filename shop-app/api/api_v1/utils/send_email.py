from email.message import EmailMessage
from core.config import settings

import aiosmtplib


async def send_token_verification_email(
    recipient: str,
    subject: str,
    token: str,
):
    admin_email = settings.api.v1.email.admin_email

    message = EmailMessage()
    message["From"] = admin_email
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(
        settings.api.v1.email.verif_message(
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
