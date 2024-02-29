# editor: 百年
# time: 2024/2/29 11:11
a=int(input('请输入数字1:'))
b=int(input('请输入数字2:'))
print('两者相加为:{0}'.format(a+b))


# 还有一些坑点
# 如果没有进行类型转换，会变成按照字符串类型拼接
c=input('请输入第一个数字')
d=input('请输入第二个数字')

print(c+d)

'''
请输入第一个数字3
请输入第二个数字2
32
'''

# 观察c,d两个变量的类型
print(type(c))
print(type(d))

'''
<class'str'>
<class'str'>
'''
# <class 'str'>
# <class 'str'>


# 进行强制类型转换后便可将数字字符串变成真正的数字类型
print(int(c)+int(d))

'''
请输入第一个数字3
请输入第二个数字2
5'''
