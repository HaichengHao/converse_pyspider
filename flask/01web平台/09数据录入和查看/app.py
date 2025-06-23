"""
@File    :app.py
@Editor  : 百年
@Date    :2025/6/23 9:09 
"""

# important:本次要解决的问题-不要这么多路由,而是要有一个装饰器

# flask中有一个特殊的装饰器函数 before_request
# 当所有的请求到来时都会先执行这个函数


from flask import Flask, render_template, request, redirect, session
from utils import dbhelper
from datetime import datetime
app = Flask(__name__)
# important:想要设置session成功这个是必须的!!!!,需要为app对象设置密钥
app.secret_key = ';ouahsef;euahiuhiluh'


@app.route('/signup', methods=['POST', 'GET'])
def signup():
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


@app.route('/index',methods=['POST','GET'])
def index():
    # important:注意,到这里先读取凭证,凭证一致才返回
    # 读取凭证加解密
    # step2:
    if request.method == 'GET':
        result = session.get('user_info')
        return render_template('index.html', msg=result)
    user = request.form.get('user')
    pwd  = request.form.get('pwd')
    dbhelper.add_user(user,pwd)


@app.route('/login', methods=['POST', 'GET'])
def login():
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
    ctimestr = datetime.now().strftime('%Y-%m-%d %H:%M')
    return render_template('index.html',msg = result,time=ctimestr)


@app.before_request
def auth():
    # important:设置白名单,不然用户会卡循环登录最后报错,白名单里放的是无需登录就能访问的页面
    if request.path == "/login":
        return
    print('请求前操作')
    result = session.get('user_info')
    print(result)
    if result:  # 如果正确则返回页面
        return render_template('index.html', msg=result)

    # 如果为空那就唤起无权访问界面
    return redirect('/login')


'''
新的需求:想让每个页面都显示登录的用户名,但是如果还是按照之前的写法的话那每个页面的url都需要一个用户名
那么如何解决呢?这时候就需要定义全局模板'''

# important:这个函数只要被装饰了,那就可以直接利用JinJA执行这个函数
# tips:现在去index界面修改html
@app.template_global()
def current_user():
    return session['user_info'][0]['account_name']

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
