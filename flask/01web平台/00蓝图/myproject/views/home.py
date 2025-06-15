"""
@File    :home.py
@Editor  : 百年
@Date    :2025/6/15 10:50 
"""
from flask import Blueprint
home = Blueprint(name="home",import_name=__name__)


@home.route('/index')
def index():
    return "index"