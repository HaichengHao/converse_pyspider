# @Editor    : 百年
# @FileName  :01_多线程实现多任务.py
# @Time      :2024/7/23 11:02

'''为什么使用多线程?
进程是分配资源的最小单位，一旦创建一个进程就会分配一定的资源。就像跟2个人聊qq需要打开两个qq一样是比较浪费资源的
 线程是程序执行的最小单位，是加上继承只负责分配资源，而利用这些资源执行程序的是线程，也就是说晋城市现成的容器
一个进程中最少有一个线程来负责执行程序,同时线程自己不拥有系统资源,只需要一点儿在运行中必不可少的资源,
但它与同属一个进程的其它线程共享进程所拥有的全部资源，这就像通过一个qq软件(1个进程)打开两个窗口(两个线程)根两个人聊天一样
实现多任务的同时也节省了资源'''
'''
多线程是Python中程序实现多任务的一种方式
线程是程序执行的最小单位
同属一个进程的多个线程共享进程所拥有的全部资源'''

import os
from threading import Thread
import time
def func1():
    for i in range(10):
        print('func1执行')
        time.sleep(0.1)
def func2():
    for i in range(5):
        print('func2执行')
        time.sleep(0.4)
def func3():
    for i in range(4):
        print('func3执行')
        time.sleep(0.5)

if __name__ == '__main__':
    t1=Thread(target=func1)
    t2=Thread(target=func2)
    t3=Thread(target=func3)

    # 打开线程
    t1.start()
    t2.start()
    t3.start()

    # 主线程等待所有线程执行完毕
    t1.join()
    t2.join()
    t3.join()

    print('主线程结束')
# func1执行
# func2执行
# func3执行
# func1执行
# func1执行
# func1执行
# func2执行
# func1执行
# func3执行
# func1执行
# func1执行
# func1执行
# func2执行
# func1执行
# func1执行
# func3执行
# func2执行
# func3执行
# func2执行

# 交替执行