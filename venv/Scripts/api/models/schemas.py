import uuid

from typing import Optional

from datetime import datetime, timezone

from pydantic import BaseModel, Field


class UserBaseMode(BaseModel):
    user_id: Optional[uuid.UUID] = uuid.uuid4()
    username: str
    hashed_pwd: str
    account_created: datetime = datetime.now()
    update_visit: datetime = datetime.now()
    is_active: bool = True
    is_superuser: bool = False
    is_anonymous: bool = False

class UserLogin(BaseModel):
    username: str
    password: str 
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
    
class TokenData(BaseModel):
    username: str | None = None
    scopes: list[str] = []