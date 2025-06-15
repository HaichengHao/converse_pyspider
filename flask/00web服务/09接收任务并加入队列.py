"""
@File    :09接收任务并加入队列.py
@Editor  : 百年
@Date    :2025/6/14 10:26 
"""
import uuid
import hashlib
import sqlite3
from flask import Flask, jsonify, request
from dbutils.pooled_db import PooledDB
import json
import redis

# REDIS_CONN_PARAMS = {
#     'host': '127.0.0.1',
#     'port': 6379,
#     'db': 2,
#     'decode_responses': True  # 设置默认解码
# }

TASK_QUEUE = 'task_lst'
RESULT_QUEUE = 'task_result'
# 使用REDIS连接池
REDISPOOL_CONN_PARAMS = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 2,
    'max_connections': 1000,
    'decode_responses': True  # 设置默认解码
}
REDISPOOL = redis.ConnectionPool(**REDISPOOL_CONN_PARAMS)  # 使用redis连接池
conn = redis.Redis(connection_pool=REDISPOOL)
# conn = redis.Redis(**REDIS_CONN_PARAMS)  # 解包赋值

app = Flask(__name__)


# Pool = PooledDB(
#     creator=sqlite3,
#     mincached=2,
#     maxcached=5,
#     maxconnections=10,
#     blocking=True,
#     setsession=[],
#     ping=0,
#     database="uandt.db",
#     check_same_thread=False

# )


# def dbverify(sql, params):
#     conn = Pool.connection()
#     cursor = conn.cursor()
#     cursor.execute(sql, params)
#     result = cursor.fetchone()
#     cursor.close()
#     conn.close()
#     return result


@app.route('/task', methods=['POST', 'GET'])
def task():
    # token = request.args.get("token")
    # if not token:
    #     return jsonify({'status': False, 'error': '认证失败,联系管理员购买通行证'})
    # res_verify = dbverify(sql="select tokens from user where tokens=(?)", params=(token,))
    # if res_verify == None:
    #     return jsonify({'status': False, 'error': '认证失败,令牌信息有误'})
    #

    # 获取得到的order_string
    ordered_string = request.json.get("ordered_string")
    if not ordered_string:
        return jsonify({'status': False, "error": "参数错误"})

    # 因为要伪造耗时操作,所以要将其放入队列中
    # 其次,要返回任务id

    # 生成任务id,这里就用uuid来生成
    taskid = str(uuid.uuid4())
    print(taskid)
    # 将order_string放到Redis数据库队列 中
    task_dict = {'tid': taskid, 'data': ordered_string}
    # conn.lpush("task_lst", json.dumps(task_dict))
    conn.lpush(TASK_QUEUE, json.dumps(task_dict))

    # encrypt_string = ordered_string + "560c52ccd288fed045859ed18bffd973"
    # obj = hashlib.md5(encrypt_string.encode('utf-8'))
    # sign = obj.hexdigest()

    # 将签名的结果返回给用户
    return jsonify({"status": True, "data": taskid, "message": "正在处理中"})


@app.route('/result', methods=['GET'])
def result():
    # 获取task_id
    tid = request.args.get('tid')
    if not tid:
        return jsonify({'status': False, 'message': "请求错误,未携带任务号"})
    # sign = conn.hget('task_result', tid)  # 因为拿到的是hash,所以要用到hget
    sign = conn.hget(RESULT_QUEUE, tid)  # 因为拿到的是hash,所以要用到hget
    if not sign:
        return jsonify({'status': True, 'data': "", 'message': "未完成,请继续等待worker完成"})
    print(sign)

    # 如果拿到就返回结果并且从结果队列中删除
    # conn.hdel('task_result', tid)
    conn.hdel(RESULT_QUEUE, tid)
    return jsonify({'status': True, "message": 'ok', 'sign': sign})
    # return jsonify({'status':True,"message":'ok','sign':sign.decode('utf-8')}) 如果redis没设置自动解码的话就需要解码操作


if __name__ == '__main__':
    app.run(debug=True)
