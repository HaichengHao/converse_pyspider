"""
@File    :app.py
@Editor  : 百年
@Date    :2025/8/15 9:50 
"""

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
import uvicorn
from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    name: str
    password: str
    email: EmailStr
    fullname: str | None = None


class UserOut(BaseModel):
    name: str
    email: EmailStr


app = FastAPI()


# important:这里我们设置响应模型的参数,指定为UserOut类,这样我们返回的对象就是只有name和email而不会把密码一并返回
@app.post('/reg', response_model=UserOut)
async def regis(user: UserIn):
    return user


if __name__ == '__main__':
    uvicorn.run('01响应模型:app', host='127.0.0.1', port=8099, reload=True, log_level='debug')
