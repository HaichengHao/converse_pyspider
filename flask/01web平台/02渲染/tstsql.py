"""
@File    :tstsql.py
@Editor  : 百年
@Date    :2025/6/15 13:36 
"""
import pymysql
conn = pymysql.Connection(
    host='localhost',
    port=3306,
    user='root',
    password='HHCzio20',
    # charset='utf-8',
    database='flaskdemo',
    cursorclass=pymysql.cursors.DictCursor  # 关键点
)


cursor = conn.cursor()
cursor.execute('select * from user_info')

#直接查看表头
# cursor.execute('select column_name from information_schema.columns where table_name="user_info";')
result = cursor.fetchall()
# print(result,type(result))

# ((1, '张三', '123456', '张先生', 0, '男', None, None),
# (2, '西北锤王', '1234321', '孙少安', 1, '男', None, None),
# (3, '谢尔比', 'SHERLL', 'sr', 1, '男', None, None),
# (4, '乔布斯', '123455', 'jobs', 1, '男', None, None)) <class 'tuple'>

'''
返回的是元组'''
for item in result:
    print(item)


