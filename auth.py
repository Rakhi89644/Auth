from fastapi import FastAPI
from sqlalchemy.orm import Session
from . import models,schemas
from fastapi.security import OAuth2PasswordBearer 
from jose import JOSEError,jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime,timedelta
from typing import Optional
from .database import SessionLocal,engine

models.Base.metadata.create_all(bind=engine)
 
app=FastAPI()

#dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#D


SECRET_KEY='97db4c6bfacbea379aa433c726dc20670460a6326950140dfc101bb139387b5d'
ALGORITHUM= "HS256"

pwd_context = CryptContext(schemes=['bcrypt'],deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
 
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)\


def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db,username:str):
    return db.query(models.User).filter(models.User.username == username)

def create_user(db:Session,user:schemas.UserCreate):
    db.user = models.User(username=user.username,hashed_password=get_password_hash(user.password))
    db.add(db.user)
    db.commit()
    db.refresh(db.user)

def authenticate_user(fake_db,username:str,password:str):
    user = get_user(fake_db,username)
    if not user:
        return False
    if not verify_password(password,user.hashed_password):
        return False
    return user