"""
@File    :05请求体路径参数查询参数.py
@Editor  : 百年
@Date    :2025/8/15 22:50 
"""
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {'item_id': item_id, **item.dict()}
    if q:
        result.update({'q': q})
    return result


if __name__ == '__main__':
    uvicorn.run('05请求体路径参数查询参数:app', reload=True, log_level='debug', host='127.0.0.1', port=8099)
