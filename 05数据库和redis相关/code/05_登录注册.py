# @Author    : 百年
# @FileName  :05_登录注册.py
# @DateTime  :2024/10/27 10:41
import sqlite3

conn = sqlite3.connect('spider3.db')

cursor = conn.cursor()


# 注册函数
def regist():
    username = input('请输入用户名>>')
    cursor.execute("select uname from users where uname = (?);", (username,))
    res = cursor.fetchone()
    if res == None:
        while True:
            passwd = input('请输入密码>>')
            repeat_passwd = input('请再次输入密码>>')
            if passwd == repeat_passwd:
                email = input('请输入邮箱>>')
                cursor.execute("select email from users where email = (?);", (email,))
                res1 = cursor.fetchone()
                if res1 == None:
                    cursor.execute("insert into users(uname,pwd,email) values (?,?,?);", (username, passwd, email))
                    conn.commit()
                    print('注册成功')
                    break
                else:
                    print('该邮箱已经存在，请勿重复注册')
            else:
                print('两次密码不一致，请重新输入')
                continue
    else:
        print('该用户名已经存在，请重新输入')


# 登录函数
def login():
    username = input('请输入用户名>>')
    passwd = input('请输入密码>>')
    cursor.execute("select uname,pwd from users where uname=(?) and pwd=(?);", (username, passwd))
    res2 = cursor.fetchone()
    if res2 == None:
        print('您并未注册，请先注册>>')
    else:
        print('欢迎登录!!')


# def prelogin(fn):
#     def inner(*args,**kwargs):
#         username = input('请输入用户名>>')
#         passwd = input('请输入密码>>')
#         cursor.execute("select uname,pwd from users where uname=(?) and pwd=(?);", (username, passwd))
#         res2 = cursor.fetchone()
#         if res2 == None:
#             print('您并未注册，请先注册>>')
#         else:
#             print('欢迎登录!!')
#             res = fn(*args, **kwargs)
#             return res
#     return inner()

# 修改密码的前提是你已经登录成功

def chpwd():
    login()
    username=input('请再次输入用户名>>')
    newpwd = input('请输入新的密码>>')
    repeat_newpwd = input('请再次输入新的密码>>')
    if newpwd == repeat_newpwd:
        cursor.execute('update users set pwd=(?) where uname = (?);',(newpwd,username))
        conn.commit()
        print(f'修改成功,新密码请牢记:{newpwd}')
        cursor.close()
        conn.close()
    else:
        print('两次密码不一致请重新输入')

# 找回密码
def findpwd():
    count = 0
    while True:
        # 次数限定为3
        if count==3:
            print('多次尝试失败')
            return
        username=input('请再次输入用户名>>')
        email = input('请输入注册时用的邮箱>>')
        cursor.execute('select * from users where uname=(?) and email=(?)',(username,email))
        res = cursor.fetchone()
        if res == None:
            count += 1
            print('输入信息有误，请重新输入')
            continue
        else:
            cursor.execute('select pwd from users where uname=(?);',(username,))
            res1 = cursor.fetchone()
            print(res1[0])
            cursor.close()
            conn.close()
            break


# 主函数
if __name__ == '__main__':
    # regist()
    # login()
    chpwd()
    # findpwd()
    # code = findpwd()