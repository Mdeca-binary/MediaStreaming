from typing import Annotated

from fastapi import (APIRouter, 
                     Form, Depends)
from fastapi.security import (OAuth2PasswordBearer, 
                              OAuth2PasswordRequestForm)

from passlib.context import CryptContext

from stores.schemas import (LoginBaseModel)

AUTH = APIRouter(prefix="/auth", tags=["authentication"])

cryptContext = CryptContext()

outh2_scheme = OAuth2PasswordBearer(
    tokenUrl="login", 
    scopes={
        "user": "Read information about the current user.", 
        "items": "Read items", 
    }
)

@AUTH.post("/login")
def loginPageView(user_input:Annotated[OAuth2PasswordRequestForm, 
                                       Depends()]):
    username = user_input.username
    password = user_input.password
    decrypt_pwd = cryptContext.verify(password, "")
    pass 

@AUTH.post("/signup")
def signUpPageView():
    return

@AUTH.post("/logout")
def logoutPageView():
    return