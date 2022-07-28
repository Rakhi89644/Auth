import imp
from fastapi import FastAPI
from typing import List,Union

from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


class user(BaseModel):
    id: int
    title: str
    url: Union[str,None]
    thumbnailUrl: str


app=FastAPI()
@app.post('/user',response_model=user)
async def example(User:user):
    jsonable_encoder_user = jsonable_encoder(user)

    return JSONResponse(content=jsonable_encoder_user)