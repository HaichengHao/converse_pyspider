# @Editor    : 百年
# @FileName  :01协程引例1.py
# @Time      :2024/8/31 10:15
# todo:记得先运行异步案例1中的Server.py
import time
import asyncio

urls = [
    'www.1.com',
    'www.2.com',
    'www.3.com'
]

start = time.time()
# 0 创建特殊函数
async def get_request(url):
    print('正在请求', url)
    # todo:可以开启和关闭time.sleep(2)的注释查看运行的结果
    # time.sleep(2) <--time是不支持异步模块的，如果注释掉再次运行，便可以发现速度过快
    #当然asyncio也有它自己的模块可以解决这个问题
    # asyncio.sleep(2) #再次运行查看结果
    # 最终解决方案
    await asyncio.sleep(2)
    print('请求成功', url)
    return 123
def t_callback(t):
    print('我是回调函数')
tasks=[]
for url in urls:
    # 1创建协程对象
    c = get_request(url)
    # 2创建任务对象
    task = asyncio.ensure_future(c)
    # 2.1创建任务对象回调函数
    task.add_done_callback(t_callback)
    #2.2将任务对象添加到任务列表之中
    tasks.append(task)
# 3创建事件循环对象，注意，事件循环对象写外边，目前我们有3个任务对象和1个事件循环对象
loop = asyncio.get_event_loop()
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# 将包含三个任务的任务列表添加到事件循环对象当中
loop.run_until_complete(asyncio.wait((tasks)))
'''
async def wait(fs, *, timeout=None, return_when=ALL_COMPLETED):
    """Wait for the Futures and coroutines given by fs to complete.

    The fs iterable must not be empty.

    Coroutines will be wrapped in Tasks.

    Returns two sets of Future: (done, pending).

    Usage:

        done, pending = await asyncio.wait(fs)

    Note: This does not raise TimeoutError! Futures that aren't done
    when the timeout occurs are returned in the second set.
    """'''
print(f'耗时:{time.time()-start}')
# 耗时:6.04284143447876 <--同步执行的，没有实现异步，为什么？回看03_协程，
# 因为我们在特殊函数内部用了不支持异步模块的代码time.sleep()

''' 注释掉time.sleep()后的运行结果，运行速度太快了，是有问题的
D:\python\python.exe D:/converse_fullstack/converse/04爬虫高级/02进程_线程_协程相关/case/协程案例/01协程引例1.py
D:\converse_fullstack\converse\04爬虫高级\02进程_线程_协程相关\case\协程案例\01协程引例1.py:30: DeprecationWarning: There is no current event loop
  task = asyncio.ensure_future(c)
D:\converse_fullstack\converse\04爬虫高级\02进程_线程_协程相关\case\协程案例\01协程引例1.py:36: DeprecationWarning: There is no current event loop
  loop = asyncio.get_event_loop()
正在请求 www.1.com
请求成功 www.1.com
正在请求 www.2.com
请求成功 www.2.com
正在请求 www.3.com
请求成功 www.3.com
我是回调函数
我是回调函数
我是回调函数
耗时:0.002002716064453125

'''
''' 加上asyncio.sleep(2)后的运行结果
D:\python\python.exe D:/converse_fullstack/converse/04爬虫高级/02进程_线程_协程相关/case/协程案例/01协程引例1.py
D:\converse_fullstack\converse\04爬虫高级\02进程_线程_协程相关\case\协程案例\01协程引例1.py:33: DeprecationWarning: There is no current event loop
  task = asyncio.ensure_future(c)
D:\converse_fullstack\converse\04爬虫高级\02进程_线程_协程相关\case\协程案例\01协程引例1.py:39: DeprecationWarning: There is no current event loop
  loop = asyncio.get_event_loop()
正在请求 www.1.com
请求成功 www.1.com
正在请求 www.2.com
请求成功 www.2.com
正在请求 www.3.com
请求成功 www.3.com
我是回调函数
我是回调函数
我是回调函数
耗时:0.12803959846496582 还是不对，速度还是太快了，阻塞操作没有执行
D:\converse_fullstack\converse\04爬虫高级\02进程_线程_协程相关\case\协程案例\01协程引例1.py:23: RuntimeWarning: coroutine 'sleep' was never awaited
  asyncio.sleep(2) #再次运行查看结果
RuntimeWarning: Enable tracemalloc to get the object allocation traceback

Process finished with exit code 0
'''
'''
D:\python\python.exe D:/converse_fullstack/converse/04爬虫高级/02进程_线程_协程相关/case/协程案例/01协程引例1.py
D:\converse_fullstack\converse\04爬虫高级\02进程_线程_协程相关\case\协程案例\01协程引例1.py:35: DeprecationWarning: There is no current event loop
  task = asyncio.ensure_future(c)
D:\converse_fullstack\converse\04爬虫高级\02进程_线程_协程相关\case\协程案例\01协程引例1.py:41: DeprecationWarning: There is no current event loop
  loop = asyncio.get_event_loop()
正在请求 www.1.com
正在请求 www.2.com
正在请求 www.3.com
请求成功 www.1.com
请求成功 www.2.com
请求成功 www.3.com
我是回调函数
我是回调函数
我是回调函数
耗时:2.003131151199341 <--可以看运行成功了，每个都是2s

Process finished with exit code 0
'''
