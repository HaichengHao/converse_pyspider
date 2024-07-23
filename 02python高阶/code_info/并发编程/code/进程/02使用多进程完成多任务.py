# @Editor    : 百年
# @FileName  :02使用多进程完成多任务.py
# @Time      :2024/7/13 7:13
import time
import multiprocessing

def music():
    for i in range(3):
        print('听音乐')
        time.sleep(0.2)

def coding():
    for i in range(3):
        print('写代码')
        time.sleep(0.2)

# 定义程序的执行入口
if __name__ == '__main__':
    #创建进程对象
    # 进程对象  = multiprocessing.Process(target=任务名)
    # target 执行的目标任务名，这里指的是函数名
    # name 进程名，一般不用设置
    # group 进程组，目前只能用none
    start_time=time.time()
    p1 = multiprocessing.Process(target=music)
    p2 = multiprocessing.Process(target=coding)

    # 启动进程
    p1.start()
    p2.start()
    print(f'程序执行所用时间：{time.time() - start_time}s')
'''
0.022225618362426758s <--执行时间明显比一条虫下来快很多
听音乐
写代码
写代码
听音乐
听音乐
写代码'''