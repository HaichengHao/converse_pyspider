# @Author    : 百年
# @FileName  :05嵌入单个请求体参数.py
# @DateTime  :2025/8/20 17:10
'''
假设您只有一个来自 Pydantic 模型 Item 的单个 item 请求体参数。

默认情况下，FastAPI 将直接期望其请求体。

但是，如果您希望它期望一个包含键 item 且其内部是模型内容的 JSON!!!!!，就像您声明额外请求体参数时那样，您可以使用特殊的 Body 参数 embed
item: Item = Body(embed=True)
'''
import uvicorn
from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item:Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

if __name__ == '__main__':
    uvicorn.run('05嵌入单个请求体参数:app',reload=True,log_level='debug',host='127.0.0.1',port=8099)


'''
如果是淡出的写了item:Item
那么请求体是这样的
{
    "name": "qqg",
    "description": "stwg",
    "price": 0.22,
    "tax": 0.87
  }
  
但是如果写的是item:Annotated[Item, Body(embed=True)]
那么请求体就是这样的
{
  "item": {
    "name": "qqg",
    "description": "stwg",
    "price": 0.22,
    "tax": 0.87
  }
}
'''

#summary:
'''
总结¶
您可以向路径操作函数添加多个请求体参数，即使一个请求只能有一个请求体。

但是 FastAPI 会处理它，在您的函数中为您提供正确的数据，并在路径操作中验证和记录正确的模式。

您还可以声明接收作为请求体一部分的单一值。

您可以指示 FastAPI 将请求体嵌入到一个键中，即使只声明了一个参数。'''