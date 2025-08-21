# @Author    : 百年
# @FileName  :02禁止额外查询参数.py
# @DateTime  :2025/8/17 14:24

'''
禁止额外查询参数
在某些特殊用例中（可能不常见），您可能希望限制要接收的查询参数。

您可以使用 Pydantic 的模型配置来 forbid 任何 extra 字段
'''

import uvicorn
from typing import Annotated,Literal
from fastapi import FastAPI,Query
from pydantic import BaseModel,Field

app = FastAPI()

class FilterParams(BaseModel): #可以看看源码,
    '''model_config: ClassVar[ConfigDict] = ConfigDict()所以要传入的是一个配置字典'''
    model_config = {'extra':'forbid'}
    limit:int = Field(100,gt=0,le=100)
    offset:int = Field(0,ge=0)
    order_by:Literal['created_at','updated_at'] = 'created_at'
    tags:list[str]=[]

@app.get('/items/')
async def read_items(filter_query:Annotated[FilterParams,Query()]):
    return filter_query

if __name__ == '__main__':
    uvicorn.run('02禁止额外查询参数:app',log_level='debug',reload=True,host='127.0.0.1',port=8099)

'''
如果客户端尝试在查询参数中发送一些额外数据，他们将收到一个错误响应。

例如，如果客户端尝试发送一个 tool 查询参数，其值为 plumbus，例如
https://example.com/items/?limit=10&tool=plumbus
他们将收到一个错误响应，告诉他们查询参数 tool 不被允许

{
    "detail": [
        {
            "type": "extra_forbidden",
            "loc": ["query", "tool"],
            "msg": "Extra inputs are not permitted",
            "input": "plumbus"
        }
    ]
}
'''