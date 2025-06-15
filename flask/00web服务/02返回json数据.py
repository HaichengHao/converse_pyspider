# @Author    : 百年
# @FileName  :02返回json数据.py
# @DateTime  :2024/10/27 20:19

'''
json格式的请求体
{"xx":123,"yy":99}
'''

import json #可以单独调用json
from flask import Flask,request,jsonify #也可以调用jsonify

# 创建一个flask对象
app = Flask(__name__)

# http://127.0.0.1:5000/index?age=19&pwd=123 这种是以GET方式来请求的，默认只支持GET
# 如果想要支持POST,需要在@app.route()指定参数method=['POST'],注意，里头不写GET也是支持GET的
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
@app.route('/index') #如果有人访问/xxx时就自动执行index函数来处理这个请求
def index():
    # GET方式
    # age = request.args.get('age') #get请求用args来获取
    # pwd = request.args.get('pwd')
    # print(age,pwd)
    #
    # # 目前只能模拟get请求，需要用到postman模拟post请求
    # xx=request.form.get('xx') #post请求用form来获取
    # yy=request.form.get('yy')
    # print(xx,yy)
    # # JSON格式
    # 如何获取看03
    # print(request.json)
    # 调用核心算法生成sign签名
    # 注意返回的格式应当是字符串形式的
    # 所以对于json格式我们需要将其序列化
    # return json.dump({"status":True,"data":"adawfefe1ho121rnxal"})
#     如果失败了也可以返回一个False  return json.dump({"status":False,"data":"error"})

# 如果使用的是jsonify可以这样写
    return jsonify({"status":True,"data":"adawfefe1ho121rnxal"})
@app.route('/err')
def err():
    return "失败"


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000) #不写host和port就会用默认的端口