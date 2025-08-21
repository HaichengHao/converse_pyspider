# @Author    : 百年
# @FileName  :04多个请求体参数和多个查询参数.py
# @DateTime  :2025/8/20 16:45

'''
多个请求体参数和查询参数
当然，您还可以根据需要声明额外的查询参数，除了任何请求体参数之外。

因为，默认情况下，单一值被解释为查询参数，所以您不必显式添加 Query，您可以直接
'''

import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None


@app.put('/items/{item_id}')
async def update_item(
        *,
        item_id: int,
        item: Item,
        user: User,
        importance: Annotated[int, Body(gt=0)],
        q: str | None = None,
):
    results={
        'item_id':item_id,
        'item':item,
        'user':user,
        'importance':importance
    }
    if q:
        results.update({"q":q})
    return results

if __name__ == '__main__':
    uvicorn.run('04多个请求体参数和多个查询参数:app',reload=True,host='127.0.0.1',port=8099,log_level='debug')
