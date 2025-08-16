"""
@File    :extensions.py
@Editor  : 百年
@Date    :2025/8/8 19:56 
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
