"""
@File    :02redis测试.py
@Editor  : 百年
@Date    :2025/6/14 18:31 
"""
import uuid
import hashlib
import sqlite3
from flask import Flask, jsonify, request
from dbutils.pooled_db import PooledDB
import json
import redis
REDIS_CONN_PARAMS={
    'host':'127.0.0.1',
    'port':6379,
    'db':2,
    'decode_responses':True
}
conn = redis.Redis(**REDIS_CONN_PARAMS)

result = conn.brpop('task_lst')  #brpop和rpop不一样,前者返回的是元组,后者返回的是字符串
# print(result['data'],type(result))
print(result)
'''
('task_lst', '{"tid": "a6217827-ced8-4925-bd16-4fc8fb05277c", 
"data": "actual_played_time=0&aid=851776257&appkey=1d8b6e7d45233436&auto_play=0&build=6240300&c_locale=zh_CN&channel=xxl
_gdt_wm_253&cid=516350598&epid=0&epid_status=&from=6&from_spmid=tm.recommend.0.0&last_play_progress_time=0&list_play_time
=0&max_play_progress_time=0&mid=0&miniplayer_play_time=0&mobi_app=android&network_type=1&paused_time=0&platform=android&
play_status=0&play_type=1&played_time=0&quality=80&s_locale=zh_CN&session=897a6991b1f7489f915e420c9b82136d9c5dec62&sid=0
&spmid=main.ugc-video-detail-vertical.0.0&start_ts=0&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226
.24.0%22%2C%22abtest%22%3A%22%22%7D&sub_type=0&total_time=0&ts=1655220112&type=3&user_status=0&video_duration=232"}')'''

# 可以知道我们要的是元组的第二个元素
print(result[1],type(result[1]))
# 返回的是字符串
'''
{"tid": "71776e7d-36ee-4f33-a567-cd39addcf3ce", "data": "actual_played_time=0&aid=851776257&appkey=1d8b6e7d45233436&auto_play=0&build=6240300&c_locale=zh_CN&channel=xxl_gdt_wm_253&cid=516350598&epid=0&epid_status=&from=6&from_spmid=tm.recommend.0.0&last_play_progress_time=0&list_play_time=0&max_play_progress_time=0&mid=0&miniplayer_play_time=0&mobi_app=android&network_type=1&paused_time=0&platform=android&play_status=0&play_type=1&played_time=0&quality=80&s_locale=zh_CN&session=897a6991b1f7489f915e420c9b82136d9c5dec62&sid=0&spmid=main.ugc-video-detail-vertical.0.0&start_ts=0&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.24.0%22%2C%22abtest%22%3A%22%22%7D&sub_type=0&total_time=0&ts=1655220112&type=3&user_status=0&video_duration=232"} <class 'str'>'''

#我们要的是将其序列化之后的字典的data键对应的值
data = json.loads(result[1])
print(data['data'])