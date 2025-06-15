import pymysql
from dbutils.pooled_db import PooledDB

pool_mysql = PooledDB(
    creator= pymysql,
    mincached=2,
    maxcached=5,
    maxconnections=10,
    setsession=[],
    host='127.0.0.1',
    port = 3306,
    user='root',
    password='HHCzio20',
    database='flaskdemo',
    cursorclass=pymysql.cursors.DictCursor  #指定后返回的将是字典类型的数据
    
)


def dbverify(sql):
    conn = pool_mysql.connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall() 
    return result

# if __name__ == '__main__':
#     res = dbverify('select * from user_info')
#     print(res)