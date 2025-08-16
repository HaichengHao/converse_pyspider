"""
@File    :models.py
@Editor  : 百年
@Date    :2025/8/8 19:56 
"""
from datetime import datetime

from .extensions import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(15),nullable=False)
    password = db.Column(db.String(12),nullable=False)
    phone = db.Column(db.String(11),unique=True)
    regi_time = db.Column(db.DateTime,default=datetime.now)

    def __str__(self):
        return self.username