"""
@File    :09redis连接池.py
@Editor  : 百年
@Date    :2025/6/14 22:33 
"""
import redis

redispool_params={
    'host':'127.0.0.1',
    'port':6379,
    'db': 2,
    'max_connections':1000,
    'decode_responses': True  # 设置默认解码
}
pool = redis.ConnectionPool(**redispool_params)
conn = redis.Redis(connection_pool=pool)
