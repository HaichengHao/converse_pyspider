"""
@File    :__init__.py
@Editor  : 百年
@Date    :2025/8/6 16:52 
"""
import os
from .commands import init_db,drop_db,hello
from flask import Flask
from .extensions import db,migrate
from config import config
def create_app(config_name=None):
    app = Flask(__name__)

    #加载配置项  若指定了配置则使用指定配置否则使用默认的配置
    config_name = config_name or os.getenv('FLASK_ENV','default')
    app.config.from_object(config[config_name])

    #初始化扩展
    db.init_app(app)
    migrate.init_app(app,db)
    # app.cli.add_command(init_db)

    app.cli.add_command(hello)
    return app

