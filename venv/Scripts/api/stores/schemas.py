import uuid

from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl


class SignUpBaseModel(BaseModel):
    user_id: uuid.UUID = uuid.uuid4()
    username: str
    # PLAIN PASSWORD
    password: str
    account_created: datetime = datetime.now()
    last_visit: datetime = datetime.now()
    is_active: bool = True
    is_superuser: bool = False
    is_anonymous: bool = False

class LoginBaseModel(BaseModel):
    username: str
    password: str 
    last_visit: datetime = datetime.now()

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str
    scopes: list[str] = []
    
class ImagePost(BaseModel):
    filename: str
    content_type: str
    file_size: int
    caption: str 

class VideoPost:
    pass

class MusicPost:
    pass

class TextPost:
    pass