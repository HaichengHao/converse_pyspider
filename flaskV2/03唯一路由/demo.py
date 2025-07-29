"""
@File    :demo.py
@Editor  : 百年
@Date    :2025/7/29 10:58 
"""
#summary: 带/的会自动重定向,不带/结尾的就是唯一路由
from flask import Flask

app = Flask(__name__)


@app.route('/about')
def about():
    return 'hi'
#tips:如果写成http://127.0.0.1:8090/about/则访问不到


@app.route('/projects/')
def projects():
    return 'nihao'

# tips:http://127.0.0.1:8090/projects 就算写斜杠也可以重定向到带斜杠的


if __name__ == '__main__':
    app.run(debug=True,port=8090,host='127.0.0.1')

