"""
@File    :app.py
@Editor  : 百年
@Date    :2025/6/15 20:56 
"""
'''
现在的网页还是有bug的,即直接访问不需要验证,所以要加上新的机制
那就是cookie和session

'''

from flask import Flask, render_template, request, redirect, session
from utils import dbhelper

app = Flask(__name__)
# important:想要设置session成功这个是必须的!!!!,需要为app对象设置密钥
app.secret_key = ';ouahsef;euahiuhiluh'  # 这个是可以自己指定的,随便输入,相当于加盐


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


@app.route('/index')
def index():
    # important:注意,到这里先读取凭证,凭证一致才返回
    # 读取凭证加解密
    # step2:
    result = session.get('user_info')
    print(result)
    if result:  # 如果正确则返回页面
        return render_template('index.html', msg=result)
    # 如果为空那就唤起无权访问界面
    return render_template('ucantview.html', msg="你无权访问,请先登录")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    # 得到用户post过来的数据
    user = request.form.get('user')
    pwd = request.form.get('pwd')

    print(user, pwd)
    # 然后到数据库中进行校验
    result = dbhelper.dbverify(sql='select * from user_info where account_name=%s and pwd=%s', params=(user, pwd))
    # if result:
    #     # 校验成功则登录成功,就可以指定重定向到其它界面
    #     # return "登录成功"
    #     return redirect('/index')
    if not result:  # 如果为空,那就维持在当前页面并报错
        return render_template("login.html", msg="登录失败,用户名或密码错误")
    # important:设置session
    # step1:
    session['user_info'] = result
    return redirect('/index')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

'''
   raise RuntimeError(
RuntimeError: The session is unavailable because no 
secret key was set.  Set the secret_key on the application
 to something unique and secret.  
 可以看到如果使用session是需要加密的
 
 '''
