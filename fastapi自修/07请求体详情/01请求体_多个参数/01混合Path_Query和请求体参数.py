# @Author    : 百年
# @FileName  :01混合Path_Query和请求体参数.py
# @DateTime  :2025/8/17 15:55

import uvicorn

from typing import Annotated

from fastapi import FastAPI,Path

from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description:str|None=None
    price:float
    tax:float|None = None

@app.put('/items/{item_id}')
async def update_item(
        item_id:Annotated[int,Path(title="The ID of the item to get",ge=0,le=1000)],
        q:str|None=None,
        item:Item|None=None
):
    '''
    请注意，在这种情况下，将从请求体中获取的 item 是可选的。因为它有一个 None 默认值。
    '''
    results={
        'item_id':item_id
    }
    if q:
        results.update({'q':q})
    if item:
        results.update({'item':item})
    return results
if __name__ == '__main__':
    uvicorn.run('01混合Path_Query和请求体参数:app',log_level='debug',reload=True,host='127.0.0.1',port=8099)
