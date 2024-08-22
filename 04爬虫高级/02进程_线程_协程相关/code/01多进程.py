# @Editor    : 百年
# @FileName  :01多进程.py
# @Time      :2024/7/12 18:03
'''
1导包
    import multiprocessing
2通过进程类创建进程对象
    进程对象=multiprocessing.Process()
3启动进程执行任务
    进程对象.start()
'''
# # 1导包
# import multiprocessing
# def func():
#     print('我是板顶给子进程的一组任务')
#
# if __name__ == '__main__':
#     print('主进程开始执行')
#     # 2创建一个进程p,给该进程绑定一组任务
#     p=multiprocessing.Process(target=func)
#     # 启动创建好的进程
#     p.start()
#     print('主进程执行结束')
'''
可以通过os.getpid() 获取自己进程的ID号
os.getppid() 获取自己进程的父进程的ID号
'''
# # 1导包
# import os
# import multiprocessing
# def func():
#     print(f'我是板顶给子进程的一组任务,我的进程id>>{os.getpid()}')
#     print(f'我是子进程的父进程的ID号，我的父进程ID>>{os.getppid()}')
#
# if __name__ == '__main__':
#     print(f'主进程开始执行，主进程的进程ID>>{os.getpid()}')
#     # 2创建一个进程p,给该进程绑定一组任务
#     p=multiprocessing.Process(target=func)
#     # 启动创建好的进程
#     p.start()
#     print('主进程执行结束')

'''
主进程开始执行，主进程的进程ID>>15748
主进程执行结束
我是板顶给子进程的一组任务,我的进程id>>4344
我是子进程的父进程的ID号，我的父进程ID>>15748'''



# 如何给子进程传递参数
# 1导包
import os
import multiprocessing
def func(num1,num2):
    print(f'我是绑定给子进程的一组任务,我的进程id>>{os.getpid()}')
    print(f'我是子进程的父进程的ID号，我的父进程ID>>{os.getppid()}')
    print(f'我是子进程接收到的参数：num1={num1},num2={num2}')

if __name__ == '__main__':
    print(f'主进程开始执行，主进程的进程ID>>{os.getpid()}')
    # 2创建一个进程p,给该进程绑定一组任务
    p=multiprocessing.Process(target=func,args=(123,456))
    # 启动创建好的进程
    p.start()
    print('主进程执行结束')

# 有关进程和线程的知识，在python高阶知识中做了补充，本节作为回忆即可，详细还是看python高阶中的知识