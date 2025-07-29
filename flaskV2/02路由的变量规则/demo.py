"""
@File    :demo.py
@Editor  : 百年
@Date    :2025/7/29 8:34 
"""

#路由并不一定要是字符串,也可以是变量,只要写好符合的变量规则就能实现符合规则的路由

from flask import Flask


app = Flask(__name__)


data={
    'a':'北京',
    'b':'上海',
    'c':'广州',
    'd':'深圳'
}

@app.route('/index')
def index():
    return '我是首页'

@app.route('/getcity/<key>') #key默认就是字符串类型的,如果想要声明类型的话就<string:key>
def getcity(key):
    return data.get(key)

@app.route('/add/<int:num>')
def add(num):
    result = num+10
    return str(result)
'''
最开始没写强制转换的时候报错了,可以观察发现其返回值类型中没有int类型,下面的报错信息写了其支持的返回值类型
TypeError: The view function did not return a valid response. The return type must be a string, dict, list, 
tuple with headers or status, Response instance, or WSGI callable, but it was a int.'''

@app.route('/addf/<float:money>')
def addf(money):
    return str(money)

@app.route('/index/<path:p>')
def get_path(p):
    print('**********>',type(p))
    return p
'''
**********> <class 'str'> 
返回值依旧是字符串类型的'''

@app.route('/uidget/<uuid:id>')
def uidget(id):
    return str(id)

'''
38cb82f9-655c-4092-85e6-ec9a5925c763 注意这个是需要严格生成的,不是随便乱敲的,可以回看之前的flask00web服务的生成uuid'''

if __name__ == '__main__':
    app.run(debug=True,port=8080,host='0.0.0.0')