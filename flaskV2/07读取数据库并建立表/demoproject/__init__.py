"""
@File    :__init__.py
@Editor  : 百年
@Date    :2025/7/31 9:21 
"""
from flask import Flask
from demoproject.views.index import index
def createapp():
    app = Flask(__name__)
    app.register_blueprint(index)

    return app
