# @Editor    : 百年
# @FileName  :00异步爬虫.py
# @Time      :2024/7/29 7:37
from flask import Flask,render_template
from time import sleep

# 1.实例化app对象
app = Flask(__name__)
@app.route('/main')
def main():
    sleep(2)
    return 'i am nain'
@app.route('/bobo')
def index1():
    sleep(2)
    return render_template('test.html')
