"""
@File    :model.py
@Editor  : 百年
@Date    :2025/8/6 21:27 
"""
from ..extensions import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)