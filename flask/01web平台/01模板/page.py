"""
@File    :page.py
@Editor  : 百年
@Date    :2025/6/15 13:02 
"""
import time
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)
# app = Flask(__name__,template_folder='xxx')  important:也可以指定模板文件


@app.route('/index')
def index():
    ctimestr = datetime.now().strftime('%Y-%m-%d %H:%M')
    return render_template('index.html',n1="张三",time = ctimestr) #它会寻找到这个文件并读取内容并返回给调用者(浏览器),并对模板内容进行渲染
# 注意它默认去templeates目录寻


@app.route('/login')
def login():
    pass


@app.route('/error')
def error():
    pass


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
