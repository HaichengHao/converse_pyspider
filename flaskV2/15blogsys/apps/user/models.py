"""
@File    :model.py
@Editor  : 百年
@Date    :2025/8/10 9:13 
"""
from .extensions import db
from datetime import datetime
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(64),nullable=False) #要放的是要加密的密码,所以大小应当是加密之后的大小,故db.String(Size) 的Size要谨慎设置
    phone = db.Column(db.String(11),unique=True)
    regi_date = db.Column(db.DateTime,default=datetime.now)
    isdelete=db.Column(db.Boolean,default=False) #逻辑删除

    def __str__(self):
        return self.username
