"""
@File    :01声明查询参数.py
@Editor  : 百年
@Date    :2025/8/16 19:31 
"""
'''
如果您有一组相关的查询参数，您可以创建一个 Pydantic 模型来声明它们。
这将允许您在多个地方重用模型，并且可以一次性为所有参数声明验证和元数据

使用 Pydantic 模型声明查询参数
在 Pydantic 模型中声明您需要的查询参数，然后将参数声明为 Query
'''

import uvicorn
from typing import Annotated,Literal

from fastapi import FastAPI,Query

from pydantic import BaseModel,Field

app = FastAPI()
# FastAPI 将从请求中的查询参数中提取每个字段的数据，并为您提供您定义的 Pydantic 模型。
class FilterParams(BaseModel):
    limit:int = Field(100,gt=0,le=100)
    offset:int = Field(0,ge=0)
    order_by:Literal['created_at','updated_at'] = "created_at"
    tags:list[str] = []

@app.get('/items/')
async def read_items(filter_query:Annotated[FilterParams,Query()]):
    return filter_query

if __name__ == '__main__':
    uvicorn.run('01声明查询参数:app',host='127.0.0.1',port=8090,reload=True,log_level='debug')

'''类似于把要查询的单独写一个类里头,然后就不需要在查询那里定义一大堆
http://127.0.0.1:8090/items/?limit=100&offset=2&order_by=updated_at&tags=1212adad
'''