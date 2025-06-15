"""
@File    :account.py
@Editor  : 百年
@Date    :2025/6/15 10:49 
"""

from flask import Blueprint

#创建account蓝图
account = Blueprint(name="account",import_name=__name__)


@account.route('/login')
def login():
    return "success"

@account.route('/logout')
def logout():
    return "退出成功"

