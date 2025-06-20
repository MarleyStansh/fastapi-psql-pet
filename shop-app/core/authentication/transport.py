from fastapi_users.authentication import BearerTransport

bearer_transport = BearerTransport(
    # TODO: update_url
    tokenUrl="auth/jwt/login",
)
