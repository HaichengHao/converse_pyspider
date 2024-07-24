# @Editor    : 百年
# @FileName  :01_python中单任务的实现.py
# @Time      :2024/7/13 6:51
import time
import os


def func_a():
    print('I am task A')
    time.sleep(2)


def func_b():
    print('I am task B')
    time.sleep(1)


if __name__ == '__main__':
    starttime = time.time()
    func_a()
    func_b()
    endtime = time.time()
    totaltime = endtime - starttime
    print(f'Total time: {totaltime} seconds')
