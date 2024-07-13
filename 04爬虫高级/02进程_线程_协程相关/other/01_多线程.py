# @Editor    : 百年
# @FileName  :01_多线程.py
# @Time      :2024/7/11 22:31
"""def func(name):
    for i in range(10):
        print(name,i)

if __name__ == '__main__':
    func('周杰伦')
    func('王力宏')
"""
"""
周杰伦 0
周杰伦 1
周杰伦 2
周杰伦 3
周杰伦 4
周杰伦 5
周杰伦 6
周杰伦 7
周杰伦 8
周杰伦 9
王力宏 0
王力宏 1
王力宏 2
王力宏 3
王力宏 4
王力宏 5
王力宏 6
王力宏 7
王力宏 8
王力宏 9
可以看到单线程一个一个的运行，如果周杰伦没有运行完那么王力宏也不会执行，单线程的执行效率极其低下
"""

# 如果想要开启多线程，那么要先引入一个包
from threading import Thread

# 创建一个任务
def task1(name):
    for i in range(10):
        print(name, i)
if __name__ == '__main__':
    # 创建线程
    # 线程名 = Thread(target=目标函数,args=(参数(强制要求为元组，记得加逗号)))
    t1 = Thread(target=task1, args=("周杰伦",))
    t2 = Thread(target=task1, args=("王力宏",))
    t3 = Thread(target=task1, args=("张学友",))
    # 线程执行
    t1.start()
    t2.start()
    t3.start()
