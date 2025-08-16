"""
@File    :02查询参数列表_多个值.py
@Editor  : 百年
@Date    :2025/8/16 10:32 
"""
from typing import Annotated

from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = ["foo","bar"]): #指定默认值为["foo","bar"]
    # 您还可以直接使用 list 而不是 list[str] async def read_items(q: Annotated[list, Query()] = []):
    '''
    请记住，在这种情况下，FastAPI 不会检查列表的内容。

例如，list[int] 会检查（并记录）列表的内容是否为整数。但单独的 list 不会。
    '''
    query_items = {"q": q}
    return query_items

if __name__ == '__main__':
    uvicorn.run('02查询参数列表_多个值:app', reload=True, log_level='debug', host='127.0.0.1', port=8099)


# 然后，使用类似这样的 URL https://:8000/items/?q=foo&q=bar
# 您将在您的路径操作函数中，在函数参数 q 中，以 Python list 的形式接收多个 q 查询参数的值（foo 和 bar）。

# 因此，该 URL 的响应将是
'''
{
  "q": [
    "foo",
    "bar"
  ]
}'''

# 如果您访问 https://:8000/items/
# q 的默认值将是：["foo", "bar"]，您的响应将是
'''
{
  "q": [
    "foo",
    "bar"
  ]
}'''