# @Author    : 百年
# @FileName  :02_python连接sqlite.py
# @DateTime  :2024/10/26 21:34
import sqlite3
# sqlite创建连接对象十分简单，但是还是回顾一下pymysql更好
conn = sqlite3.connect('spider3.db')
cursor = conn.cursor()

# 给class表增加一行数据
cursor.execute("insert into class values ('5','初三');")
cursor.execute('select * from class;')
result1 = cursor.fetchall()
# 注意，我们这样并没有提交事务，所以并不会有改变，如果真想改变表需要加上下面一行代码
conn.commit()#如果事务不提交则写入操作无法持久化
# print(result)
for item in result1:
    print(item)
#     关闭游标和sql连接
cursor.close()
conn.close()