"""
@File    :01python链接redis.py
@Editor  : 百年
@Date    :2024/12/21 23:35 
"""

# 注意redis2.10.6可以将字典写入进redis数据库

import redis
# 创建连接对象
conn = redis.Redis(host='127.0.0.1',port=6379)
print(conn)
'''
D:\venvs\converse_pyspider\Scripts\python.exe E:/converse_spider/converse_pyspider/05数据库和redis相关/03Redis学习/code/01python链接redis.py
Redis<ConnectionPool<Connection<host=127.0.0.1,port=6379,db=0>>>
可以看到我们已经连接成功'''

# 插入数据

# IMPORTANT:需要重点练习的有字典类型和列表类型
# IMPORTANT:字典类型
# result = conn.sadd('class','num3')
# print(result) #注意:redis数据库中插入成功就会返回1否则返回0

'''
1 <--说明插入成功，我们可以去client端查看是否插入成功
'''
# 或者这样来看看我们到底插入成功了没有
result = conn.smembers('class')
print(result)
# {b'num1', b'num3'} <--可以看到返回的结果显示numb3确实是插入成功了
# QUIZ：为什么返回的字典类型数据的前面加上了个b?
# ANSWER:因为redis数据库默认存储的字典数据是二进制数据


# IMPORTANT:列表类型

result2 = conn.lpush('hobby','animate')
print(result2)
conn.smembers('class')
# 6 <--最开始插入的是五条数据，这里又加了一条说明我们已经插入数据成功了