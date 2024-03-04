# editor: 百年
# time: 2024/3/4 10:37

# 1.算数运算符
#     + - * / % //

'''
a=10
b=-2
c=4
d=-3
print(a/b)
print(a%d)
# -2  <--余数等于被除数减去除数*商
print(a//c)
# 2 <--整除，只保留商，不管余数
'''

# 2.比较运算符
#     > < >= <=  != ==
# 两个等号作的是判断，一个等号是赋值
'''
a=10
b=20
c=10
d=90
print(a==c)
print(a>b)
# True
# False
'''

# 3.赋值运算符
#     = += -= *= /= %= //=
'''
a=10
b=20
print(f'a={a},b={b}')

# 两值互换操作,注意，此渐变操作只适用于python
a,b=b,a
print(f'a={a},b={b}')
# a=10,b=20
# a=20,b=10

# 其底层逻辑
c=20
d=100
print(f'c={c},d={d}')
# c=20,d=100
temp=c
c=d
d=temp
print(f'c={c},d={d}')
# c=100,d=20

# 计算100以内的整数和
a=1
sum = 0
while a <=100:
    sum+=a
    a+=1
print(sum)
'''

# 4.逻辑运算符
#     可以有效的减少判断层级
#     1 and 与
#     2 or  或
#     3 not 非


# 与  全真则真，一假则假
print(True and  False)
# False
print(True and True)
# True

# 或 一真则真
print(True or False)
# True
print(True or False or False)
# True


# 非 非真则假，非假则真

a = not True
print(a)
# False


# 常用场景
user_name=input('请输入用户名:').strip()
passwd=input('请输入密码')
if user_name == 'admin' and passwd == '123456':
    print('登录成功')
else:
    print('登录失败')


# 5成员运算符
lst=[1,2,4,5,7]
print(1 in lst)
print(10 in lst)
print(8 not in lst)
print(100 not in lst)
# True
# False
# True
# True