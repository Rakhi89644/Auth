import imp
from lib2to3.pgen2.token import COLONEQUAL
from secrets import token_bytes
from turtle import st
from typing import List,Optional

from pydantic import BaseModel

class Toke(BaseModel):
    access_token: str
    token_type: str

class TokenDate(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str
    is_active: Optional[bool] = None

class UserINDB(User):
    hashed_password: str
class UserCreate(User):
    password: str