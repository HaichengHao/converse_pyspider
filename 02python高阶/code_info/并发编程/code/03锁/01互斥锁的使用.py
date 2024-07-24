# @Editor    : 百年
# @FileName  :01互斥锁的使用.py
# @Time      :2024/7/24 10:35
# 互斥锁:对共享数据进行锁定，保证同一时刻只有一个线程去操作
# 互斥锁的介绍
# 对共享数据进行锁定，保证同一时刻只有一个线程去操作
# 注意
# 互斥锁是多个线程一起去抢，抢到锁的线程先运行，没有抢到锁的线程进行等待，等锁使用完释放后，其它等待的线程再去抢这个锁
# 互斥锁的创建
# mutex=threading.lock()
# 上锁
# mutex.acquire()
# 释放锁
# mutex.release()
import threading
from threading import Thread
global_number = 0

def sum_num1():
    # 上锁
    mutex.acquire()
    for i in range(1000000):
        # 调用global函数实现在函数内部修改全局变量
        global global_number
        global_number += 1
    # 解锁
    mutex.release()
    print(f'global_number:{global_number}')
def sum_num2():
    # 上锁
    mutex.acquire()
    for i in range(1000000):
        global global_number
        global_number += 1
    # 解锁
    mutex.release()
    print(f'global_numbe2:{global_number}')


if __name__ == '__main__':
    # 创建锁
    mutex=threading.Lock()
    t1 = Thread(target=sum_num1)
    t2 = Thread(target=sum_num2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Main Thread End.')
# global_number:1000000
# global_numbe2:2000000
# Main Thread End.
# 这次运行就对了