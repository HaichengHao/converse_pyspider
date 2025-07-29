"""
@File    :demo.py
@Editor  : 百年
@Date    :2025/7/29 14:54 
"""
'''
flask的返回类型多种多样'''

from flask import Flask,Response,jsonify

app = Flask(__name__)


@app.route('/index')
def index():
    return {'a': '北京', 'b': '上海'}



@app.route('/index1')
def index1():
    return Response('aloha')  #可以看看Response的实现
    '''
    其实其也可以写成 return "aloha" ,因为本质的实现步骤就是放到Response()里头 '''

@app.route('/indexjson')
def indexjson():
    return jsonify(
        {
            'a':'北京',
            'b':'上海'
        }
    )



# 返回元组
@app.route('/indextuple')
def indextuple():
    return jsonify(['a','b','c']), 200, {'Content-Type': 'application/json'}


@app.route('/indextuple2')
def indextuple2():
    return ', '.join(['a', 'b', 'c'])  # 返回 "a, b, c"


@app.route('/fof')
def fof():
    return 'sorry,page not found',404

@app.route('/indexn')
def indexn():
    response = Response(
        'aloha'
    )
    response.set_cookie('name','haha')
    return response
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8090)
