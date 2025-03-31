"""
@File    :02对照之参数传递.py
@Editor  : 百年
@Date    :2025/3/30 15:47 
"""


def func1(a, b):
    result = a + b
    return result


if __name__ == '__main__':
    a = 1
    b = 2
    reslut = func1(a,b)
    print(reslut)
