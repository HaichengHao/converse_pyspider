"""
@File    :02使用模型.py
@Editor  : 百年
@Date    :2025/8/14 15:07 
"""
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel,Field

class Item(BaseModel):
    name:str
    age: int = Field(default=0,gt=0,lt=100) #范围约束
    description:str|None = None
    price: float
    tax:float | None = None


app = FastAPI()

# tips:在函数内部，你可以直接访问模型对象的所有属性
@app.post('/items/')
async def getitem(item:Item):
    #获取模型的字典
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        price_with_tax = round(price_with_tax,2)
        item_dict.update({'price_with_tax':price_with_tax})
    return item_dict


if __name__ == '__main__':
    uvicorn.run("02使用模型:app",reload=True,host='127.0.0.1',port=8099,log_level='debug')