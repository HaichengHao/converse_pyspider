"""
@File    :02路径参数.py
@Editor  : 百年
@Date    :2025/7/30 20:38 
"""
from fastapi import FastAPI,templating

app = FastAPI()

@app.get('/items/{item_id}') #tips:在这种情况下，item_id 被声明为 int 类型。
async def getid(item_id: int):
    return {'item_id':item_id}
