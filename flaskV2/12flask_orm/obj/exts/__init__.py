"""
@File    :__init__.py.py
@Editor  : 百年
@Date    :2025/8/6 10:45 
"""

# 创建一个映射对象,完成数据库到flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()
mig = Migrate()