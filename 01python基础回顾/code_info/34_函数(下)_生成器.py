# editor: 百年
# time: 2024/3/10 9:28
# 生成器的本质就是迭代器

# 创建生成器(generator)的两种方案
# 1.生成器函数
#     生成器函数中有一个关键字yield
#     生成器执行的时候，得到的是生成器，并不会执行函数，得到的是生成器
#     只要函数中出现了yield,它就是一个生成器函数
#       yield的作用: 1 可以返回数据
#                   2 可以分段执行函数中的内容
'''
def func1():
    print('哈哈')
    yield 999  #yiled与return有不同之处，return是立即执行函数并返回结果，而yield只有执行到next的时候才会返回数据
res=func1()
# print(res)
# <generator object func1 at 0x0000021BE7AF83C0>
# 可见利用yield生成了一个生成器对象(generator object)
# 如何查看生成器生成的对象呢?因为其本质还是迭代器，所以可利用next来查看
print(next(res))  #或者写为res.__next__()
# 哈哈
# 999

# 注意，仍需关注StopIteration,因为本质是迭代器，所以也会遇到超限的问题
# print(next(res))'''
'''
Traceback (most recent call last):
  File "D:\converse_fullstack\converse\01python基础回顾\code_info\34_函数(下)_生成器.py", line 24, in <module>
    print(next(res))
StopIteration'''

# 可以分段执行函数中的内容
'''def func2():
    print(123)
    yield 666
    print(456)
    yield 999
#     在之前的学习中我们知道return执行之后，其后的内容将不再被执行
ret = func2()
# print(ret)
# <generator object func2 at 0x00000204F20D83C0>
print(next(ret))
# 123
# 666
# 接着输出
print(next(ret))
# 通过next(iter)可以执行到下一个yield的位置
# 456
# 999'''

# 生成器的使用场景
# 去工厂定制100件衣服
'''def order():
    lst=[]
    for i in range(100):
        lst.append(f'第{i+1}件')
    return lst
lst=order()
print(lst)'''
# ['第1件', '第2件', '第3件', '第4件', '第5件', '第6件', '第7件', '第8件', '第9件', '第10件', '第11件', '第12件', '第13件', '第14件', '第15件', '第16件', '第17件', '第18件', '第19件', '第20件', '第21件', '第22件', '第23件', '第24件', '第25件', '第26件', '第27件', '第28件', '第29件', '第30件', '第31件', '第32件', '第33件', '第34件', '第35件', '第36件', '第37件', '第38件', '第39件', '第40件', '第41件', '第42件', '第43件', '第44件', '第45件', '第46件', '第47件', '第48件', '第49件', '第50件', '第51件', '第52件', '第53件', '第54件', '第55件', '第56件', '第57件', '第58件', '第59件', '第60件', '第61件', '第62件', '第63件', '第64件', '第65件', '第66件', '第67件', '第68件', '第69件', '第70件', '第71件', '第72件', '第73件', '第74件', '第75件', '第76件', '第77件', '第78件', '第79件', '第80件', '第81件', '第82件', '第83件', '第84件', '第85件', '第86件', '第87件', '第88件', '第89件', '第90件', '第91件', '第92件', '第93件', '第94件', '第95件', '第96件', '第97件', '第98件', '第99件', '第100件']

# 想象一下这样的场景，一次不用生产100件，而是每天生产20件
'''def order():
    lst=[]
    for i in range(100):
        lst.append(f'第{i+1}件')
        if len(lst)==20:
            yield lst
#             下一次拿衣服
            lst=[] #清空列表，因为每次都是20件

lst=order()
print(next(lst))
# ['第1件', '第2件', '第3件', '第4件', '第5件', '第6件', '第7件', '第8件', '第9件', '第10件', '第11件', '第12件', '第13件', '第14件', '第15件', '第16件', '第17件', '第18件', '第19件', '第20件']
# 一次二十件

# 第二批
print(next(lst))
# ['第21件', '第22件', '第23件', '第24件', '第25件', '第26件', '第27件', '第28件', '第29件', '第30件', '第31件', '第32件', '第33件', '第34件', '第35件', '第36件', '第37件', '第38件', '第39件', '第40件']

# 生成器的优势，使用得当可以节省内存'''

# 第二种创建方法
# 2 生成器表达式
# 语法
# (数据 for循环 [if判断])

gen=(i**2 for i in range(10))
print(gen)
# <generator object <genexpr> at 0x0000023551B383C0>  #生成器对象
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# 0
# 1
# 4
# 9
# while 1:
#     try:
#         print(next(gen))
#     except StopIteration:
#         break
'''
0
1
4
9
16
25
36
49
64
81
'''

gen_lst=list(gen)
print(gen_lst)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 隐含内容，list和set本身就是有一个循环迭代在里边的
# 例如
s='周芷若'
lst=list(s)
print(lst)
# ['周', '芷', '若']

# 如果再次打印list(gen)会是一个空列表
print(list(gen))
# []
# 为什么呢，因为之前生成器的内容已经迭代完了