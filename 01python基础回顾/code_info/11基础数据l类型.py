# editor: 百年
# time: 2024/3/1 15:45
# int:整数，加减乘除，大小比较
# float:小数，浮点型

# print(10/3)
# 3.3333333333333335 <--并不是料想中的3.3333...

# 基础数据类型的转换
a='10'
print(type(a))
b=int(a)
print(type(b))
'''
<class 'str'>
<class 'int'>
'''

c=11
# 将其转化为布尔值
c_1=bool(c)
print(type(c_1),c_1)
# <class 'bool'> True

# 非零数字的布尔值皆为True


# 在python中表示空的东西都是Fals e
s1=''
print(bool(s1))
l1=[]
print(bool(l1))

# False
# False
