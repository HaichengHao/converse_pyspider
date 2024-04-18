# editor: 百年
# time: 2024/3/9 9:44
# def magic(game):
#     def inner(*args, **kwargs):
#         print('外挂开')
#         res=game(*args, **kwargs)  #这里是目标函数的执行，这里是能够拿到从目标函数返回的返回值的
#         print('外挂关')
#         return res  #inner里也有返回值了
#     return inner
#
# @magic  #相当于lol=magic(lol) 即lol = inner
# def lol(username,passwd,hero):
#     print(f'登录用户为{username},密码{passwd},英雄{hero}')
#     return '一波平推，对面都来不及投'
# # lol(username='马画藤',passwd='12312',hero='寡妇')
#
# res=lol(username='马画藤',passwd='12312',hero='女警')
# print(res)
''' 未开启magic,如果加上@magic便会有None，思考原因,因为inner函数里并没有返回值
登录用户为马画藤,密码12312,英雄女警
一波平推，对面都来不及投
None
'''

# 在inner中进行修改
# 将game(*args,**kwargs) 赋值于res
# 并在inner中返回res

''' 总结：
def wrapper(fn):  wrapper:装饰器 fn: 目标函数
    def inner(*args,**kwargs):
      #在目标函数执行之前的操作代码
      res=fn(*args,**kwargs)  #执行目标函数  <--与上一结p30相比，
      #在目标函数执行之后进行的操作
      return res #  <--与p30相比，对res进行了返回，让inner()进行返回
    return inner <--记住，一定要返回inner函数，记住不能加括号，加括号就是把目标函数执行的结果返回

@wrapper #利用装饰器 即调用inner,注意是调用，并不是执行inner()
def target():
    pass

target() --> 即 inner() ，执行inner函数 
'''
# 这个便是通用装饰器的写法，不再是雏形

# 其它情况
# 一个函数被多个装饰器装饰

def wrapper_1(fn): # fn=wrapper_2.inner
    def inner(*args,**kwargs):
        print('这里是wrapper_1,开始') #1
        res=fn(*args,**kwargs)   #2 wrapper_2.inner()
        print('这里是wrapper_1,结束')#8
        return res#9
    return inner#10

def wrapper_2(fn): #wrapper_2(target)
    def inner(*args,**kwargs):
        print('这里是wrapper_2,开始')#3
        res=fn(*args,**kwargs)  #4 target()，即打印出'我是个目标函数'
        print('这里是wrapper_2,结束')#5
        return res#6
    return inner#7


@wrapper_1 #target=wrapper_1(target) =>此时后面小括号的target是wrapper2.inner ,即target=wrapper_1(wrapper2.inner)而等号前面的target从简单理解上看
# 其就是wrapper1.inner,如果有疑惑，记得观察返回值类型
@wrapper_2 #target=wrapper_2(target) => 此时等号前面的target: wrapper2.inner
def target():
    print('我是个目标函数')#4

target()

'''
这里是wrapper_1,开始
这里是wrapper_2,开始    <--经过观察发现，可以想象成目标函数先被wrapper_2套住，后被wrapper_1套住
我是个目标函数
这里是wrapper_2,结束
这里是wrapper_1,结束
'''


# 尝试另一种方式
@wrapper_2
@wrapper_1
def target_2():
    print('我是目标函数2')
target_2()
'''
这里是wrapper_2,开始
这里是wrapper_1,开始
我是目标函数2
这里是wrapper_1,结束
这里是wrapper_2,结束'''

'''
记住规则规律
@wrapper1
@wrapper2
def target():
    pass
target()

那么，结果会是
wrapper1 wrapper2 target() wrapper2 wrapper1'''

