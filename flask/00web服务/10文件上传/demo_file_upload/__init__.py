# @Author    : 百年
# @FileName  :__init__.py
# @DateTime  :2025/7/4 19:08
from flask import Flask
from demo_file_upload.views.upload import uPload


def create_app():
    app = Flask(__name__)
    return app
