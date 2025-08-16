"""
@File    :03响应模型编码参数.py
@Editor  : 百年
@Date    :2025/8/15 16:23 
"""
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include=["name", "description"],
    #tips:设置返回模型的包含值,有就返回,没有的就返回空
    #     response_model_include 指定要包含的值
)
async def read_item_name(item_id: str):
    return items[item_id]



#tips: response_model_exclude_unset=True 意为排除未设置的值,True为排除,False为不排除,设置为True就是显示所有 有的 没有的一律不显示
# response_model_exclude_defaults 去除掉有默认值的,但是如果写入了值,那就返回
# response_model_exclude_none 排除为None的值,但是有就返回
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True,\
         response_model_exclude_defaults=True,response_model_exclude_none=True)
async def read_item(item_id: str):
    return items[item_id]

# tips:设置排除的值,比上面的温和,仅仅排除掉tax,有tax就返回,没有就排除 不显示
#  response_model_exclude 指定要排除的值
@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]