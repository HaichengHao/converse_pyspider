"""
@File    :05从OpenApi中排除参数.py
@Editor  : 百年
@Date    :2025/8/16 10:59 
"""

'''
从 OpenAPI 中排除参数¶
要将查询参数从生成的 OpenAPI schema（以及自动文档系统）中排除，请将 Query 的参数 include_in_schema 设置为 False'''

import uvicorn
from typing import Annotated
from fastapi import FastAPI,Query

app = FastAPI()

@app.get('/items/')
async def get_items(hidden_query:Annotated[str|None,Query(include_in_schema=False)]=None):
    if hidden_query:
        return {"hidden_query":hidden_query}
    return {"hidden_query":"not found"}


if __name__ == '__main__':
    uvicorn.run('05从OpenApi中排除参数:app', reload=True, log_level='debug', host='127.0.0.1', port=8099)
