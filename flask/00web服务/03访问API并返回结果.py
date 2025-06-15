# @Author    : 百年
# @FileName  :03访问API并返回结果.py
# @DateTime  :2024/10/27 20:49
from flask import Flask,request,jsonify
import hashlib
# 创建应用对象
app = Flask(__name__)

@app.route('/bili',methods=["POST","GET"])
def bili():
    '''
    请求的数据格式要求的是字典
    '''
    ordered_string = request.json.get("ordered_string")
    if not ordered_string: #如果没有得到ordered_string
        return jsonify({"status":False,"error":"参数错误"})
    # 调用核心sign
    encrypt_string = ordered_string + "560c52ccd288fed045859ed18bffd973"
    obj = hashlib.md5(encrypt_string.encode('utf-8'))
    sign = obj.hexdigest()
    # 将签名的结果返回给用户
    return jsonify({"status":True,"data":sign})

# 用postman伪造调用者
if __name__ == '__main__':
    app.run('127.0.0.1',port=5000)