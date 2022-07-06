import email
from http.client import HTTPException
from os import access
from fastapi import Depends, FastAPI,HTTPException,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List
from fastapi_jwt_auth import AuthJWT
from pydantic.networks import url_regex

app=FastAPI()

class Settings(BaseModel):
    authjwt_secret_key:str = '5fd6ba2ca1b5f697c15e2ec835f9236f7286bf6268a05088be4eec592d284ba6'

@AuthJWT.load.Config
def get_config():
    return Settings()

class User(BaseModel):
    username:str
    email:str
    password:str

    class Config:
        schema_extra={
            "example":{
                "username":"rakhi kumari",
                "email":"krakhi0401@gmail.com",
                "password":"password"
            }
        }

class UserLogin(BaseModel):
    username:str
    password:str

    class Config:
        schema_extra={
            "example":{
                "username":"rakhi kumari",
                "email":"krakhi0401@gmail.com",
                "password":"password"
            }

    }

users=[]

@app.get('/')
def index():
    return{"hello":"Rakhi"}
#creating user
@app.post('/signup',status_code=201)
def create_user(user:User):
    new_user={
        "username":user.username,
        "email":user.email,
        "password":user.password
    }

    #users.append(new_user)
    return new_user
#getting all user
@app.get('/users',response_model=List[User])
def get_users():
    return users

@app.post('/login')
def login(user:UserLogin,Authorize:AuthJWT=Depends()):
    for u in users:
        if (u["username"]==user.username) and (u["password"]==user.password):
            return url_regex

        raise HTTPException(status_code='401',detail="Invalid username and password")

@app.get('/protected')
def get_logged_in_user(Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid token')

        current_user=Authorize.get_jwt_subject()

        return {"current_user":current_user}


