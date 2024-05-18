from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class Message(BaseModel):
    message: str