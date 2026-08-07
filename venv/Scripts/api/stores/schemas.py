from pydantic import BaseModel, Field


class LoginBaseModel(BaseModel):
    username: str | None = Field()
    password: str | None = Field()

class SignUpBaseModel(BaseModel):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
    scopes: list[str] = []