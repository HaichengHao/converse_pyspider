# @Editor    : 百年
# @FileName  :04获取进程编号.py
# @Time      :2024/7/13 11:22
'''
获取进程编号需要导入os模块
获取进程编号>> os.getpid()                   processid
获取当前进程的父进程的进程编号 >> os.getppid()    parentprocessid

进程编号的作用:
当程序中进程的数量越来越多时，如果没有办法区分主进程和子进程还有不同的子进程，
那么就无法进行有效的进程管理，为了方便管理实际上每个进程都是有自己的编号的
'''

# 方式1
import multiprocessing

'''import os
print(f'父进程的ID: {os.getppid()}')
print(f'子进程的id: {os.getpid()}')'''
# 父进程的ID: 8172
# 子进程的id: 13016
# 删除整行的快捷键shift+delete

# 方式2
from  multiprocessing import Process
import os
def work():
    print('执行work任务')
    print(f'当前进程编号:{multiprocessing.current_process().pid}')
#     获取父进程编号
    print(f'父进程编号:{os.getppid()}')
if __name__ == '__main__':
    print(f'主进程开始,id为:{os.getpid()}')
    sub_process=multiprocessing.Process(target=work)
    sub_process.start()

# 主进程开始,id为:16332
# 执行work任务
# 当前进程编号:21712
# 父进程编号:16332 <--可见work是main的子进程，work的父进程是main
