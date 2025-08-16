"""
@File    :01快速开始.py
@Editor  : 百年
@Date    :2025/8/13 21:36 
"""
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def home():
    return {"message": 'hello from fastapi'}


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8099)
