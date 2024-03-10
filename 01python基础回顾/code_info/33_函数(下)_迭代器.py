# editor: 百年
# time: 2024/3/9 15:41
'''
最初的python学习中，我们经常会使用for 循环来做迭代
例如
for 变量 in 可迭代对象(iterable)  常用iterable对象 str lst tuple dict set
    pass
迭代器:iterator
可迭代的数据类型都会提供一个叫迭代器的东西，这个迭代器可以帮我们把数据类型中的所有数据逐一拿到
'''


# # 获取迭代器的两种方案
# #     1  iter(可迭代对象)   内置函数，可以直接拿到迭代器
# it_s='人生苦短'
# it=iter(it_s)  #创建迭代器it
# print(it)
# # <str_iterator object at 0x00000292C82DDB40> <--字符串迭代器
#
# # 第二种创建迭代器的方法
# # iterable.__iter__()  特殊方法，使用较少
# it2=it_s.__iter__()
# print(it2)
#
# # 从迭代器中拿到数据的两种方案
# #     1  next(迭代器)
#
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# # 人
# # 生
# # 苦
# # 短
# # 这里要注意，利用next()一定要关注可迭代对象的长度
#
# # 这里尝试超限输出迭代器对象中拿到的数据
# # print(next(it))
#
# '''
# StopIteration <--报错信息:停止了迭代，即迭代器中已经没有数据可取了，换言之，即迭代结束了'''
#
# # 第二种从迭代器中拿数据的方案
# print(it2.__next__())
# print(it2.__next__())
# print(it2.__next__())
# print(it2.__next__())
# # 人
# # 生
# # 苦
# # 短

# 模拟for 循环的工作原理
str1='我是测试用字符串'
it = iter(str1) #创建迭代器

while 1:   #这就相当于for循环的循环体
    try:
        data=next(it)
        print(data)
    except StopIteration:  #如果超限，则结束循环从迭代器中取出数据的操作
        break
'''
我
是
测
试
用
字
符
串
'''

# for 循环里一定是要拿迭代器的，所以所有不可迭代的东西不能用for循环
# for 循环里面一定有next出现
# 迭代器统一了所有不同类型数据的遍历工作

#补充：
# 迭代器本身也是可被迭代的内
str_demo='你好Python'
it=iter(str_demo)
# <str_iterator object at 0x000001BD1B963FA0>
print(it)
for item in  it:
    print(item)
'''
你
好
P
y
t
h
o
n'''

# 迭代器本身的特性
# 1.只能向前，不能反复
# 2.特别节省内存
# 3.惰性机制