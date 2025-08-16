"""
@File    :urls.py
@Editor  : 百年
@Date    :2025/8/14 15:19 
"""
from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import List

user = APIRouter(prefix='/user')

class Addr(BaseModel):
    province:str
    city:str

class User(BaseModel):
    # name: str = Field(pattern="^a")  # 使用正则表达式约束输入
    name:str
    age: int = Field(default=0, gt=0, lt=100)
    birth: date | None
    friends: List[int]
    addr:Addr #important:这里使用了类型嵌套
    # 自定义验证规则
    @field_validator("name")
    def name_must_alpha(cls, value):
        assert value.isalpha(), "name must be alpha"  # important:使用断言,value必须是字母,如果不是就输出后面的name must be alpha
        return value

@user.post('/data', description="用户信息", response_description="返回用户的信息")
async def data(user: User):
    print(user, type(user))
    # name='小王' age=12 birth=datetime.date(2025, 8, 14) friends=[1, 2, 3] <class 'apps.app01.urls.User'>
    print(user.dict())  # 通过.dict方法可以将已经拿到的数据转换为一个字典
    return user