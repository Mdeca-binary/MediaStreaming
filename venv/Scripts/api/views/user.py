import jwt
from jwt.exceptions import InvalidTokenError
from typing import Annotated

from fastapi import (APIRouter, Security, 
                     Depends, HTTPException, status)
from fastapi.security import (SecurityScopes)

from views.auth import outh2_scheme, SECRET_KEY, ALGORITHM
from stores.schemas import TokenData, LoginBaseModel, SignUpBaseModel
from stores.db import session, UserDBModel

USER_PROFILE = APIRouter(
    prefix="/profile", 
    tags=["Profile"]
)

def get_user(username: str):
    
    user = session.query(UserDBModel).filter_by(username=username).first()
    if user:
        user_dict = {
            "username": user.username, 
            "password": user.hashed_pwd
        }
        return SignUpBaseModel(**user_dict)


async def get_current_user(
    security_scopes: SecurityScopes, 
    token: Annotated[str, Depends(outh2_scheme)]):
    if security_scopes.scopes:
        authenticate_value = f"Bearer scope={security_scopes.scope_str}"
    else:
        authenticate_value = "Bearer"
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                         detail="Could not validate credentials", 
                                         headers={"WWW-Authenticate": authenticate_value})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credential_exception
        scope: str = payload.get("scope", "")
        token_scopes = scope.split(" ")
        token_data = TokenData(scopes=token_scopes, username=username)
    except (InvalidTokenError, ValueError):
        raise credential_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credential_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Not enough permissions", 
                headers={"WWW-Authenticate": authenticate_value}, 
            )
    return user

async def get_current_active_user(
    current_user: Annotated[SignUpBaseModel, 
                            Security(get_current_user, scopes=["items"])]):
    if current_user.is_active != True:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Inactive user.")
    return current_user
        

@USER_PROFILE.get("/user/")
async def profilePageView(user:Annotated[SignUpBaseModel, 
                                         Depends(get_current_active_user)]) -> SignUpBaseModel:
    return user