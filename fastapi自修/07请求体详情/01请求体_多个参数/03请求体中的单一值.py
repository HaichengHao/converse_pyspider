# @Author    : 百年
# @FileName  :03请求体中的单一值.py
# @DateTime  :2025/8/17 16:33

'''
请求体中的单一值¶
与通过 Query 和 Path 为查询参数和路径参数定义额外数据的方式相同，FastAPI 提供了一个等效的 Body。

例如，扩展前面的模型，您可以决定在同一个请求体中，除了 item 和 user 之外，再添加一个键 importance。

如果您按原样声明它，因为它是一个单一值，FastAPI 将假定它是一个查询参数。

但是您可以使用 Body 指示 FastAPI 将其视为另一个请求体键

'''

import uvicorn
from typing import Annotated
from fastapi import Body,FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description:str|None=None
    price:float
    tax:float|None =None

class User(BaseModel):
    username:str
    full_name:str|None = None

@app.put('/items/{item_id}')
async def update_item(
        item_id:int,
        item:Item,
        user:User,
        importance:Annotated[int,Body()]
):
    results={
        'item_id':item_id,
        'item':item,
        'user':user,
        'importance':importance
    }
    return results

if __name__ == '__main__':
    uvicorn.run('03请求体中的单一值:app',log_level='debug',host='127.0.0.1',port=8099,reload=True)
