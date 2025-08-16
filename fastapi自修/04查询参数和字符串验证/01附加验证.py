"""
@File    :01附加验证.py
@Editor  : 百年
@Date    :2025/8/15 23:10 
"""


# 我们将强制规定，即使 q 是可选的，一旦提供，其长度不能超过 50 个字符。

#导入Query和Annotated
'''
Query 来自 fastapi
Annotated 来自 typing
'''

import uvicorn
from fastapi import FastAPI,Query
from typing import Annotated

app = FastAPI()

@app.get('/items/')

#tips:现在我们有了这个可以放置更多信息（在本例中是一些附加验证）的 Annotated，将 Query 添加到 Annotated 内部，并将参数 max_length 设置为 50
async def read_items(q:Annotated[str | None,Query(min_length=3,max_length=50,pattern="^fixedquery$")]=None):
    result = {
        'items':[{'item_id':'foo'},{'item_id':'Bar'}]
    }
    if q:
        result.update({'q':q})
    return result

if __name__ == '__main__':
    uvicorn.run('01附加验证:app', reload=True, log_level='debug', host='127.0.0.1', port=8099)
