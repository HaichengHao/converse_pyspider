"""
@File    :03模型嵌套与自定义规则.py
@Editor  : 百年
@Date    :2025/8/14 16:24 
"""
from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
import uvicorn
from typing import List


class Addr(BaseModel):
    province: str
    city: str


class User(BaseModel):
    name: str
    age: int = Field(default=1, gt=0, lt=100)
    addr: Addr

    @field_validator("name")
    def name_must_alpha(cls, value):
        assert value.isalpha()
        return value

class Data(BaseModel):
    data:List[User]

app = FastAPI()
@app.post('/user',description='用户信息')
async def getdata(user:User):
    return user

@app.post('/data')
async def data(data:Data):
    return data

if __name__ == '__main__':
    uvicorn.run('03模型嵌套与自定义规则:app',host='127.0.0.1',port=8090,reload=True,log_level='debug')