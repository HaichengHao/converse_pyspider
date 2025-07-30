"""
@File    :demo.py
@Editor  : 百年
@Date    :2025/7/30 16:45 
"""
from flask import Flask,render_template
lst=[
    i for i in range(10)
]
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html',ls=lst)

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=8090)

