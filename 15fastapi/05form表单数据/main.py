"""
@File    :main.py
@Editor  : 百年
@Date    :2025/8/14 21:17 
"""
from apps.app01 import app
import uvicorn

if __name__ == '__main__':

    uvicorn.run(app,host='127.0.0.1',port=8088)
