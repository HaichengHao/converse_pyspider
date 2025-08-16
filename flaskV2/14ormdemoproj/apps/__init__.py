"""
@File    :__init__.py
@Editor  : 百年
@Date    :2025/8/8 19:56 
"""
import os

from flask import Flask
from .user.extensions import db, migrate
from config import config  # 引入config字典
from .user.view import user_bp

def create_app(configname=None):
    app = Flask(__name__,template_folder='../templates')
    configname = configname or os.getenv('FLASK_ENV' or 'default')
    app.config.from_object(config[configname])
    db.init_app(app)
    app.register_blueprint(user_bp)
    migrate.init_app(app=app, db=db)
    #注册蓝图

    return app
