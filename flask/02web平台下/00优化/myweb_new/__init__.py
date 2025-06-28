"""
@File    :__init__.py
@Editor  : 百年
@Date    :2025/6/23 19:39 
"""
from flask import Flask, session, request, redirect
from myweb_new.views.login import login
from myweb_new.views.signup import signup
from myweb_new.views.index import index
from myweb_new.views.log_out import log_out
from markupsafe import Markup  #important:注意引入这个才能传入的时候让html文件默认为格式


def current_user():
    return session['user_info'][0]['account_name']


def auth():
    # important:设置白名单,不然用户会卡循环登录最后报错,白名单里放的是无需登录就能访问的页面
    if request.path in ["/login", '/signup']:
        return
    # important:新操作,解决样式问题,新的白名单
    if request.path.startswith('/static/'):
        return
    print('请求前操作')
    result = session.get('user_info')
    print(result)
    # if result:  # 如果正确则返回页面
    #     return render_template('index.html', msg=result)  important:这样做会产生逻辑循环,导致index中插入数据不会返回结果

    # 如果为空那就唤起无权访问界面
    if not result:
        return redirect('/login')

#important:处理页码
def getpage():
    page = request.args.get("page","1")
    page = int(page)
    if page <=1:
        prev_page = 1
    else:
        prev_page = page-1
    try:
        next_page = page+1
    except:
        next_page = 1
    pageinfo = f"""
        <nav aria-label="...">
          <ul class="pager">
            <li><a href="?page={prev_page}">上一页</a></li>
            <li><a href="?page={next_page}">下一页</a></li>
          </ul>
        </nav>
    """
    return Markup(pageinfo)
def create_app():
    app = Flask(__name__)
    app.secret_key = ';ouahsef;euahiuhiluh'

    # important:这样可以简洁一些
    app.template_global()(current_user)
    app.template_global()(getpage)
    app.before_request(auth)
    # @app.template_global()
    # def current_user():
    #     return session['user_info'][0]['account_name']
    #
    #
    # @app.before_request
    # def auth():
    #     # important:设置白名单,不然用户会卡循环登录最后报错,白名单里放的是无需登录就能访问的页面
    #     if request.path in ["/login", '/signup']:
    #         return
    #     print('请求前操作')
    #     result = session.get('user_info')
    #     print(result)
    #     # if result:  # 如果正确则返回页面
    #     #     return render_template('index.html', msg=result)  important:这样做会产生逻辑循环,导致index中插入数据不会返回结果
    #
    #     # 如果为空那就唤起无权访问界面
    #     if not result:
    #         return redirect('/login')

    app.register_blueprint(signup)
    app.register_blueprint(index)
    app.register_blueprint(login)
    app.register_blueprint(log_out)

    return app
