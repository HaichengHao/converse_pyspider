"""
@File    :signup.py
@Editor  : 百年
@Date    :2025/6/23 19:46 
"""
from flask import Blueprint, render_template, request, redirect
from myweb_optimize.utils import dbhelper

signup = Blueprint(name='signup', import_name=__name__)


@signup.route('/signup', methods=['POST', 'GET'])
def signup_route():
    if request.method == 'GET':
        return render_template('signup.html')

    user = request.form.get('user')
    pwd = request.form.get('pwd')
    print(user, pwd)
    dbhelper.add_user(name=user, pwd=pwd)
    # 然后走一遍监测是否插入成功
    result = dbhelper.dbverify(sql='select * from user_info where account_name=%s and pwd=%s', params=(user, pwd))
    print(result)
    if result:
        # 插入成功
        return redirect('/login')  # 重定向到登录页面进行登录
    else:
        return render_template('signup.html', msg="注册失败,请重新注册")
