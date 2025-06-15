"""
@File    :__init__.py
@Editor  : 百年
@Date    :2025/6/15 10:49 
"""
from flask import Flask
from myproject.views.account import account
from myproject.views.home import home

def create_app():
    app = Flask(__name__)

    # important:要与蓝图之间创建关系,将蓝图注册到这里
    app.register_blueprint(account)
    app.register_blueprint(home)


    return app
