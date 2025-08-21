"""
@File    :04别名参数.py
@Editor  : 百年
@Date    :2025/8/16 10:42 
"""
'''
假设您希望参数名为 item-query。

例如

http://127.0.0.1:8000/items/?item-query=foobaritems
'''

import uvicorn
from typing import Annotated
from fastapi import FastAPI,Query

app = FastAPI()


@app.get('/items/',deprecated=True) #这里也可以设置参数过期
#tips：这里设置了别名参数alias
# 废弃参数¶
# 现在假设您不再喜欢这个参数了。
# 您必须让它在那里保留一段时间，因为有客户端正在使用它，但您希望文档清晰地将其显示为已废弃。
# 然后将参数 deprecated=True 传递给 Query
# 声明了别名之后,api的输入框中会有自己写的alias的字段,可以看看docs显示的内容
async def read_items(q:Annotated[str|None,Query(alias="item-query" ,deprecated=True)]=None):
    results={"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update(
            {'q':q}
        )
    return results


if __name__ == '__main__':
    uvicorn.run('04别名参数:app', reload=True, log_level='debug', host='127.0.0.1', port=8099)

