from datetime import datetime, timedelta
from typing import Optional

import jwt
from fastapi import HTTPException, Depends
from fastapi_login import LoginManager
from pydantic import BaseModel

from database.models.user import Users


class TokenManager:
    jwt_token_prefix: str = "Token"
    SECRET_KEY = "246c02f153b6fdc0e2de79f565ccf8c59d250ec4c8daa26128537b9424b55acd"  # Replace with a secure secret key
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 15


manager = LoginManager(TokenManager.jwt_token_prefix, token_url="/auth/login", default_expiry=timedelta(minutes=30),
                       use_cookie=True)


@manager.user_loader()
def get_user_by_email(email: str) -> Optional[Users]:

    user = Users.objects(email=email).first()

    return user


async def get_user(email: str) -> Optional[Users]:

    user = Users.objects(email=email, is_active=True).first()

    return user


class TokenData(BaseModel):
    username: str


def create_access_token(email: str):
    payload = {'iat': datetime.utcnow(),
               'scope': 'access_token',
               'sub': email}

    return manager.create_access_token(data=payload)


def create_refresh_token(email: str):
    payload = {'iat': datetime.utcnow(),
               'scope': 'token_refresh',
               'sub': email}

    return manager.create_access_token(data=payload)

