"""
@File    :model.py
@Editor  : 百年
@Date    :2025/8/6 21:27 
"""
import datetime

from ..extensions import db
from sqlalchemy import text


class User(db.Model):
    __tablename__ = 'user'  # 可选,指定表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), unique=True, nullable=False)  # 设置不允许为空 即not null
    password = db.Column(db.String(12), unique=True, nullable=False)
    phone = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(20))
    register_time = db.Column(db.DateTime, default=datetime.time)  # 获取注册时间

    def __str__(self):
        return self.username

class UserInfo(db.Model):
    __tablename__='userinfo'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    realname = db.Column(db.String(20))
    gender = db.Column(db.Boolean,default=False)

    def __str__(self):
        return self.id
