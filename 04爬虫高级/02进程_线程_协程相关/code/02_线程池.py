# @Editor    : 百年
# @FileName  :02_线程池.py
# @Time      :2024/7/28 15:35
'''
线程池创建与使用分步走
1 导包 from concurrent.futures import ThreadPoolExecutor

2 调用，在主程序中创建线程池
with ThreadPoolExecutor(指定线程池线程数) as executor:
#     3 提交任务到线程池
        executor.submit(任务函数, 任务参数)
#  如果想要使用回调函数，那么就在其后添加.add_done_callback(回调函数名，参数)
'''
# todo:学习本节建议看异步案例中的main2.py
# 导入线程池执行器
from concurrent.futures import ThreadPoolExecutor
import time


# 引例
# def func(name):
#     for i in range(10):
#         print(name,i)
#
# if __name__ == '__main__':
#     # 开10个线程
#     with ThreadPoolExecutor(10) as t:
#         t.submit(func,'周星驰')
#         t.submit(func,'林克')
#         t.submit(func,'刘德华')

# 接收返回值
def func(name, timeofsleep):
    time.sleep(timeofsleep)
    print(f'我是{name}')

    return name


# 定义接收返回值的函数
def getcbk(res):
    # .result 可以拿到前一个函数的执行结果，即前一个函数的返回值
    print(res.result())


if __name__ == '__main__':
    # with ThreadPoolExecutor(3) as executor:
    # .add_done_callback(目标函数名) 定义的是前一个任务完成之后现在所要执行的内容
    ''' executor.submit(func,name='周星驰',timeofsleep=2).add_done_callback(getcbk)
     executor.submit(func,'周润发',1).add_done_callback(getcbk)
     executor.submit(func,'周结论',3).add_done_callback(getcbk)'''
    # 我是周润发
    # 周润发
    # 我是周星驰
    # 周星驰
    # 我是周结论
    # 周结论



    # 使用创建任务队列的方式让任务按序执行，需要使用到map,
    # map 方法会自动将任务分配给线程池中的线程进行并发执行，并返回结果的迭代器。

    # 创建任务队列
    tasklst = ['周星驰', '周润发', '周结论']
    with ThreadPoolExecutor(3) as executor:
    # def map(self, fn任务函数, *iterables可迭代对象, timeout=None时延, chunksize=1片大小):  <--base.py中的用法提示
    # 注意，利用map想像submit那样使用回调函数返回结果直接利用变量接收即可，但要注意，它返回的是一个生成器
        result =  executor.map(func, tasklst, [1, 2, 3])
        print(type(result)) #<class 'generator'>
    # 如果想查看结果只需要我们利用生成器的知识来看就行
        print(list(result))

    # 最终运行结果
    # <class 'generator'>
    # 我是周星驰
    # 我是周润发
    # 我是周结论
    # ['周星驰', '周润发', '周结论']
    # 我们可以看出，线程是按照我们指定的顺序来执行的而不是像submit那样混乱