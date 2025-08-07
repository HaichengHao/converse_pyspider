"""
@File    :__init__.py
@Editor  : 百年
@Date    :2025/8/4 14:16 
"""

from flask import Flask,request
from .apps.user.view import user_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp)
    return app