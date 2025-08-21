# @Author    : 百年
# @FileName  :01Field的使用.py
# @DateTime  :2025/8/20 18:07

'''
就像你可以使用 Query、Path 和 Body 在路径操作函数参数中声明额外的验证和元数据一样，
你也可以使用 Pydantic 的 Field 在 Pydantic 模型!!!内部声明验证和元数据。
'''
# important:注意,field是在pydantic模型中用的，Q\P\B是在路径参数中用的

from typing import Annotated
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None,
        title='the description of the item',
        max_length=300
    )
    price: float = Field(
        gt=0,
        description='价格必须大于0'
    )
    tax: str | None = None
