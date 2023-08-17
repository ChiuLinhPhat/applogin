from fastapi import Form
from pydantic import BaseModel


class Token(BaseModel):
    """
    :return access_token
    """
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"
    access_expire: int = 1800
    refresh_expire: int = 1800


class TokenNew(BaseModel):
    """
    :return access_token
    """
    access_token: str
    token_type: str = "Bearer"
    access_expire: int = 1800


class checkOtp:

    def __init__(
            self,
            email: str = Form(...),
            opt: str = Form(...)
    ):
        self.email = email
        self.opt = opt


