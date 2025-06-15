# @Author    : 百年
# @FileName  :01初识.py
# @DateTime  :2024/10/27 19:36
from flask import Flask,request

# 创建一个flask对象
app = Flask(__name__)

# http://127.0.0.1:5000/index?age=19&pwd=123 这种是以GET方式来请求的，默认只支持GET
# 如果想要支持POST,需要在@app.route()指定参数method=['POST'],注意，里头不写GET也是不支持GET的
# POST会有请求体,它不是http://127.0.0.1:5000/index?age=19&pwd=123 这样的形式，而是
'''
http://127.0.0.1:5000/index
请求体:xx=123&yy=99这样的形式
需要用request.form.get('xx')
request.form.get('yy')'''
'''
另外一种情况
如果请求体是json格式
{"xx":123,"yy":456}该如何接受呢?'''
@app.route('/index',methods=['POST']) #如果有人访问/xxx时就自动执行index函数来处理这个请求
def index():
    # GET方式
    age = request.args.get('age') #get请求用args来获取
    pwd = request.args.get('pwd')
    print(age,pwd)

    # 目前只能模拟get请求，需要用到postman模拟post请求
    xx=request.form.get('xx') #post请求用form来获取
    yy=request.form.get('yy')
    print(xx,yy)
    # JSON格式,注意传入的是json,在postman中点击raw,选择json
    print(request.json)
    return "成功"
@app.route('/err')
def err():
    return "失败"


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True) #不写host和port就会用默认的端口