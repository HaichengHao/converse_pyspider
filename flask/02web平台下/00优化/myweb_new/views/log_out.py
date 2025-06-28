"""
@File    :logout.py
@Editor  : 百年
@Date    :2025/6/28 12:50 
"""

'''
注销的路子就是清除掉session,然后重定向到登录页面'''
from flask import session, redirect, Blueprint,request

log_out = Blueprint(name='log_out', import_name=__name__)


@log_out.route('/logout', methods=['POST', 'GET'])
def logout_route():
    if request.method == 'GET':
        session.clear()
        return redirect('/login')
