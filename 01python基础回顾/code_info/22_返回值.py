# editor: 百年
# time: 2024/3/6 15:20
#
# def fun(a,b):
#     # print(a+b)
#     return a+b
# result = fun(10,99)
# print(result)
# 109
'''
def fun(a,b):
    a+=b
# 如果没有返回值
res=fun(10,99)
print(res)
# None
# 没有返回值则默认为None'''

'''# 函数执行到了return，则其后面的代码不会执行
def fun(a,b):
    return  #<--只有一个return有点像break
    print(a+b)
result = fun(10,99)
print(result)
# None'''

# 如果有多个返回值,返回的结果是一个元组
def fun(a,b):
    return a+b,a*b
res=fun(2,5)
print(res)
# (7, 10)