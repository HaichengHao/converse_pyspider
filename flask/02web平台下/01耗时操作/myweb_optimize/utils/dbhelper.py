"""
@File    :dbhelper.py
@Editor  : 百年
@Date    :2025/6/23 19:41 
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


def dbverify(sql, params):
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    result = cursor.fetchall()
    return result


def add_user(name, pwd):
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute("insert into user_info(account_name,pwd) values (%s,%s)", (name, pwd))
    conn.commit()
    conn.close()


def add_info(name, pwd, uid):
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute("insert into jd(username,pwd,uid) values (%s,%s,%s)", (name, pwd, uid))
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return new_id


def show_info(uid,per_page_count,offset):
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute("select username,pwd,status from jd where uid = %s order by id desc limit %s offset %s", (uid,per_page_count,offset))
    result = cursor.fetchall()
    return result

def get_count(uid):
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute("select count(*) from jd where uid = %s",(uid,))
    result=cursor.fetchone()
    return result

def getinfo():
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute("select * from user_info")
    result = cursor.fetchall()
    return result

