# @Author    : 百年
# @FileName  :04_转账案例.py
# @DateTime  :2024/10/27 10:04
import sqlite3
conn = sqlite3.connect('spider3.db')

cursor = conn.cursor()

# 转账的思路，一个人转给另外一个人，转账人的余额减去a,被转账人余额加上a,同时发生
try:
    cursor.execute("update bank set mony = mony - 200 where name='王保强';")
    cursor.execute("update bank set mony = mony +  200 where name = '刘墙东';")
    conn.commit()
    print('操作成功')
except BaseException as e:
    print(e)
    conn.rollback() #如果失败就回滚到未修改的表

cursor.close()
conn.close()



