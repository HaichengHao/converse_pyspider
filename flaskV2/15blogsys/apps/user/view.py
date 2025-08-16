"""
@File    :view.py
@Editor  : 百年
@Date    :2025/8/10 10:04 
"""
from .models import User
from .extensions import db
from flask import Blueprint, request, render_template, redirect, url_for
from .models import User
user_bps = Blueprint(name='user',import_name=__name__)
import hashlib

@user_bps.route('/')
def user_center():
    users = User.query.all()
    print(users)
    return render_template('user/usercenter.html',users=users)

@user_bps.route('/deldata')
def del_data():
    username = request.args.get('username')
    #tips:从前端拿到
    #先查询到
    # res = db.session.query(username)
    # print(res)
    # 2025-08-11 12:44:33,318 INFO sqlalchemy.engine.Engine [cached since 1631s ago] {}
    # [<User 1>]

    #tips:执行删除操作
    user = User.query.filter_by(username=username).first()

    #tips:或者这样写
    # username = db.session.query(User).filter_by(username=username)

    db.session.delete(user)
    db.session.commit()
    #然后重定向到用户中心界面
    return redirect('/')


@user_bps.route('/modifydata', methods=['POST', 'GET'], endpoint='modifydata')
def modidata():
    if request.method == 'GET':
        username = request.args.get('username')
        user = User.query.filter_by(username=username).first()
        if not user:
            return "用户不存在", 404
        return render_template('user/custom_data.html', user=user)

    # POST 处理
    username = request.form.get('username')
    newusername = request.form.get('newusername')
    password = request.form.get('password')
    repassword = request.form.get('repassword')
    phone = request.form.get('phone')

    if password != repassword:
        return render_template('user/custom_data.html', errorinfo='两次输入的密码不一致，请重新输入')

    user = User.query.filter_by(username=username).first()
    if not user:
        return render_template('user/custom_data.html', errorinfo="用户不存在，无法修改")

    # 更新用户名（如果提供了新用户名）
    if newusername:
        user.username = newusername

    # 更新密码（已加密）
    user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # 更新手机号
    if phone:
        user.phone = phone

    db.session.commit()
    return redirect(url_for('user.user_center'))



@user_bps.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
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

            #important:调用加密算法对密码进行加密
            user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            user.phone = phone
            # step3:往数据库里添加
            db.session.add(user)
            # step4:进行提交
            db.session.commit()
            # return '用户注册成功'
            return redirect(url_for('user.user_center'))
        else:
            return render_template('user/register.html', errorinfo='两次输入的密码不一致请重新输入')
    return render_template('user/register.html')



@user_bps.route('/login',methods=['GET','POST'])
def login():
    if request.method =='GET':
        return render_template('user/login.html')
    username = request.form.get('username')
    password_raw = request.form.get('password')
    password_enc = hashlib.sha256(password_raw.encode('utf-8')).hexdigest()
    phone = request.form.get('phone')

    user = User.query.filter_by(username=username,password=password_enc,phone=phone).first()
    if user:
        return redirect('/')
    else:
        return render_template('user/login.html',errorinfo='信息错误,请重试')

