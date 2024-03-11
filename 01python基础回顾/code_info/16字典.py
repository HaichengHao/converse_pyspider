# editor: 百年
# time: 2024/3/3 10:05
# 字典是以键值对的方式存储数据的
# 字典的标识方式{key:value}
'''
dic1={'张三':20,'李四':23}

# 字典的取值法
# .get(key)法
# 索引法set[key]
print(dic1.get('张三'))
# 20
print(dic1['张三'])
# 20

try:
    dic2={[1,2]:20}
except BaseException as e:
    print(e)
  #   unhashable type: 'list'
#   字典的键必须是可哈希的数据类型

try:
    set4={'李四':[20,12]}
    print(set4)
except BaseException as e:
    print(e)
# {'李四': [20, 12]} <--字典的键可以是任何数据类型'''

# # 2字典的增删改查
# dic_1={'李四':30,'王五':25,'钱六':66}
# dic_1['张三']=20
# print(dic_1)
# # {'张三': 20}
#
# #字典中不可出现重复的key,若key重复指定value,则会按最后一个value修改
# dic_1['张三']=23
# print(dic_1)
# # {'张三': 23} <--变成了修改的操作
#
# dic_1.setdefault('张中三','张老三')  # setdefault设置的是默认值
# print(dic_1)
# # {'李四': 30, '王五': 25, '钱六': 66, '张三': 23, '张中三': '张老三'}
#
# # 尝试再设置默认值
# try:
#     dic_1.setdefault('张中三',22)
#     print(dic_1)
# #     {'李四': 30, '王五': 25, '钱六': 66, '张三': 23, '张中三': '张老三'}  <--可以发现，默认值指定过后再次指定不会发生变化
# except BaseException as e:
#     print(e)
#
# # 字典元素的删除
# # .pop('key') <--根据key删除
# dic_1.pop('张三')
# print(dic_1)
# # {'李四': 30, '王五': 25, '钱六': 66, '张中三': '张老三'}
#
# # del dic['key']
# del dic_1['钱六']
# print(dic_1)
# # {'李四': 30, '王五': 25, '张中三': '张老三'}
#
# # 查
# print(dic_1.get('李四'))
# # 30
# print(dic_1['李四'])
# # 30
#
# print(dic_1.get('小明'))
# # None 《--get取值法对于取不到的值会返回None
#
#
# # print(dic_1['小明'])
# '''
# Traceback (most recent call last):
#   File "D:\converse_fullstack\converse\01python基础回顾\code_info\16字典.py", line 74, in <module>
#     print(dic_1['小明'])
# KeyError: '小明'
#
# Process finished with exit code 1
# '''
# # 可以发现dic['key']在有不存在的key时会报错
#
# # 空None
# a=None #单纯的空就是空，什么操作也干不了
# print(type(a))
# # <class 'NoneType'>
'''
# 字典的循环
dic1={
    '张三':'爱吃面',
    '李四':'爱吃米饭',
    '王五':'爱吃炸鸡',
    '陈六':'爱吃牛肉'
}
# 遍历键可以得到键，之后便可通过dic[key]取值法得到键对应的值
# 1 利用for 循环
for key in dic1:
    print(dic1[key])
# 爱吃面
# 爱吃米饭
# 爱吃炸鸡
# 爱吃牛肉

# 2 希望把所有的key全部保存在一个列表中
print(dic1.keys())
# dict_keys(['张三', '李四', '王五', '陈六'])
print(type(dic1.keys()))
# <class 'dict_keys'>
print(list(dic1.keys())) #这样可以拿到所有的key了
# ['张三', '李四', '王五', '陈六']


# 拿到所有的value
print(dic1.values())
print(type(dic1.values()))
# dict_values(['爱吃面', '爱吃米饭', '爱吃炸鸡', '爱吃牛肉'])
# <class 'dict_values'>
print(list(dic1.values()))
# ['爱吃面', '爱吃米饭', '爱吃炸鸡', '爱吃牛肉']

print(dic1.items())
print(type(dic1.items()))
# dict_items([('张三', '爱吃面'), ('李四', '爱吃米饭'), ('王五', '爱吃炸鸡'), ('陈六', '爱吃牛肉')])
# <class 'dict_items'>
print(list(dic1.items()))
# [('张三', '爱吃面'), ('李四', '爱吃米饭'), ('王五', '爱吃炸鸡'), ('陈六', '爱吃牛肉')]
# 会返回一个有键值对组成的元组作为其元素的列表
#
# for item in dic1.items():
#     print(item)
    # ('张三', '爱吃面')
    # ('李四', '爱吃米饭')
    # ('王五', '爱吃炸鸡')
    # ('陈六', '爱吃牛肉')
for item in dic1.items():
    key=item[0]
    value=item[1]
    print(key, value)
    # 张三 爱吃面
    # 李四 爱吃米饭
    # 王五 爱吃炸鸡
    # 陈六 爱吃牛肉

a_,b_=(1,2)  #元组或者列表都可以进行这个操作，这个操作称为解构或者解包
print(a_,b_)
# 1 2

# 利用上面的解包思路我们可以进行如下操作
for item in dic1.items():
    key,value=item #<--在上面的案例中我们知道item是(key,value)组成的列表，所以其可以解包
    print(key, value)
# 张三 爱吃面
# 李四 爱吃米饭
# 王五 爱吃炸鸡
# 陈六 爱吃牛肉
# 发现解包操作也是可以的

# 其实可以直接简写
for key,value in dic1.items():
    print(key, value)'''

# 字典的嵌套
# 注意字典的值可以是任何数据形式
zhangsan={
    'name':'张三',
    'gender':'male',
    'age':20,
    'address':{
        'city':'长沙',
        'province':'湖南'
    },
    'friends':[
        {'李四':{
            'age':19,
            'gender':'male',
            'girlfriend':{
                'name':'翠花',
                'age':18,
                'friends':[
                    {'小芳':{
                        'age':18,
                        'gender':'female',
                    }},
                    {'娟子':{
                        'age':20,
                        'hobby':'篮球'
                    }}
                ]
            }
        }},
        {'王五':{
            'age':22,
            'gender':'male',
        }}
    ]
}

# 这样的一个场景，张三想知道朋友李四的女朋友的朋友娟子的年龄
print(zhangsan['friends'][0]['李四']['girlfriend']['friends'][1]['娟子']['age'])
# 20


dic1={
    '张三':'爱吃面',
    '李四':'爱吃米饭',
    '王五':'爱吃炸鸡',
    '陈六':'爱吃牛肉',
    '王琦':'爱吃饺子'
}
# 删除姓王的
'''
for key in dic1:
    if key.startswith('王'):
        del dic1[key]
    else:
        continue
    print(dic1)'''
#     RuntimeError: dictionary changed size during iteration
# 这样写会报错
# 字典在迭代和循环的时候大小发生了改变
# 注意这里比对列表那一节进行学习，创建一个临时的列表进行存储要删除的数据，最后读取要删除数据的key再删除掉原字典的元素
temp=[]
for key in dic1:
    if key.startswith('王'):
        temp.append(key)
    else: #否则key不变
        key=key
print(temp) #先打印输出看看有无获取到符合删除要求的键
# ['王五', '王琦'] 《--获取到了
# 之后遍历temp将符合条件的键值对进行删除
for del_key in temp:
    del dic1[del_key]
print(dic1) #再次打印发现删除了要删除的元素
# {'张三': '爱吃面', '李四': '爱吃米饭', '陈六': '爱吃牛肉'}
# 可以


# 补充
# 字典可以通过.update({key: value})的方式新增数据