"""
@File    :view.py
@Editor  : 百年
@Date    :2025/8/4 16:11 
"""
from flask import Blueprint, request, render_template,redirect
# import model

user_bp = Blueprint(name='user', import_name=__name__)

users = []


@user_bp.route('/')
def user_center():
    return '用户中心'


@user_bp.route('/register', methods=['GET', 'POST'])
def register_route():
    if request.method == 'GET':
        return render_template('user/register.html')
    username = request.form.get('username')
    password = request.form.get('password')
    re_enterpassword = request.form.get('re_password')
    phonenum = request.form.get('phone')
    if password == re_enterpassword:
        # 用户名唯一
        for user in users:
            if username == user:
                return render_template('user/register.html', erro_info='用户名已经被使用')
        # # 创建user对象
        # user_info = model.User(username, password, phonenum)
        # # 添加到用户列表中
        # users.append(user_info)

        return redirect('/')


@user_bp.route('/login', methods=['GET', 'POST'])
def login_route():
    return '登录'


@user_bp.route('/logout', methods=['GET', 'POST'])
def logout_route():
    return '退出'
