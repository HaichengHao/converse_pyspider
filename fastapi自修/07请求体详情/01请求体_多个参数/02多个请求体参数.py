# @Author    : 百年
# @FileName  :02多个请求体参数.py
# @DateTime  :2025/8/17 16:12

'''
在前面的例子中，路径操作 会期望一个 JSON 请求体，包含一个 Item 的属性，例如
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
'''
import uvicorn

from fastapi import FastAPI,Query,Path

from pydantic import BaseModel

app = FastAPI()
class Item(BaseModel):
    name:str
    description:str|None = None
    price:float
    tax:float|None=None
class User(BaseModel):
    username:str
    full_name:str|None=None

@app.put('/items/{item_id}')
async def update_item(item_id:int,item:Item,user:User):
    '''

    在这种情况下，FastAPI 会注意到函数中有多个请求体参数（有两个参数是 Pydantic 模型）。

因此，它会使用参数名作为请求体中的键（字段名），并期望一个像这样的请求体
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
请注意，即使 item 的声明方式与之前相同，但现在它被期望在请求体中以键 item 出现。
FastAPI 将对请求进行自动转换，以便参数 item 接收其特定内容，user 也是如此。

它将执行复合数据的验证，并为 OpenAPI 模式和自动文档进行相应的文档化。
    '''
    result = {
        'item_id':item_id,
        'item':item,
        'user':user
    }
    return result
if __name__ == '__main__':

    uvicorn.run('02多个请求体参数:app',log_level='debug',reload=True,host='127.0.0.1',port=8099)
