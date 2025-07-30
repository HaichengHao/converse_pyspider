"""
@File    :01demo.py
@Editor  : 百年
@Date    :2025/7/30 19:22 
"""

from fastapi import FastAPI

app = FastAPI()

dic={
    'a':'北京',
    'b':'上海'
}
@app.get('/')
async def root():
    return '你好'


@app.get('/items/{item_id}')
async def read_item(item_id):
    return {'item_id':item_id}


#就像flask的路由的变量规则一样
@app.get('/getv/{k}')
async def getdic(k):
    return dic.get(k)





