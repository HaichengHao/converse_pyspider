"""
@File    :04请求体与路径参数同时声明.py
@Editor  : 百年
@Date    :2025/8/15 22:42 
"""

'''
你可以同时声明路径参数和请求体。

FastAPI 将识别函数参数中与路径参数匹配的参数应从路径中获取，
而声明为 Pydantic 模型的函数参数应从请求体中获取。'''

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {'item_id': item_id, **item.dict()}

if __name__ == '__main__':
    uvicorn.run('04请求体与路径参数同时声明:app',reload=True,host='127.0.0.1',port=8099,log_level='debug')