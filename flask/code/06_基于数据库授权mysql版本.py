# @Author    : 百年
# @FileName  :06_基于数据库授权mysql版本.py
# @DateTime  :2024/10/28 13:01
# @Author    : 百年
# @FileName  :05基于数据库授权sqlite版本.py
# @DateTime  :2024/10/28 10:18
# @Author    : 百年
# @FileName  :04基于文件进行授权.py
# @DateTime  :2024/10/28 9:22
'''
如果是私有服务，那就用这个，这样给钱的才能用你的API，否则不能使用
'''
import pymysql
import hashlib
from flask import Flask, jsonify, request

# 创建app对象
app = Flask(__name__)

'''
可以尝试在运行时往表中插入新的数据，看看会不会产生错误，发现并不会，文件授权也不会，这就是分开写的好处'''

# 定义一个函数连接数据库来检测token的合法性
def dbverify(sql,params):
    conn=pymysql.connect(host='',port=3306,user='root',passwd='',charset='utf8',db='uandt.db')
    cursor = conn.cursour()
    cursor.execute(sql,params)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result



@app.route('/bili', methods=['POST', 'GET'])
def bili():
    # 注意token是url携带的，所以要用args.get获取的方式
    token = request.args.get("token")  # 先获取token
    if not token:  # 如果未携带token,则直接返回认证失败
        return jsonify({"status": False, "error": "认证失败,请联系管理员获取token"})

    # 如果携带了token,则需要验证token的合法性
    # 调用我们写的函数验证token
    # 这里是参数化了，使用起来更方便，如果还需要对数据库进行其它操作也可以进行，故将旧的sqlite也做了参数化
    res_verify = dbverify("select tokens from user where tokens='%s'",[token,]) #调用数据库验证token返回结果给变量res_verify,看看携带的token有没有在数据表中
    if res_verify == None:
        return jsonify({"status": False, "error": "认证失败,令牌错误"})

    # 如果在就正常的往后进行
    ordered_string = request.json.get("ordered_string")
    if not ordered_string:  # 如果没有得到ordered_string
        return jsonify({"status": False, "error": "参数错误"})
    # 如果获取到了就调用核心sign
    encrypt_string = ordered_string + "560c52ccd288fed045859ed18bffd973"
    obj = hashlib.md5(encrypt_string.encode('utf-8'))
    sign = obj.hexdigest()
    # 将签名的结果返回给用户
    return jsonify({"status": True, "data": sign})


if __name__ == '__main__':
    app.run()
