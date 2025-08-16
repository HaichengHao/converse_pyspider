"""
@File    :02返回类型与数据过滤.py
@Editor  : 百年
@Date    :2025/8/15 16:06 
"""



from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
import uvicorn
from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    name: str
    email: EmailStr
    fullname: str | None = None


class UserIn(BaseModel):
    password: str


app = FastAPI()

@app.post('/reg')
async def regis(user: UserIn):
    return user


if __name__ == '__main__':
    uvicorn.run('02返回类型与数据过滤:app', host='127.0.0.1', port=8099, reload=True, log_level='debug')

'''
先让我们看看编辑器、mypy 和其他工具会如何看待这一点。

BaseUser 包含基础字段。然后 UserIn 继承自 BaseUser 并添加了 password 字段，因此它将包含两个模型的所有字段。

我们将函数返回类型注解为 BaseUser，但我们实际上返回的是一个 UserIn 实例。

编辑器、mypy 和其他工具不会对此抱怨，因为在类型方面，UserIn 是 BaseUser 的子类，这意味着当预期是任何 BaseUser 类型时，它是一个 *有效* 类型。

FastAPI 数据过滤¶
现在，对于 FastAPI，它将查看返回类型并确保你返回的内容**只**包含该类型中声明的字段。

FastAPI 在内部与 Pydantic 协同完成多项工作，以确保类继承的那些规则不被用于返回数据过滤，否则你最终可能会返回比预期多得多的数据。

通过这种方式，你可以两全其美：既有带**工具支持**的类型注解，又有**数据过滤**。'''