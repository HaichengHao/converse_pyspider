# @Author    : 百年
# @FileName  :00生成uuid(补充内容).py
# @DateTime  :2024/10/28 10:37
'''
写这个是方便进行基于数据库授权的,
而且方便给别的用户使用自己的程序这样可以直接写表
'''
import uuid
import sqlite3

conn = sqlite3.connect('uandt.db')

cursor = conn.cursor()

name = input('请输入用户名>>')
token = uuid.uuid4() #直接随机生成uuid
token=str(token) #sqlite不支持直接的uuid格式，为了方便存储可以将其改为字符串格式

cursor.execute('insert into user(name,tokens) values (?,?)',(name,token))

conn.commit()
print('插入成功')
cursor.close()
conn.close()


# mysql写法
# import mysql.connector
# conn = mysql.connector.connect(
#     host = 'localhost',
#     port = 3306,
#     user='root',
#     password='',
#     database = 'spider',
#     charset = 'utf-8'
# )
# cursor = conn.cursor()
# cursor.execute("insert into user(name,token) values ('%s','%s') "%(name,token))
# conn.commit()
# cursor.close()
# conn.close()