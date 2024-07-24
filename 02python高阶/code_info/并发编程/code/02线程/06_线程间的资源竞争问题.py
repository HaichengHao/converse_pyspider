# @Editor    : 百年
# @FileName  :06_线程间的资源竞争问题.py
# @Time      :2024/7/24 9:32
from threading import Thread
global_number = 0

def sum_num1():
    for i in range(1000000):
        # 调用global函数实现在函数内部修改全局变量
        global global_number
        global_number += 1
    print(f'global_number:{global_number}')
def sum_num2():
    for i in range(1000000):
        global global_number
        global_number += 1
    print(f'global_numbe2:{global_number}')


if __name__ == '__main__':
    t1 = Thread(target=sum_num1)
    t2 = Thread(target=sum_num2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Main Thread End.')
# global_number:1642235
# global_numbe2:2000000
# Main Thread End.
# 很明显是不对的
# 解决办法:同步，就是协同不掉，按预定的先后次序进行运行，好比现实生活中的对讲机
# 使用线程同步:保证同一时刻只能有一个线程去操作全局变量