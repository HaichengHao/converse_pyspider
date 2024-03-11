# editor: 百年
# time: 2024/3/11 9:28
'''
zip 把多个可迭代内容进行合并
locals 查看当前位置的局部变量的内容
globals 可以查看全局作用域的内容
sorted 排序
filter 筛选
map 映射
'''

# zip
# lst_k=['张三','李四','王五','赵六']
# lst_v=[20,23,25,27]
# lst_v2=['张氏春秋','李氏春秋','王氏春秋','赵氏孤儿']
# '''info_dic={}
# for k,v,v2 in zip(lst_k,lst_v,lst_v2):
#     info_dic.update({k:{v:v2}})
# print(info_dic)'''
# # {'张三': {20: '张氏春秋'}, '李四': {23: '李氏春秋'}, '王五': {25: '王氏春秋'}, '赵六': {27: '赵氏孤儿'}}
# info_lst=zip(lst_k,lst_v,lst_v2)
# print(info_lst)
# # <zip object at 0x000002A44D1E46C0>
# print(dir(zip))
# # ['__class__', '__delattr__', '__dir__',
# # '__doc__', '__eq__', '__format__', '__ge__',
# # '__getattribute__', '__gt__', '__hash__',
# # '__init__', '__init_subclass__', '__iter__',
# # '__le__', '__lt__', '__ne__', '__new__',
# # '__next__', '__reduce__', '__reduce_ex__',
# # '__repr__', '__setattr__', '__setstate__',
# # '__sizeof__', '__str__', '__subclasshook__']
#
# # 发现有__iter__应该是可迭代对象
# # 尝试输出
# print(next(info_lst))
# # ('张三', 20, '张氏春秋')  <--猜想确认
#
# # 利用生成器输出数据的方式进行输出
# print(list(info_lst))
# # [('李四', 23, '李氏春秋'), ('王五', 25, '王氏春秋'), ('赵六', 27, '赵氏孤儿')]
#
#


# # locals
# a=100
# print(locals()) #此时locals被写在了全局作用域范围内，此时看到的就是全局作用域中的内容
# # {'__name__': '__main__', '__doc__': '\nzip 把多个可迭代内容进行合并\nlocals 查看当前位置的局部变量的内容\n\n', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001E8BA370490>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\converse_fullstack\\converse\\01python基础回顾\\code_info\\37内置函数(下).py', '__cached__': None, 'lst_k': ['张三', '李四', '王五', '赵六'], 'lst_v': [20, 23, 25, 27], 'lst_v2': ['张氏春秋', '李氏春秋', '王氏春秋', '赵氏孤儿'], 'info_lst': <zip object at 0x000001E8BA3E4D80>, 'a': 100}
#
# def func1():
#     b=100
#     print(locals())
# func1()
# # {'b': 100}  #locals打印的就是当前作用域下的局部变量
#


# # globals  查看全局变量的内容
# print(globals())
# # {'__name__': '__main__', '__doc__': '\nzip 把多个可迭代内容进行合并\nlocals 查看当前位置的局部变量的内容\n\n', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000025C05830490>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\converse_fullstack\\converse\\01python基础回顾\\code_info\\37内置函数(下).py', '__cached__': None, 'lst_k': ['张三', '李四', '王五', '赵六'], 'lst_v': [20, 23, 25, 27], 'lst_v2': ['张氏春秋', '李氏春秋', '王氏春秋', '赵氏孤儿'], 'info_lst': <zip object at 0x0000025C058A29C0>, 'a': 100, 'func1': <function func1 at 0x0000025C05AE1990>}


