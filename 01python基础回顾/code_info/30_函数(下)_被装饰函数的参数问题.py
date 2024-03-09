# editor: 百年
# time: 2024/3/9 9:11
# def magic(game):
#     def inner():
#         print('外挂开启')
#         game()
#         print('外挂关闭')
#     return  inner
#
# @magic  #这里就相当于 lol = magic(lol)  也可理解为是inner
# def lol():
#     print('英雄联盟开启')
#
# @magic
# def crossfire():
#     print('穿越火线开启')
#
# # 使用
# lol()  #<--这里即相当于inner() ，即执行了inner函数
# crossfire() #与上面同理
# '''  运行结果:
# 外挂开启
# 英雄联盟开启
# 外挂关闭
# 外挂开启
# 穿越火线开启
# 外挂关闭
# '''


def magic(game):
    def inner(*args, **kwargs):  #inner添加了参数，利用可变位置参数和可变关键字参数可以接收任何参数
        print('外挂开启')
        game(*args, **kwargs)  #利用解包赋值，打散位置参数和关键字参数，注意和上面的*args和**kwargs含义有所不同
        print('外挂关闭')
    return inner



@magic
def lol(username,passwd,hero):
    print(f'游戏账号:{username},游戏密码:{passwd},英雄:{hero}')
    print('英雄联盟开启')

@magic
def crossfire(username,passwd,main_weapon):
    print(f'用户名{username},密码{passwd},主武器:{main_weapon}')
    print('穿越火线开启')

# 使用
lol(username='德玛西亚的王',passwd='123456',hero='盖伦')  #<--这里即相当于inner() ，即执行了inner函数
#解析：相当于inner(username='德玛西亚的王',passwd='123456',hero='盖伦')
# 之后在inner函数中进行game(username='德玛西亚的王',passwd='123456',hero='盖伦'),
# 作用在外部即表现为lol(username='德玛西亚的王',passwd='123456',hero='盖伦')


# 使用
crossfire(username='小趴菜',passwd='12312',main_weapon='m4a1')


''' 与p29比较，仅仅是在传参时对inner增加了参数以及对目标函数增加了解包的参数，且均为万能接收的*args和**kwargs
def wrapper(fn):  wrapper:装饰器 fn: 目标函数
    def inner(*args,**kwargs):
      #在目标函数执行之前的操作代码
      fn(*args,**kwargs)  #执行目标函数
      #在目标函数执行之后进行的操作
    return inner <--记住，一定要返回inner函数，记住不能加括号，加括号就是把目标函数执行的结果返回
'''
