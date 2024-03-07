# editor: 百年
# time: 2024/3/7 16:50
'''
内容回顾：
    1.函数可以作为参数进行传递
    2.函数可以作为返回值返回
    3.函数名称可以像变量一样进行赋值操作

'''
# 回顾
'''
# 函数可以作为参数传递
# 函数可以作为返回值返回
def func1():
    print('我是一个函数')

def func2(fn): #定义一个执行函数的函数func2
    fn()

# 把函数func1作为参数传递到func2中，这样利用func2执行func1
# 即函数代理
func2(func1)'''

# 函数名可以像变量一样进行赋值操作
'''
def func1():
    print('我是函数1')
def func2():
    print('我是函数2')

# 将函数进行赋值操作，把func2赋值给func1
func1=func2
# 尝试执行func1看看是不是想要的结果
func1()
# 我是函数2 <--可见其本质上是运行了函数func2

'''

# 装饰器 >要求记住最后的结论
def play_lol():
    print('爱玩，虽然菜')
def play_cf():
    print('爱玩，虽然不准')
def play_qcar():
    print('爱玩，不会漂移')
# 打游戏想开挂，但是每次开启和关闭外挂都很麻烦
# print('开挂')
# play_cf()
# print('关闭外挂')

# 创建一个管家函数，能在打游戏前自动开启外挂，结束后自动关闭外挂
'''
def magic():
    print('外挂打开')
    play_lol()  #如果这样写，那就变成了函数代理的定义了，我们不想让管家magic帮我们决定游戏是否打开
    print('外挂关闭')

'''
# 所以，我们应该这样写
def magic():
    def inner():
        print('外挂开启')
        play_cf()
        print('外挂关闭')
    return inner()
