# @Author    : 百年
# @FileName  :04pydantic模型.py
# @DateTime  :2025/8/20 22:42
'''
Pydantic 是一个用于执行数据验证的 Python 库。

您将数据的“形状”声明为带有属性的类。

每个属性都有一个类型。

然后，您使用一些值创建该类的一个实例，它将验证这些值，将它们转换为适当的类型（如果适用），并为您提供一个包含所有数据的对象。

通过该结果对象，您将获得所有的编辑器支持。
'''
from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123
