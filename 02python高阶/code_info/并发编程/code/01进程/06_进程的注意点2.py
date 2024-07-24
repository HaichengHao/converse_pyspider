# @Editor    : 百年
# @FileName  :06_进程的注意点2.py
# @Time      :2024/7/23 9:30
# 2主进程默认不会等待所有的子进程执行结束再结束 即主进程结束之后子进程可能依然在运行
import os
'''import multiprocessing
import time

# 创建一个任务task1


def task1():
    for i in range(10):
        print('task1子进程正在执行')
        time.sleep(0.2)
# 定义程序执行的入口
if __name__ == '__main__':
    # 创建子进程对象
    process_task1=multiprocessing.Process(target=task1)
    # 启动进程
    process_task1.start()
    # 进程休眠1s
    time.sleep(1)
    print('主进程执行结束')
'''
# task1子进程正在执行
# task1子进程正在执行
# task1子进程正在执行
# 主进程执行结束 <--这时候主进程已经执行结束了，但是子进程仍在执行
# task1子进程正在执行
# task1子进程正在执行
# task1子进程正在执行
# task1子进程正在执行
# task1子进程正在执行

# 现在要解决这样一个问题:即主进程结束了但是子进程还没有结束，我们希望子进程随着主进程的结束直接结束
# 解决方案:设置守护进程,在子进程启动语句之前写 子进程名称.deamon = True

# 修改代码
'''import multiprocessing
import time

# 创建一个任务task1


def task1():
    for i in range(10):
        print('task1子进程正在执行')
        time.sleep(0.2)
# 定义程序执行的入口
if __name__ == '__main__':
    # 创建子进程对象
    process_task1=multiprocessing.Process(target=task1)
    # 设置守护进程
    process_task1.daemon = True  # 守护进程，主进程结束后子进程也结束
    # 启动进程
    process_task1.start()
    # 进程休眠1s
    time.sleep(1)
    print('主进程执行结束')'''
# task1子进程正在执行
# task1子进程正在执行
# task1子进程正在执行
# task1子进程正在执行
# task1子进程正在执行
# 主进程执行结束

# 这次可以发现，即使子进程值运行了五次没有执行完毕，但是主进程结束后子进程也直接结束，不再继续执行

# 方案2，销毁子进程
# 即让子进程在主进程结束前销毁
import multiprocessing
import time

# 创建一个任务task1


def task1():
    for i in range(10):
        print('task1子进程正在执行')
        time.sleep(0.2)
# 定义程序执行的入口
if __name__ == '__main__':
    # 创建子进程对象
    process_task1=multiprocessing.Process(target=task1)

    # 启动进程
    process_task1.start()
    # 进程休眠1s
    time.sleep(1)

    # 销毁子进程
    process_task1.terminate()  # 销��子进程

    print('主进程执行结束')

# task1子进程正在执行
# task1子进程正在执行
# task1子进程正在执行
# task1子进程正在执行
# task1子进程正在执行
# 主进程执行结束 <--方案2也是可行的