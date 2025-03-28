# @Author    : 百年
# @FileName  :07集成数据库连接池sqlite版本.py
# @DateTime  :2024/10/28 13:18
'''
SQLite线程安全问题：SQLite的连接在默认情况下不是线程安全的。当Flask在处理请求时，它可能会在不同的线程中使用相同的数据库连接，导致错误。
局部变量访问错误：在 dbverify 函数中，如果出现异常，cursor 变量可能未被定义，从而导致 UnboundLocalError。
解决方案
1. 启用SQLite的线程安全
在连接数据库时，可以通过设置 check_same_thread 参数为 False 来允许在不同的线程中使用相同的连接。
'''

# @Author    : 百年
# @FileName  :05基于数据库授权sqlite版本.py
# @DateTime  :2024/10/28 10:18
# @Author    : 百年
# @FileName  :04基于文件进行授权.py
# @DateTime  :2024/10/28 9:22
'''
如果是私有服务，那就用这个，这样给钱的才能用你的API，否则不能使用
'''
# @Author    : 百年
# @FileName  :08集成数据库连接池mysql版本.py
# @DateTime  :2024/10/28 11:05
'''
利用连接池机制优化冗余的数据库操作，提升性能
比如flask程序刚运行就创建和sqlite的2个链接，让其保持着
以后如果再有对数据库的操作,flask就拿着请求去连接池里面拿一个链接
当请求数量超过2个时候，允许再创建几个链接，但是有上限，最大为5
如果超过5个则新来的第6个等待五个中的任何一个结束链接
需要使用一个包dbutils,既数据库实用工具
'''
import sqlite3
from dbutils.pooled_db import PooledDB
import hashlib
from flask import Flask, jsonify, request

# 创建app对象
app = Flask(__name__)

'''
可以尝试在运行时往表中插入新的数据，看看会不会产生错误，发现并不会，文件授权也不会，这就是分开写的好处'''
# 配置连接池
Pool = PooledDB(
    creator=sqlite3,  # 使用链接数据库的模块,如果用的是mysql就用pymysql
    mincached=2,  # 初始化时，连接池中至少创建的空闲的链接，0表示不创建,表示刚启动时创建的
    maxcached=5,  # 连接池中最多闲置的链接,0和None不限制
    maxconnections=10,  # 链接池允许的最大连接数，0和None表示不限制链接数
    blocking=True,  # 连接池中如果没有可用链接后,是否阻塞等待，为True,则等待，False,则不等待然后报错
    setsession=[],  # 开始会话前执行的命令列表。如:["set datestyle to...","set time zone..."]
    ping=0,
# *args = [],  # 这里可以传递额外的参数
    # **kwargs = {"database": "uandt.db"}  # 这里是指定数据库文件的关键参数
    database="uandt.db", #传入关键字参数database指定sqlite数据库
    check_same_thread=False

)


# 定义一个函数连接数据库来检测token的合法性
def dbverify(sql, params):
    conn = Pool.connection()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result
# def dbverify(sql, params):
#     conn = Pool.connection()
#     try:
#         cursor = conn.cursor()
#         cursor.execute(sql, params)
#         result = cursor.fetchone()
#     except Exception as e:
#         print(f"Database error: {e}")
#         result = None
#     finally:
#         cursor.close()
#         conn.close()
#     return result


@app.route('/bili', methods=['POST', 'GET'])
def bili():
    # 注意token是url携带的，所以要用args.get获取的方式
    token = request.args.get("token")  # 先获取token
    if not token:  # 如果未携带token,则直接返回认证失败
        return jsonify({"status": False, "error": "认证失败,请联系管理员获取token"})

    # 如果携带了token,则需要验证token的合法性
    # 调用我们写的函数验证token
    res_verify = dbverify("select tokens from user where tokens=(?)",
                          (token,))  # 调用数据库验证token返回结果给变量res_verify,看看携带的token有没有在数据表中
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
