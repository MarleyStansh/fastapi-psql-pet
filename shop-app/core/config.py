from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)
from pydantic import BaseModel, PostgresDsn
from typing import ClassVar


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class EmailConfig(BaseModel):
    host: str = "localhost"
    port: int = 8025
    admin_email: str = "admin@site.com"

    @classmethod
    def verif_message(self, email, token):
        return f"Verification token for user with email {email}: {token}. Use it to verify your account."

    @classmethod
    def passw_reset_message(self, email, token):
        return f"Password reset token for user with email {email}: {token}. Use it to reset your password."


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    products: str = "/products"
    auth: str = "/auth"
    users: str = "/users"
    email: EmailConfig = EmailConfig()


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()

    @property
    def bearer_token_url(self):
        parts = (self.prefix, self.v1.prefix, self.v1.auth, "/login/")
        path = "".join(parts)
        return path.removeprefix("/")


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 50

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class AccessTokenConfig(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig
    access_token: AccessTokenConfig

    model_config = SettingsConfigDict(
        env_file=[
            ".env.template",
            ".env",
        ],
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )


settings = Settings()
