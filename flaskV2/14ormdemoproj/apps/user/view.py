"""
@File    :view.py
@Editor  : 百年
@Date    :2025/8/9 11:01 
"""
from flask import Blueprint, request, render_template
from .extensions import db
from .models import User

user_bp = Blueprint(name='user', import_name=__name__)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        pass
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:
            # tips:与模型进行结合,来完成数据库的添加
            # step1:找到模型类并创建对象
            user = User()
            # step2:给对象的属性进行赋值
            user.username = username
            user.password = password
            user.phone = phone
            # step3:往数据库里添加
            db.session.add(user)
            # step4:进行提交
            db.session.commit()
            return '用户注册成功'
        else:
            return render_template('user/register.html', errorinfo='两次输入的密码不一致请重新输入')
    return render_template('user/register.html')
