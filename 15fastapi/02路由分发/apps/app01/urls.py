"""
@File    :urls.py
@Editor  : 百年
@Date    :2025/8/14 8:11 
"""
# 其实路由分发的操作很像flask中蓝图的操作
from fastapi import APIRouter
shop = APIRouter(prefix='/shop',tags=['shop的实现'])

@shop.get('/food',tags=['卖食品'],summary='seveneleven')
async def shop_food():
    return {'shop':'food'}

@shop.get('/bed',tags=['卖个床'])
async def shop_food():
    return {'food':'bed'}