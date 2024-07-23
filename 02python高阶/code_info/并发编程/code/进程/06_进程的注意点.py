# @Editor    : 百年
# @FileName  :06_进程的注意点.py
# @Time      :2024/7/23 8:57
# 1进程之间不共享全局变量
# 实际上创建一个子进程就是把主进程的资源进行拷贝产生了一个新的进程，这里的主进程和子进程是相互独立的
import multiprocessing
import time
from multiprocessing import Process
import os
mylst=[]
def writedata():
    for i in range(3):
        mylst.append(i)
    print(f'writedata:{mylst}')
def readdata():
    print(f'readdata:{mylst}')

if __name__ == '__main__':
    writeprocess=multiprocessing.Process(target=writedata)
    readprocess=multiprocessing.Process(target=readdata)
    writeprocess.start()
    time.sleep(1)
    readprocess.start()
# writedata:[0, 1, 2]
# readdata:[]
# 可见两个子进程之间并没有共享全局变量


# 2主进程默认不会等待所有的子进程执行结束再结束 即主进程结束之后子进程可能依然在运行
