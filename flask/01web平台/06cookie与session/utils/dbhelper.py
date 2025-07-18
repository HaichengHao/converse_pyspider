"""
@File    :dbhelper.py
@Editor  : 百年
@Date    :2025/6/15 21:32 
"""
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
    cursorclass = pymysql.cursors.DictCursor

)

def dbverify(sql,params):
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute(sql,params)
    result = cursor.fetchall()
    return result

def add_user(name,pwd):
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute("insert into user_info(account_name,pwd) values (%s,%s)",(name,pwd))
    conn.commit()
    conn.close()

# if __name__ == '__main__':
#     # res = dbverify(sql='select * from user_info where account_name=%s and pwd=%s',params=('qw','1234'))
#     res = add_user("李二虎","12345678")
#     print(res)

