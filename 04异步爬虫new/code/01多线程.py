"""
@File    :01多线程.py
@Editor  : 百年
@Date    :2024/12/21 16:50 
"""

# 单线程案例
# def func(name):
#     for i in range(10):
#         print(name,i)
# if __name__ == '__main__':
#     func('bob')
#     func('jack')
#     func('amiy')
#     # 上个函数执行后下面的函数才会运行，执行效率很低

from threading import Thread


# 创建任务
def func(name):
    for i in range(100):
        print(name, i)


if __name__ == '__main__':
    # 创建线程,指定任务参数target即这个线程的目的是什么并传入相应的参数
    thread1 = Thread(target=func,args=("bob",)) #IMPORTANT:注意这里有强制要求，传入的参数必须是元组或者列表形式
#      *args* is a list or tuple of arguments for the target invocation. Defaults to (). <--这是threading.py的参考文件
    thread2 = Thread(target=func, args=("jerry",))
    thread3 = Thread(target=func, args=("amy",))

#     线程创建好了接下来就是启动线程
    thread1.start()
    thread2.start()
    thread3.start()
#     IMPORTANT: 注意，此时这个python程序里总共有四个线程而不是简单的看成线程只有thread1,2,3，因为主线程是主函数

# 可以运行一下看看，结果是相当混乱的

