"""
@File    :06多进程.py
@Editor  : 百年
@Date    :2024/12/23 11:53 
"""
# IMPORTANT:导入需要的包
from multiprocessing import Process


# 准备一个函数
def func(name):
    for i in range(1000):
        print(name,i)

if __name__ == '__main__':
    p1 = Process(target=func,args=('周杰伦',)) #IMPORTANT:一定要注意，传入的是元组
    p2 = Process(target=func,args=('周润发',))
    p3 = Process(target=func,args=('周星驰',))

    p1.start()
    p2.start()
    p3.start()