"""
@File    :main.py
@Editor  : 百年
@Date    :2025/8/14 21:44 
"""
import uvicorn
from fastapi import FastAPI
from apps.app1 import filedemo
app = FastAPI(description="上传文件用的")

app.include_router(filedemo)

if __name__ == '__main__':
    uvicorn.run("main:app",reload=True,host='127.0.0.1',port=8099,log_level="debug")