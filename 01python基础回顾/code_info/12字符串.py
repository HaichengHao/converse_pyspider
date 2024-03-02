'''# 1.字符串的格式化问题
# 我叫xxx,家住xxx,今年xxx岁，兴趣xxx

name=input('输入您的名字:')
address=input('输入您的家庭住址')
age=int(input('输入您的年龄:'))
interest=input('输入您的兴趣爱好:')


# 1 '{0}'.format()格式化字符串
print('我叫{0},家住{1},今年{2}岁，兴趣{3}'.format(name,address,age,interest))

# 2 %占位符
# 注意 %s 表示为字符串占位 ，%d为整数数字占位
print('我叫%s,家住%s,今年%d岁，兴趣%s' % (name,address,age,interest))

# 3 fstring
print(f'我叫{name},家住{address},今年{age}岁，兴趣{interest}')

# 规范的fstring写法
# 写开来，方便理解和可读性
s1=f'我叫{name}，今年{age}岁，家住{address},兴趣{interest}'
print(s1)

'''
'''
# 2 . 索引和切片
# 索引：按照位置提取元素
s1='我叫黄飞鹏'
# 可以采用索引位置提取元素
# 注意三个参数[start:stop:step]
# 获取飞，注意索引位置从0开始，虽然飞是第四个字，但其索引位置是3
print(s1[3])
# 飞


# 切片：从一个字符串中提取一部分内容
print(s1[3:])
# 飞鹏

# 注意，可正序可逆序
print(s1[-1])
# 鹏
print(s1[::-1])
# 鹏飞黄叫我 <--实现倒序输出
'''

'''
# 3字符串的常用操作
s='i love Pyspider'
s1=s.capitalize()
print(s1)
# I love pyspider <--将首字母大写，其余小写

s2=s.upper()
print(s2)
# I LOVE PYSPIDER <--将所有字母大写

s3=s.lower()
print(s3)
# i love pyspider <--将所有字母小写

s4=s.title()
print(s4)
# I Love Pyspider  <--将每个单词的首字母大写

# 如何忽略大小写进行判断
verify_code='XaD1'
print(verify_code)
user_input=input('请输入验证码：')
# 一般用.upper()
if user_input.upper() == verify_code.upper() :
    print('验证码正确')'''



'''
# 4字符串的切割和替换
# s1 = "     你好  ， 我是  ，内个谁    "
# print(s1)
# s1 = s1.strip()
# print(s1)
#      你好  ， 我是  ，内个谁
# 你好  ， 我是  ，内个谁

# 利用.strip()可以去掉左右的空白符

# 用法，模拟用户登录
# 防止无脑甲方输入空格之后挑刺说程序有问题
# username = input('请输入用户名').strip()
# passwd=input('请输入密码').strip()
# if username == 'admin':
#     if passwd=="123456":
#         print('登陆成功')
#     else:
#         print('登录失败')
# else:
#     print('登录失败')

#利用.replace(old=,new=,[count=])可以去掉指定的字符
# s1='我#你#他#她'
# s2=s1.replace('#','')
# print(s2)
# # 我你他她
# # 如果不指定次数，则默认全匹配
#
# s3 = s1.replace('#','',1)
# print(s3)
# # 我你#他#她
# # 如果指定count，则匹配count的数值次数
# s4=s1.replace('#','呀')
# print(s4)
# # 我呀你呀他呀她
#
# str1='he ll o ,w o r l d  '
# str2=str1.replace(' ','')
# # 去掉所有的空格
# print(str2)
# # hello,world


# 利用 .split(sep='',[maxsplit=])进行字符串的切割
# sep指定的是按照某个字符或者字符串进行切割
# maxsplit为可选参数，表示切几次
s1='he_ll_o_,_python'
print(s1.split(sep='_',maxsplit=2))
# ['he', 'll', 'o_,_python']
print(s1.split(sep='_'))
# ['he', 'll', 'o', ',', 'python']
# 利用.split()切割的结果返回的是一个列表

# 做切割的时候一定注意一件事，用什么切，即sep指定的是什么，那么切分后这个‘sep’的值就会没了
print(s1.split(sep='ll'))
# ['he_', '_o_,_python']'''



'''
# 5字符串的查找和判断

# #查找
# s1='你好，我是渣渣辉，是兄弟来看我'
# ans1=s1.find('渣辉')
# print(ans1)
# # 6 <--find会匹配指定的字符串第一次出现的位置
# ans2=s1.find('周润发')
# print(ans2)
# # -1 <--如果返回的是-1表示没有该字符串出现
# ans3=s1.find('辉渣')
# print(ans3)
# # -1
#
# ans4=s1.index('渣渣辉')
# print(ans4)
# # 5  <--只匹配字符，忽略符号
#
# try:
#     ans5=s1.index('周润发')
# except BaseException as e:
#     print(e)
#     # substring not found <--index()在没匹配到内容时会报错而.find()不会报错而是返回-1
#
# print('渣渣辉' in s1)
# # True
# print('渣渣辉' not in s1)
# # False

# 判断
# name_=input("请输入您的名字")
# # 判断是不是姓张
# if name_.startswith('张'):
#     print('四大姓之首')
# else:
#     print(f'姓名{name_}')

# 判断输入的是不是字符串类型的数字整数，如果是转换为整数类型
# money=input('请输入您的存款额度')
# print(type(money))
# if money.isdigit():  #判断字符串是否由整数组成
#     money=int(money)
#     print(type(money))
# else:
#     print('请输入整数金额!!')
# #     请输入您的存款额度10000
# # <class 'str'>
# # <class 'int'>
# s1='hello'
# if s1.endswith('o'):
#     print('以o结尾')

# 判断是否为小数其实一般不直接用.isdecimal()
# 而是使用.split('.')来分隔整数部分和小数部分再做判断
# a=123.57
# a_ls=str(a).split('.')
# print(a_ls)
# print(len(a_ls))
# if len(a_ls)==2:
#     print(str(a)+'是一个小数')'''


# .join()

# split()和join()刚好反着来
s1='hello_world_hi_python'
lst_s1=s1.split('_')
print(lst_s1)
# ['hello', 'world', 'hi', 'python']

s2='-'.join(lst_s1)
print(s2)
# hello-world-hi-python
