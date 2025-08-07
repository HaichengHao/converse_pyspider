"""
@File    :index.py
@Editor  : 百年
@Date    :2025/7/31 9:28 
"""
from flask import Blueprint, request, render_template
from ..utils import dbhelper

index = Blueprint(name='index', import_name=__name__)
item = dbhelper.showdata()


@index.route('/index', methods=['GET', 'POST'])
def index_route():
    return render_template('index.html', item=item)
