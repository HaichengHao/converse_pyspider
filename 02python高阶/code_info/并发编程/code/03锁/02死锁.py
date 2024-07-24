# @Editor    : 百年
# @FileName  :02死锁.py
# @Time      :2024/7/24 11:03
# 一直等待对方释放锁的方式就是死锁
# 死锁的结果:会造成应用程序停止响应，不能处理其它任务了
import threading
from threading import Thread
global_number = 0

def sum_num1():
    print('sum_num1....')
    # 上锁
    mutex.acquire()
    for i in range(1000000):
        # 调用global函数实现在函数内部修改全局变量
        global global_number
        global_number += 1
    # 这里为了还原死锁状况我们不让解锁
    print(f'global_number:{global_number}')
def sum_num2():
    print('sum_num2....')
    # 上锁
    mutex.acquire()
    for i in range(1000000):
        global global_number
        global_number += 1
    # 不解锁
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
# sum_num1....
# sum_num2....
# global_number:1000000
# 产生死锁，无法继续执行代码，这要求我们在写线程执行多任务时一定要养成好习惯，及时解锁