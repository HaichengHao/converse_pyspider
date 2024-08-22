# @Editor    : 百年
# @FileName  :Server.py.py
# @Time      :2024/7/29 7:44
from flask import Flask,render_template
from time import sleep

# 1.实例化app对象
app = Flask(__name__)
# 装饰器的参数就是路由地址
@app.route('/main')
def main():#视图函数
    sleep(2)
    return 'i am nain'
@app.route('/bobo')
def index1():
    sleep(2)
    return render_template('test.html')
@app.route('/jay')
def index2():
    sleep(2)
    return render_template('test2.html')
@app.route('/tom')
def index3():
    sleep(2)
    return render_template('test3.html')

if __name__ == '__main__':
    app.run()