# editor: 百年
# time: 2024/3/9 15:02
login_Flag=False #默认的登录标识为false,即默认未登录
def login(fn):
    def inner(*args, **kwargs):
        print('还未完成登录操作')
        # 这里完成登录校验
        global login_Flag
        if login_Flag==False:   #如果没登录，则进入登录操作
            while 1:
                username=input('请输入用户名')
                passwd=input('请输入密码')
                if username == 'admin':
                    if passwd=="123456":
                        print('登陆成功')
                        # 如果登录成功就将全局变量改为True，这样在进行操作时就不用重复登录
                        login_Flag=True
                        break
                    else:
                        print('登录失败，用户名或密码错误')

        res=fn(*args, **kwargs)
        print('操作结束')
        return res
    return inner

@login
def add():
    print('增加员工信息')
@login
def mofy():
    print('修改员工信息')
@login
def delt():
    print('删除学生信息')

add()
delt()

''' 运行结果
还未完成登录操作
请输入用户名admin
请输入密码123456
登陆成功
增加员工信息
操作结束
还未完成登录操作
删除学生信息
操作结束
'''