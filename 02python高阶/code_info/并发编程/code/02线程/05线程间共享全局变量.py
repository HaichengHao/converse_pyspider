# @Editor    : 百年
# @FileName  :05线程间共享全局变量.py
# @Time      :2024/7/24 9:09
# 线程间共享全局变量
# 多个线程都是在同一进程中，多个线程使用的资源都是同一进程中的资源，因此多线程间是共享全局变量的

from threading import Thread
# 创建一个全局变量
mylst=[]
# 定义任务1
def task1():
    for i in range(10):
        mylst.append(i)
    print(mylst)
# 定义任务2
def task2():
    print(mylst)

# 定义主程序
if __name__ == '__main__':
    # 定义线程对象
    t1=Thread(target=task1)
    t2=Thread(target=task2)
    # 开启多线程
    t1.start()
    t2.start()
    # 主线程等待子线程执行结束
    t1.join()
    t2.join()
    print('运行结束')
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 运行结束
# 可以发现，与多进程对比，多进程是不共享全局变量的，而多线程则共享全局变量