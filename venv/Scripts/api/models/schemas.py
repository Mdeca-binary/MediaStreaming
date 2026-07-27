import uuid

from datetime import datetime

from pydantic import BaseModel


class UserBaseMode(BaseModel):
    id: uuid
    username: str
    hashed_pwd: str
    account_created: datetime
    update_visit: datetime
    is_active: bool
    is_superuser: bool
    is_anonymous: bool 