from pydantic import BaseModel
from typing import Optional
from datetime import date

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

class CalorieLogBase(BaseModel):
    date: date
    food_item: str
    calories: float

class CalorieLogCreate(CalorieLogBase):
    pass

class CalorieLog(CalorieLogBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
