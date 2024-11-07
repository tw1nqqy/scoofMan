from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    disabled: bool | None = None


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
