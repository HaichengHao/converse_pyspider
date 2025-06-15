"""
@File    :app.py
@Editor  : 百年
@Date    :2025/6/15 20:56 
"""
from flask import Flask,render_template,request,redirect
from utils import dbhelper
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    # 得到用户post过来的数据
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    print(user,pwd)
    # 然后到数据库中进行校验
    result = dbhelper.dbverify(sql='select * from user_info where account_name=%s and pwd=%s',params=(user,pwd))
    if result:
        #校验成功则登录成功,就可以指定重定向到其它界面
        # return "登录成功"
        return redirect('/index')
    return render_template("login.html",msg="登录失败,用户名或密码错误")

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=5000)