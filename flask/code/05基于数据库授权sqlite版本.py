# @Author    : 百年
# @FileName  :05基于数据库授权sqlite版本.py
# @DateTime  :2024/10/28 10:18
# @Author    : 百年
# @FileName  :04基于文件进行授权.py
# @DateTime  :2024/10/28 9:22
'''
如果是私有服务，那就用这个，这样给钱的才能用你的API，否则不能使用
'''
import sqlite3
import hashlib
from flask import Flask, jsonify, request

# 创建app对象
app = Flask(__name__)

'''
可以尝试在运行时往表中插入新的数据，看看会不会产生错误，发现并不会，文件授权也不会，这就是分开写的好处'''

# 定义一个函数连接数据库来检测token的合法性
def dbverify(sql,params):
    conn = sqlite3.connect('uandt.db')
    cursor = conn.cursor()
    # 执行语句,查询输入的token_str是否在数据表中
    # cursor.execute('select tokens from user where tokens=(?)',(token_str,))
    cursor.execute(sql,params)
    res = cursor.fetchone() #接收结果
    conn.commit()
    cursor.close()
    conn.close()
    return res  #返回结果，如果不在就是空，如果在就不为空


@app.route('/bili', methods=['POST', 'GET'])
def bili():
    # 注意token是url携带的，所以要用args.get获取的方式
    token = request.args.get("token")  # 先获取token
    if not token:  # 如果未携带token,则直接返回认证失败
        return jsonify({"status": False, "error": "认证失败,请联系管理员获取token"})

    # 如果携带了token,则需要验证token的合法性
    # 调用我们写的函数验证token
    # res_verify = dbverify(token) #调用数据库验证token返回结果给变量res_verify,看看携带的token有没有在数据表中
    res_verify=dbverify('select tokens from user where tokens=(?)',(token,))
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
