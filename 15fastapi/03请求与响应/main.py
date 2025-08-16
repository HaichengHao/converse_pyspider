"""
@File    :main.py
@Editor  : 百年
@Date    :2025/8/14 8:54 
"""
import uvicorn
from apps.app01 import app1
from fastapi import FastAPI

app = FastAPI()

app.include_router(app1,prefix='/shop',tags=['购物中心入口'])

if __name__ == '__main__':

    uvicorn.run('main:app',host='127.0.0.1',port=8099,reload=True,log_level='debug')