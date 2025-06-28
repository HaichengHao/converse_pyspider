"""
@File    :index.py
@Editor  : 百年
@Date    :2025/6/23 20:40 
"""
from flask import Blueprint, session, request, redirect, render_template
from myweb_new.utils import dbhelper
from myweb_new.utils.get_index_data import get_index_data

index = Blueprint(name='index', import_name=__name__)


@index.route('/index', methods=['POST', 'GET'])
def index_route():
    uid = session['user_info'][0]['ID']
    page = request.args.get("page", "1")  # tips:获取页码信息,默认是第一页
    page = int(page)  # tips:注意将接受到的转换为int类型,方便sql语句优化
    per_page_count = 5  # 每页显示几条数据
    # important:构造的sql语句是 select username,password from jd where uid = %s limit 5 offset 0 #此为第一页,第二页就是 limit 5 offset 5 所以总结为如下
    offset = (page - 1) * per_page_count
    data = get_index_data(per_page_count=per_page_count, offset=offset)
    # important:注意,到这里先读取凭证,凭证一致才返回
    # 读取凭证加解密
    # step2:
    if request.method == 'GET':
        return render_template('index.html', **data)
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    print(user, pwd)

    dbhelper.add_info(user, pwd, uid)
    # item = dbhelper.show_info(uid)
    # print(item)
    return redirect('/index')
