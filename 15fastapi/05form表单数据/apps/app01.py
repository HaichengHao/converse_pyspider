"""
@File    :app01.py
@Editor  : 百年
@Date    :2025/8/14 21:13 
"""

import uvicorn
# important:需要引入Form对象
from fastapi import FastAPI,Form
from pydantic import field_validator,Field
from typing import List

app = FastAPI(docs_url=None,redoc_url=None)

@app.post('/regin',summary='地区信息')
async def data(username:str=Form(),password:str=Form()):
    print(f'username:{username},password:{password}')
    return {
        'username':username
    }