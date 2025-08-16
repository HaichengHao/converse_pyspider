"""
@File    :03查询参数.py
@Editor  : 百年
@Date    :2025/8/12 10:04 
"""
import uvicorn
from fastapi import FastAPI
app = FastAPI()
fake_items_db = [{'item_name':'Foo'},{'item_name':'Bar'},{'item_name':'Baz'}]
@app.get('/items/')
async def read_item(skip:int = 0,limit:int = 10):
    return fake_items_db[skip:skip+limit]
'''
查询参数是 URL 中 ? 之后，用 & 字符分隔的键值对集合。
例如，在 URL 中
http://127.0.0.1:8000/items/?skip=0&limit=10'''

# 可选参数¶
# 同样地，你可以通过将默认值设置为 None 来声明可选查询参数
@app.get("/items/{item_id}")
async def read_item(item_id:str,q:str|None = None): #也可以这样async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id":item_id,"q":q}
    return {"item_id":item_id}



if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8099)

