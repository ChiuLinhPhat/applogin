from typing import Annotated

from fastapi import APIRouter, Depends, Security, Request, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordBearer
from schemas.input.auth import Token, TokenNew
from database.queries.auth import create_access_token, create_refresh_token, get_user_by_email, manager, get_user
from schemas.output.showaccout import show_she
from database.models.user import Users
router = APIRouter(
    prefix="/auth",
    tags=['Admin']
)
bearer = HTTPBearer()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = await get_user_by_email(token)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user


@router.post('/login', response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await get_user_by_email(form_data.username)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(user.email)
    refresh_token = create_refresh_token(str(user.id))
    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="Bearer",
        access_expire=1800,
        refresh_expire=1800
    )


@router.get('/show', response_model=show_she)
async def show(active_user=Depends(manager)):
    user = get_user_by_email(active_user.email)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail=" Unavailing authentication!"
        )
    return show_she(
        username=user.name,
        email=user.email
    )
