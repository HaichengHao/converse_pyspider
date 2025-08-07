"""
@File    :app.py
@Editor  : 百年
@Date    :2025/8/1 9:05 
"""
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html',msg="<h1>你好呀</h1>",msg2="aloha")

@app.route('/demo1')
def demo1():
    return render_template('demo.html',msg="<h1>你好呀</h1>") #这个html中的jinja没有进行转译

if __name__ == '__main__':
    app.run(debug=True,port=8080,host='127.0.0.1')
