"""
@File    :redis_helper.py
@Editor  : 百年
@Date    :2025/6/30 14:04 
"""
import redis
import json

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


def pushtask(new_id):
    conn = redis.Redis(connection_pool=REDISPOOL)
    conn.lpush(TASK_QUEUE, new_id)
