# editor: 百年
# time: 2024/3/7 9:55
# def func1():
#     a=29
#     def func2(): #在函数内声明函数func2()
#         pass
#      #<--局部函数只能在允许的局部作用域内访问
#     print(a)
#     func2()
# print(func1())

'''
# 案例
def func1():
    print(1)   #1<--先执行输出1
    def func2():
        print(2)  #4 <--func2被调用，先输出2
        def func3(): # 7<--func3被调用
            print(3) # 8<--输出3
        print(4)  #5 <--输出4
        func3()  # 6 <--调用func3
    print(5)  #2<--再输出5
    func2()  #3 《--调用func2
func1()
# 1
# 5
# 2
# 4
# 3'''

# 如果函数内声明的函数就想在外部使用，就把函数像变量一样返回
'''
def func1():
    def func2():
        print(2)
    return func2 #注意，返回的是函数，可不能加括号，加了括号代表的是返回函数执行后的结果
func1()  # <--只是这样写表示执行函数func1，不会报错，但什么都看不见
a=func1() #利用一个变量接收函数func1执行后返回的结果
print(a) # 并将其打印输出
# 可以看到如下结果，即函数func1内部的函数func2已经暴露在函数外部
# <function func1.<locals>.func2 at 0x000001FEF4769000>
# 注意，如果是局部变量会带有<locals>全局的话则不带
a()  #相当于函数func2已经暴露在函数外部，故只需利用()即表示将函数func2执行的结果返回
# 2'''


'''# 简单理解
def a():
    print(123)

# 如果调用函数并执行，只需函数名加括号即可
# a()
# 123

# 但是如果把函数赋给一个新的对象，并保留即可调用有可执行的功能，
# 只需 新的对象名= 函数名  <--注意带括号代表把执行后的结果赋给新对象
myfunc=a

print(myfunc,a)
# <function a at 0x000002D66DB73EB0> <function a at 0x000002D66DB73EB0>
# 可见就是指针重新分给myfunc 原来的a并没有变化

# 如果调用新的对象来执行函数，只需在其后加上括号即可
myfunc()
# 123 '''

# 定义一个让函数执行的函数act_myfunc
def act_myfunc(func):
    func()
def func1():
    print('你好世界')

act_myfunc(func1) #<--调用函数act_myfunc执行func1
# 你好世界
try:
    act_myfunc(func1())
except BaseException as e:
    print(e)
#     你好世界
# 'NoneType' object is not callable
# 可见这样写调用函数是错误的，因为func1()代表执行结果而不是函数本身

# 以上，调用函数来执行另一个函数被称为代理模式
# 总结
#     函数可以作为返回值进行返回
#     函数可以作为参数进行互相传递
#     函数名本质上就是一个变量名，本质就是个内存地址