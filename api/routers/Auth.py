from typing import Annotated

from fastapi import APIRouter, Depends, Security, Request
from fastapi.security import OAuth2PasswordRequestForm, HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordBearer
from schemas.input.auth import Token, TokenNew
router = APIRouter(
    prefix="/auth",
    tags=['Admin']
)
bearer = HTTPBearer()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


@router.get('/login', tags=["Auth"], response_model=Token)
async def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends()) -> Token:

    return None

# return Token(access_token=token, refresh_token=token_refresh, token_type='Bearer',
#              access_expire=settings.access_token_lifetime,
#              refresh_expire=settings.refresh_token_lifetime)

