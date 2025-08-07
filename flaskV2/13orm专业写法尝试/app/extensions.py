"""
@File    :extensions.py
@Editor  : 百年
@Date    :2025/8/6 16:53 
"""
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()