# @Editor    : 百年
# @FileName  :05_os.kill()杀掉进程.py
# @Time      :2024/7/23 8:41

# os.kill(要杀掉进程的pid,信号singal)
# pid:要杀掉的进程id
# singal:和操作系统有关，9代表强制杀掉进程,15代表正常杀死进程
import multiprocessing
import signal
from multiprocessing import Process
import os


def process1(name):
    print(f'{name}正在执行')


if __name__ == '__main__':
    pid = os.getpid()
    print(f'主进程开始执行，进程编号为{pid}')
    subprocess = multiprocessing.Process(target=process1, args=('小趴菜进程',))
    subprocess.start()
    os.kill(pid,15)

    # 注意这一行代码我们写在了杀死进程之后，如果代码无误，那么这一行输出语句铁定不会被执行
    print('主进程结束,已经被kill')

#    主进程开始执行，进程编号为20872
#
# Process finished with exit code 15

# 和预测的一样，杀死进程后再杀死进程执行后的语句将不会被执行