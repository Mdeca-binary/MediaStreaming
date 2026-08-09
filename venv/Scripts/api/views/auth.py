import jwt
import asyncio
from typing import Annotated
from datetime import datetime, timedelta, timezone

from fastapi import (APIRouter, status, 
                     Form, Depends, HTTPException, Response)
from fastapi.responses import RedirectResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import (OAuth2PasswordBearer, 
                              OAuth2PasswordRequestForm, 
                              SecurityScopes)
from passlib.context import CryptContext

from stores.schemas import (LoginBaseModel)
from stores.db import UserDBModel, session, Base, engine
from stores.schemas import (SignUpBaseModel, TokenData, Token)

AUTH = APIRouter(prefix="/auth", tags=["authentication"])

SECRET_KEY = "nsUSNJKjiusvajnkksoid7627UHWNS8732YBENW90S"
ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"], 
    deprecated="auto"
)

outh2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login", 
    scopes={
        "user": "Read information about the current user.", 
        "items": "Read items",  
    }
)

def create_access_token(data: dict, expire_delta: timedelta):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.now(timezone.utc) + expire_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

@AUTH.post("/login")
async def loginPageView(user_input:Annotated[OAuth2PasswordRequestForm, 
                                       Depends()], 
                        response: Response):
    username = user_input.username
    password = user_input.password
    match_user = session.query(UserDBModel).filter_by(username=username).first()
    if not match_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Username doesn't exist, check your username again.")
    elif not  pwd_context.verify(password, match_user.hashed_pwd):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Incorrect password,  check your password.")
    user_dict = {
        "username": username, 
        "password": password, 
        "last_visited": datetime.now()
    }
    user_dict = LoginBaseModel(**user_dict)
    match_user.last_visit = user_dict.last_visit
    session.commit()
    access_token_expire = timedelta(minutes=30)
    access_token = create_access_token(data={
        "sub": user_dict.username, 
        "scope": " ".join(user_input.scopes)
    }, expire_delta=access_token_expire)
    token = Token(access_token=access_token, 
                  token_type="bearer")
    
    await asyncio.sleep(3)
    response.set_cookie(key="username", value=user_dict.username)
    return JSONResponse(
        content={
            "access_token": token.access_token, 
            "token_type": token.token_type
        }, 
        status_code=status.HTTP_200_OK
    )
        
@AUTH.post("/signup")
async def signUpPageView(form: Annotated[OAuth2PasswordRequestForm, Depends()])->Token:
    Base.metadata.create_all(bind=engine)
    username = form.username
    password = form.password
    match_username = session.query(UserDBModel)\
        .filter_by(username=username).first()
    if not match_username:
        hash_pwd = pwd_context.hash(password)
        user_dict = {
            "username": username, 
            "password": hash_pwd 
        }
        user_dict = SignUpBaseModel(**user_dict)
        user = UserDBModel(
            id=user_dict.user_id, 
            username=user_dict.username, 
            hashed_pwd=user_dict.password, 
            account_created=user_dict.account_created, 
            last_visit=user_dict.last_visit, 
            is_active=user_dict.is_active, 
            is_superuser=user_dict.is_superuser, 
            is_anonymous=user_dict.is_anonymous
        )
        await asyncio.sleep(3)
        session.add(user)
        session.commit()
        access_token = create_access_token(data={"sub": user_dict.username, 
                                                "scope": " ".join(form.scopes)}, 
                                           expire_delta=timedelta(minutes=30))
        token = Token(access_token=access_token, 
                      token_type="bearer")
        return JSONResponse(content={"access_token": token.access_token, 
                                     "token_type": token.token_type}, 
                            status_code=status.HTTP_201_CREATED)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Username exist, try another username.")
    
@AUTH.post("/logout")
def logoutPageView():
    return