"""
@File    :dbhelper.py
@Editor  : 百年
@Date    :2025/7/31 9:22 
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
    cursorclass=pymysql.cursors.DictCursor

)

def showdata():
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute("select * from jd order by id desc ")
    result = cursor.fetchall()
    return result