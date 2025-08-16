"""
@File    :04多路径查询参数.py
@Editor  : 百年
@Date    :2025/8/12 10:58 
"""
'''
多路径和查询参数¶
你可以同时声明多个路径参数和查询参数，FastAPI 知道哪个是哪个。

并且你不需要以任何特定顺序声明它们。

它们将按名称检测
'''
import uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(
        user_id:int,item_id:str,q:str|None=None,short:bool=False
):
    item={'item_id':item_id,"owner_id":user_id}
    if q:
        item.update({'q':q}) #如果为真就往字典中新增数据'q':q
    if not short: #如果short为真
        item.update(
            {'description':'this is an amazing item that has long description'}
        )
    return item

if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8099)
