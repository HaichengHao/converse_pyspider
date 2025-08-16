"""
@File    :app01.py
@Editor  : 百年
@Date    :2025/8/14 8:54 
"""
from fastapi import APIRouter

app1 = APIRouter()

@app1.get('/user/{userid}')
async def get_user(userid:int|None=None):
    return {'user_id':userid}

@app1.get('/article/{id}')
async def get_article(id:int):
    return {"article_id":id}