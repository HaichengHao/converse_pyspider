"""
@File    :app.py
@Editor  : 百年
@Date    :2025/8/15 8:57 
"""
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get('/')
async def getdemo(request:Request):
    print(request.url)
    print(request.client.host)
    print(request.client.port)
    return {
        '请求链接':request.url,
        '客户端宿主':request.client.host,
        '客户端端口':request.client.port,
        '请求头':request.headers,
        'UA':request.headers.get("user-agent"),
        'cookies':request.cookies #cookies用接口文档是测试不出来的,需要我们使用postman来测试
    }

if __name__ == '__main__':
    uvicorn.run('app:app', reload=True, host='127.0.0.1', port=8099)