# sorted
# lst=[1,2,5,3,4,7,6,9,8,0]
# print(sorted(lst))
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sorted(lst,reverse=True))
#
# # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#
# # 那么，汉字如何排序?
# # 这时候，就可以使用key来指定排序规则
# name_lst=['奥特曼','卡卡罗特','孙悟空','假面骑士圣刃','宇宙霹雳超级无敌铁金刚']
# # 定义排序规则函数sort_rule，要求按名字的长度进行排序
# # def sort_rule(item): #item对应的就是列表中每一项数据
# #     return len(item)
#
# # 也可以用lambda定义
# sort_rule=lambda item : len(item)
# # 但是我们又想到一件事，既然sort_rule就是为了排序而生，何必再专门定义呢？
# # 所以我们可以改写输出语句
# # print(sorted(name_lst,key=sort_rule))  #注意别写成sort_rule() 因为这样返回的是函数执行后的结果
# #改写输出语句
# print(sorted(name_lst,key=lambda x:len(x)))
# # ['奥特曼', '孙悟空', '卡卡罗特', '假面骑士圣刃', '宇宙霹雳超级无敌铁金刚']
# # 注意！！！！！ 为何可以这样写呢？因为name_lst是可迭代对象，lambda可以将列表中的每一个元素作为迭代器进行迭代
# # 这样之后所做的操作便可将列表中的每个元素都迭代完，也拿到了返回的数据
# # 例如上面就是把名字列表中的每个元素(即名字)作为迭代对象一个个的进行len操作，便可按照名字的长度进行排序
#
# # 强化练习
# lst_demo=[
#     {'id':1,'name':'张三','age':18,'salary':5000},
#     {'id':2,'name':'李四','age':18,'salary':6000},
#     {'id':3,'name':'王五','age':16,'salary':2000},
#     {'id':4,'name':'陈六','age':19,'salary':20000},
#     {'id':5,'name':'赵七','age':19,'salary':1000}
# ]
# # 根据每个人的年龄排序
# print(sorted(lst_demo ,key=lambda x: x.get('age')))
# # 或者利用[]取值法
# print(sorted(lst_demo ,key=lambda x: x['age'] ))
# # [{'id': 3, 'name': '王五', 'age': 16, 'salary': 2000}, {'id': 1, 'name': '张三', 'age': 18, 'salary': 5000}, {'id': 2, 'name': '李四', 'age': 18, 'salary': 6000}, {'id': 4, 'name': '陈六', 'age': 19, 'salary': 20000}, {'id': 5, 'name': '赵七', 'age': 19, 'salary': 1000}]
#
# # 按薪水降序排序
# print(sorted(lst_demo,key=lambda x:x['salary'],reverse=True))
# # [{'id': 4, 'name': '陈六', 'age': 19, 'salary': 20000}, {'id': 2, 'name': '李四', 'age': 18, 'salary': 6000}, {'id': 1, 'name': '张三', 'age': 18, 'salary': 5000}, {'id': 3, 'name': '王五', 'age': 16, 'salary': 2000}, {'id': 5, 'name': '赵七', 'age': 19, 'salary': 1000}]



# filter
# filter( self,function_or_None, iterable)
# # filter(筛选的条件，可迭代对象)
# # 第一个参数function代表一个函数
# # 第二个参数代表的是可迭代对象
# # 工作原理和sorted很像，都是从可迭代对象中拿到元素
# #     用法 filter(过滤条件(一般是函数，而且是lambda表达式),可迭代对象(一般就是自己要进行过滤的数据))
# name_lst=['张三尼古拉斯','李四一代','王五大将军','陈六六','赵七伤剑']
# # 保留姓张的和姓陈的
# # 创建过滤器f
# f=filter(lambda x: x.startswith('张')|x.startswith('陈'),name_lst)
# print(f)
# print(list(f))
# # <filter object at 0x0000022462F8D570>  <--可见是一个过滤器对象,也可知道其就是一个生成器本质就是迭代器，利用next()可以逐个输出，或利用列表可迭代的特性输出list(迭代器对象)
# # ['张三尼古拉斯', '陈六六']
#
# # 抽查:再次打印
# print(list(f))
# # [] 老生常谈的话题，因为已经迭代完了，所以就没有了
#
# # 去除掉姓赵的
# f_2=filter(lambda x:not x.startswith('赵'),name_lst)
# print(list(f_2))
# # ['张三尼古拉斯', '李四一代', '王五大将军', '陈六六']



# map
lst=[2,4,1,3,6,5,7,8]
# 计算列表中每个数的平方
# 以前学过的解决方式
new_lst=[]
for i in lst:
    res=pow(i,2)
    new_lst.append(res)
print(new_lst)
# [4, 16, 1, 9, 36, 25, 49, 64]

# 或者
result=[i**2 for i in lst]
print(result)
# [4, 16, 1, 9, 36, 25, 49, 64]

# 新方法map
# map(function,iterable)
# 注意和filter进行比较，因为filter会把符合条件的对象进行保留，而map则是对整体进行操作
r=map(lambda x: pow(x,2),lst)
print(r)
# <map object at 0x00000214A21D3F10>  <--其本质还是一个迭代器
print(list(r))  #所以利用list()将其输出
# [4, 16, 1, 9, 36, 25, 49, 64]