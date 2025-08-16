"""
@File    :__init__.py.py
@Editor  : 百年
@Date    :2025/8/14 8:07 
"""
from fastapi import FastAPI
from .app01.urls import shop
from .app02.urls import user

app = FastAPI()

app.include_router(user)
app.include_router(shop)


def create_app():
    return app