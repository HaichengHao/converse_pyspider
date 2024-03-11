# editor: 百年
# time: 2024/3/11 17:52
'''
递归，自己调用自己，俗称套娃
递归如过没有东西拦截的话那它默认就是一个死循环
python默认是有递归深度的限制的，默认的最大递归深度是1000
'''
# 查看递归最大深度
import sys
print(sys.getrecursionlimit())
# 1000
# 可以通过sys.setrecursionlimit(指定的数值)来将Python的默认递归最大深度调整成指定的数值，但是不建议这么干

# # 阶乘计算
# def func1(num):
#     if num > 1:
#         num=num*func1(num-1)
#     return num
# number=int(input('输入一个数字，我来帮你算阶乘:'))
# print(func1(number))
# # 输入一个数字，我来帮你算阶乘:5
# # 120

# 斐波那契数列,从第三位开始，每个数等于前两个数的和
# [1,1,2,3,5,7,12,19.....]
# 定义斐波那契函数fiber(n)其中n为参数，表示输出第几位斐波那契数字
def fiber(n):
    if n == 1 :
        return 1
    elif n == 2 :
        return 1
    else:
        return fiber(n-1)+fiber(n-2)
num=int(input('请输入您想知道的从第1为到第几位的斐波那契数列:'))
fib_lst=[]
for i in range(1,num+1):
    fib_lst.append(fiber(i))
print(fib_lst)
# 请输入您想知道的从第1为到第几位的斐波那契数列:3
# [1, 1, 2]
# 请输入您想知道的从第1为到第几位的斐波那契数列:5
# [1, 1, 2, 3, 5]
