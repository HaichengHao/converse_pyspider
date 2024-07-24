# @Editor    : 百年
# @FileName  :03_python中主线程与子线程的结束顺序.py
# @Time      :2024/7/23 11:42
'''from threading import Thread
import time

def task1():
    for i in range(10):
        print(f'Task1: {i}')
        time.sleep(0.2)
if __name__ == '__main__':

    t1=Thread(target=task1)
    t1.start()
    print('主线程执行结束')
'''
# Task1: 0
# 主线程执行结束 <--可以看到主线程先于子线程执行结束
# Task1: 1
# Task1: 2
# Task1: 3
# Task1: 4
# Task1: 5
# Task1: 6
# Task1: 7
# Task1: 8
# Task1: 9
#
# Process finished with exit code 0

# 现在需要的解决方案:让主线程晚于子线程结束

# 方案1 创建子线程时就指定好参数daemon=True,开启线程守护
'''import threading
from threading import Thread
import time

def task1():
    for i in range(10):
        print(f'Task1: {i}')
        time.sleep(0.2)
if __name__ == '__main__':

    # 创建子线程对象时就指定好参数设置保护线程
    t1=threading.Thread(target=task1,daemon=True)
    t1.start()
    print('主线程执行结束')'''
# Task1: 0
# 主线程执行结束

# 方案2
import threading
from threading import Thread
import time

def task1():
    for i in range(10):
        print(f'Task1: {i}')
        time.sleep(0.2)
if __name__ == '__main__':

    # 创建子线程对象时就指定好参数设置保护线程
    t1=threading.Thread(target=task1)
    t1.setDaemon(True)  # 等同于 daemon=True的创建方法,此方法已经弃用，过时了
    t1.start()
    print('主线程执行结束')


# 方案3:需要用到.join()方式阻塞主线程执行
'''from threading import Thread
import time

def task1():
    for i in range(10):
        print(f'Task1: {i}')
        time.sleep(0.2)
if __name__ == '__main__':

    t1=Thread(target=task1)
    t1.start()
    t1.join()  # 主线程在t1执行结束后才执行
    print('主线程执行结束')'''
# Task1: 0
# Task1: 1
# Task1: 2
# Task1: 3
# Task1: 4
# Task1: 5
# Task1: 6
# Task1: 7
# Task1: 8
# Task1: 9
# 主线程执行结束
# 可以看到这时候主线程等待子线程执行完毕后才结束

