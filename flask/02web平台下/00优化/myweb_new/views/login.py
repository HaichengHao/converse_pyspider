"""
@File    :login.py
@Editor  : 百年
@Date    :2025/6/23 19:54 
"""
from flask import Blueprint,request,render_template,session,redirect
from myweb_new.utils import dbhelper

login = Blueprint(name='login',import_name=__name__)


@login.route('/login',methods=['POST','GET'])

def login_route():
    print('进行登录了')
    if request.method == 'GET':
        return render_template("login.html")

    # 得到用户post过来的数据
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    print(user, pwd)
    # 然后到数据库中进行校验
    result = dbhelper.dbverify(sql='select * from user_info where account_name=%s and pwd=%s', params=(user, pwd))
    if not result:  # 如果为空,那就维持在当前页面并报错
        return render_template("login.html", msg="登录失败,用户名或密码错误")
    # important:设置session
    # step1:
    session['user_info'] = result

    # data = get_index_data()
    # ctimestr = datetime.now().strftime('%Y-%m-%d %H:%M')

    return redirect('/index')