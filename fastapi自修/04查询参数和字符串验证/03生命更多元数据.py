"""
@File    :03生命更多元数据.py
@Editor  : 百年
@Date    :2025/8/16 15:59 
"""
'''
您可以添加更多关于参数的信息。

该信息将包含在生成的 OpenAPI 中，并由文档用户界面和外部工具使用。

'''


#tips:可以添加title以及 description
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[str | None, Query(
        title="Query string",
        min_length=3,
        description="Query string for the items to search in the database that have a good match"
        )] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results