"""
@File    :app.py
@Editor  : 百年
@Date    :2025/8/3 14:44 
"""
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/login')
def login():
    pass

@app.route('/signup')
def signup():
    pass
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/macro1')
def macro1():
    return render_template('macro/macro1.html')

@app.route('/macro2')
def macro2():
    return render_template('macro/macro2.html')
if __name__ == '__main__':
    app.run(port=8080,host='127.0.0.1',debug=True)


