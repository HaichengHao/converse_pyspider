"""
@File    :worker.py
@Editor  : 百年
@Date    :2025/6/30 23:24 
"""
#important:注意这个是worker,用来拿到队列中的值并进行操作,关注具体的逻辑即可,仅仅是对00web服务中09的细小改动
'''
从队列中去获取任务,执行并写入到结果队列
'''
import json
import redis
import hashlib
import pymysql
from dbutils.pooled_db import PooledDB

POOL = PooledDB(
    mincached=2,
    maxcached=5,
    maxconnections=10,
    creator=pymysql,
    setsession=[],
    user='root',
    host='localhost',
    port=3306,
    password='HHCzio20',
    database='flaskdemo',
    cursorclass=pymysql.cursors.DictCursor

)


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

def getinfo(taskid):
    conn = POOL.connection()
    cursor = conn.cursor()
    # new_id = cursor.lastrowid
    cursor.execute("select * from jd where status=1 and id=%s",(taskid,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

#important:定义刷新状态的方法
def refresh_status(taskid,stacode):
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute("update jd set status=%s where id=%s",(stacode,taskid))
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return result

def get_task():
    data = conn.brpop(TASK_QUEUE, timeout=10) #block right pop 阻塞形态右边出队
    # 作判断,
    if not data:
        return  # 如果没有数据就返回None

    # print(data)
    return json.loads(data[1])  #important: 因为pop取出来的是数组形式且元素是字节形式


def set_result(taskid, value):
    conn.hset(RESULT_QUEUE, taskid, value)


def run():
    while True:
        # step1:从redis中获取任务
        taskid = get_task()
        print(taskid)
        if not taskid:
            continue

        # encrypt_string = str(taskid) + "560c52ccd288fed045859ed18bffd973"
        # obj = hashlib.md5(encrypt_string.encode('utf-8'))
        # sign = obj.hexdigest()
        #
        # # 写入到结果队列
        # set_result(taskid, sign)
        #step2:
        #tips:还没完呢,还需要修改mysql中的状态设置
        row_dict = getinfo(taskid=taskid)
        if not row_dict:
            continue
        #tips:然后将其状态刷新为正在执行状态
        refresh_status(taskid=taskid,stacode=2)
        # if not sta:
        #     continue
        #step3:然后执行任务,并将结果写入到结果队列
        encrypt_string = str(taskid) + "560c52ccd288fed045859ed18bffd973"
        obj = hashlib.md5(encrypt_string.encode('utf-8'))
        sign = obj.hexdigest()
        # 写入到结果队列
        set_result(taskid, sign)
        print('finished')

        #step4:写入完毕之后更新状态,将状态码设置为0表示已经执行完毕
        refresh_status(taskid=taskid,stacode=0)





if __name__ == '__main__':
    run()
