"""
@File    :03必须查询参数.py
@Editor  : 百年
@Date    :2025/8/12 11:23 
"""

'''
必需查询参数
当你为非路径参数（目前我们只看到查询参数）声明默认值时，它不是必需的。

如果你不想添加特定值但又想让它可选，请将默认值设置为 None。

但当你想让一个查询参数成为必需时，你可以不声明任何默认值
'''

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/items/{item_id}')
async def read_user_item(item_id:str,needy:str):
    item = {"item_id":item_id,"needy":needy}
    return item
# 这里查询参数 needy 是一个必需的 str 类型查询参数。


# 如果你在浏览器中打开一个类似这样的 URL
# http://127.0.0.1:8000/items/foo-item
# 而没有添加必需参数 needy，你将看到一个类似以下的错误
'''
{
  "detail": [
    {
      "type": "missing",
      "loc": [
        "query",
        "needy"
      ],
      "msg": "Field required",
      "input": null,
      "url": "https://errors.pydantic.dev/2.1/v/missing"
    }
  ]
}'''

# 由于 needy 是必需参数，你需要在 URL 中设置它
# http://127.0.0.1:8099/items/1212?needy=1212
# {"item_id":"1212","needy":"1212"}


# 当然，你可以定义一些参数为必需的，一些有默认值，一些完全可选
@app.get('/items/{itemnum}')
async def read_user_itemnum(
        itemnum:str,needy:str,skip:int=0,limit:int|None=None,
):
    item = {
        'itemnum':itemnum,
        'needy':needy,
        'skip':skip,
        'limit':limit
    }
    return item
if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8099)