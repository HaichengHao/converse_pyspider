"""
@File    :app.py
@Editor  : 百年
@Date    :2025/6/15 18:26 
"""
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=5000)
