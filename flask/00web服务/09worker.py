"""
@File    :09worker.py
@Editor  : 百年
@Date    :2025/6/14 18:11 
"""
'''
从队列中去获取任务,执行并写入到结果队列
'''
import json
import redis
import hashlib

# REDIS_CONN_PARAMS = {
#     'host': '127.0.0.1',
#     'port': 6379,
#     'db': 2,
#     'decode_responses': True
# }
# conn = redis.Redis(**REDIS_CONN_PARAMS)

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


def get_task():
    data = conn.brpop(TASK_QUEUE, timeout=10) #block right pop 阻塞形态右边出队
    # 作判断,
    if not data:
        return  # 如果没有数据就返回None

    # print(data)
    return json.loads(data[1])  # 因为pop取出来的是数组形式且元素是字节形式


def set_result(taskid, value):
    conn.hset(RESULT_QUEUE, taskid, value)


def run():
    while True:
        # 从redis中获取任务
        task_dict = get_task()
        print(task_dict)
        if not task_dict:
            continue
        # 执行耗时操作
        ordered_string = task_dict['data']
        encrypt_string = ordered_string + "560c52ccd288fed045859ed18bffd973"
        obj = hashlib.md5(encrypt_string.encode('utf-8'))
        sign = obj.hexdigest()

        # 写入到结果队列
        task_id = task_dict['tid']
        set_result(task_id, sign)


if __name__ == '__main__':
    run()
