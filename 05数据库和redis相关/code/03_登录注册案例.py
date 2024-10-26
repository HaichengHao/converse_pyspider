# @Author    : 百年
# @FileName  :03_登录注册案例.py
# @DateTime  :2024/10/26 22:18
import sqlite3
conn = sqlite3.connect('spider3.db')
cursor = conn.cursor()

# 注册功能
# 理清逻辑,判断密码的输入
# username = input('请输入用户名>>')
while True:
    username = input('请输入用户名>>')
    # 判断该用户名是否被注册
    res0 = cursor.execute('select uname from users where uname = (?) ',(username,))
    res0=cursor.fetchone()
    if res0 == None:
        passwd = input('请输入密码>>')
        repeat_pwd = input('再次输入密码>>')
        mail = input('请输入邮箱>>')
        if passwd == repeat_pwd:
            cursor.execute("insert into users(uname,pwd,email) values (?,?,?);",(username,passwd,mail))
            conn.commit()
            print('注册成功')
            break
        else:
            print('两次密码不一致，请重新输入')
            continue
    else:
        print('该用户名不可用')
        continue