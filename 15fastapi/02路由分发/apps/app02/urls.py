"""
@File    :urls.py
@Editor  : 百年
@Date    :2025/8/14 8:17 
"""
from fastapi import APIRouter
user = APIRouter(tags=['用户中心'])

@user.get('/user/login',tags=['用户登录'])
async def user_log():
    return {'user':'login'}

@user.get('/user/reg',tags=['用户注册'],summary='对的,就是让注册的',response_description='注册成功就返回')
async def user_reg():
    return {'user':'reg'}