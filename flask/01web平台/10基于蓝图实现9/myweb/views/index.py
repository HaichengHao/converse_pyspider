"""
@File    :index.py
@Editor  : 百年
@Date    :2025/6/23 20:40 
"""
from flask import Blueprint,session,request,redirect,render_template
from myweb.utils import dbhelper
from myweb.utils.get_index_data import get_index_data

index = Blueprint(name='index',import_name=__name__)

@index.route('/index',methods=['POST','GET'])
def index_route():
    uid = session['user_info'][0]['ID']
    data = get_index_data()
    # important:注意,到这里先读取凭证,凭证一致才返回
    # 读取凭证加解密
    # step2:
    if request.method == 'GET':
        return render_template('index.html',**data)
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    print(user, pwd)

    dbhelper.add_info(user, pwd, uid)
    item = dbhelper.show_info(uid)
    print(item)
    return redirect('/index')