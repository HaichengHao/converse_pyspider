"""
@File    :01初体验.py
@Editor  : 百年
@Date    :2025/8/16 16:55 
"""

'''
与使用 Query 为查询参数声明更多验证和元数据的方式相同，
你也可以使用 Path 为路径参数声明相同类型的验证和元数据。'''

from typing import Annotated
from fastapi import FastAPI, Query, Path

app = FastAPI()

'''
路径参数总是必需的，因为它必须是路径的一部分。
即使你将其声明为 None 或设置了默认值，它也不会产生任何影响，它仍然始终是必需的。'''
@app.get('/items/{item_id}')
async def read_items(
        item_id: Annotated[int, Path(title='The ID of the item to get')],
        q: Annotated[str | None, Query(alias='item-query')] = None
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results
