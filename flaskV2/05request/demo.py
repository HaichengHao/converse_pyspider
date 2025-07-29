"""
@File    :demo.py
@Editor  : 百年
@Date    :2025/7/29 16:44 
"""
from flask import Flask,request,render_template
import settings
app = Flask(__name__)
app.config.from_object(settings)


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user_name = request.form.get('username')
    pwd = request.form.get('password')
    print(user_name,pwd)
    print(request.full_path)
    print(request.path)

    return render_template('index.html',msg=f'登录成功,欢迎你{user_name}')

if __name__ == '__main__':
    app.run(port=8090)
    print(app.url_map) #important:可以打印路由规则表查看规则


