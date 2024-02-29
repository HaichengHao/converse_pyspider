# editor: 百年
# time: 2024/2/29 10:31
a='hello world'
# 这个语句中a为变量名/变量 等号后的是变量的值
for i in range(4):
    print(a)

a = 'helo'
print(a)

# 变量可以由字母数字下划线组成
_b1=12
print(_b1)
c_1=13
print(c_1)
d1_=14
print(d1_)

# 但不可由数字开头
# try:
#     1_e=15
# except BaseException as e:
#     print(e)
    # SyntaxError: invalid decimal literal <--报错

# 不能用中文