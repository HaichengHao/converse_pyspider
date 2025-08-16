"""
@File    :01声明请求体.py
@Editor  : 百年
@Date    :2025/8/12 15:24 
"""

'''
当你需要将数据从客户端（例如，浏览器）发送到你的 API 时，你将它作为请求体发送。

请求体是客户端发送给你的 API 的数据。响应体是你的 API 发送给客户端的数据。

你的 API 几乎总是需要发送响应体。但客户端不一定总是需要发送请求体，有时它们只请求一个路径，可能带有一些查询参数，但不发送请求体。

要声明请求体，你可以使用 Pydantic 模型，并享受它们所有的强大功能和优势。
要发送请求体，你应该使用以下方法之一：POST（最常见）、PUT、DELETE 或 PATCH。

在规范中，使用 GET 请求发送请求体的行为是未定义的，但 FastAPI 支持这种做法，仅适用于非常复杂/极端的用例。

由于不鼓励这种做法，Swagger UI 的交互式文档在使用 GET 时不会显示请求体的文档，并且中间代理可能不支持它。
'''

import uvicorn

from fastapi import FastAPI
#step1:首先，你需要从 pydantic 导入 BaseModel
from pydantic import BaseModel

#step2:
# 然后，你将数据模型声明为一个继承自 BaseModel 的类。
# 所有属性都使用标准的 Python 类型
class Item(BaseModel):
    name:str
    description:str | None = None
    price: float
    tax:float | None = None

# important:例如，上面的模型声明了一个 JSON “object”（或 Python dict）类似这样
'''
{
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}
'''
app = FastAPI()
@app.post('/items/')
async def create_item(item:Item):
    return item

if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8099)

'''
结果¶
仅仅通过这个 Python 类型声明，FastAPI 将会

将请求体读取为 JSON。
转换相应的类型（如果需要）。
验证数据。
如果数据无效，它将返回一个清晰的错误，精确指出错误数据的位置和内容。
将接收到的数据提供给参数 item。
由于你在函数中将其声明为 Item 类型，你将获得所有属性及其类型的所有编辑器支持（补全等）。
为你的模型生成 JSON Schema 定义，如果对你的项目有意义，你也可以在任何其他地方使用它们。
这些模式将成为生成的 OpenAPI 模式的一部分，并被自动文档 UIs 使用。'''