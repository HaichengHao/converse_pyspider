"""
@File    :__init__.py.py
@Editor  : 百年
@Date    :2025/8/14 15:19 
"""
from .app01.urls import user

from fastapi import FastAPI



def create_app():
    app = FastAPI()
    app.include_router(user)

    return app