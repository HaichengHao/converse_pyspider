

# @Editor    : 百年
# @FileName  :03_协程.py
# @Time      :2024/7/29 7:45

# 多进程、多线程、线程池都不能解决IO阻塞问题
'''
解决这一问题的关键在于
我们自己从自己的应用程序级别检测到IO阻塞，然后使得cpu切换到我们自己程序的其他部分
/任务执行，这样可以将IO阻塞降到最低，我们的程序处于就绪状态的就越多
'''
'''
协程如何实现呢？
在python3.5之后，新增了asyncio模块，即异步io模块，可以帮我们检测IO(只能是网络IO【http连接就是网络IO操作
】),实现应用程序级别的切换(异步IO)'''
'''
接下来是协程的实现，从python3.4开始,python中加入了协程的概念，但是这个版本中的写成还是以生成器对象为基础的
，在python3.5中增加了asynico,使得协程的实现更加方便，需要了解以下概念
特殊函数:
    -在普通函数定义语句前加上async，则该函数就变成了特殊函数
    -特殊函数的特殊之处:
        -1:特殊函数被调用后，函数内部的程序语句(函数体)没有被立即执行
        -2:特殊函数被调用后会返回一个协程对象
        
# <coroutine object get_request at 0x000002E51C346730> <--其中的coroutine意思就是协程
# sys:1: RuntimeWarning: coroutine 'get_request' was never awaited
        
协程:
    -协程对象，特殊函数调用就可以返回/创建一个协程对象
    -协程对象 == 特殊的函数 == 一组指定形式的操作
        - 因此，协程对象 == 一组指定形式的操作
任务:
    -任务对象就是一个高级的协程对象。它的高级之处重点在于可以给任务对象绑定一个回调函数
        -回调函数有什么作用?
            -回调函数就是回头调用的函数，因此要这样理解,当任务对象被执行结束后，
            会立即给任务对象绑定的这个回调函数
            -如何绑定回调函数?
                -code 
    -任务对象==高级的协程对象==一组指定形式的操作
    -任务对象 == 一组制定形式的操作
事件循环:
    -事件循环对象(Event Loop)，可以将其当做是一个容器，该容器是用来装载任务对象的。它可装载一个或多个对象
    所以说创建好了一个或多个任务对象后，下一步就需要将任务对象全部装载在事件循环对象当中。
    -为什么需要把任务对象装载在事件循环对象当中?
        -答:当将任务对象装载在事件循环当中后，启动事件循环对象，则其内部装载的任务对象对应的相关操作就会被立即执行
        
asyncio.wait()函数: 任务列表不能够直接放在事件循环对象当中
    -给列表中的每一个任务对象赋予一个可被挂起的权限!当CPU执行的任务对象遇到阻塞的时候，当前任务对象就会被挂起，则cpu就可以执行其它任务对象，提高整体程序运行的效率
    -挂起任务对象:让当前正在被执行的任务对象交出cpu的使用权，cpu就可以被其他任务对象抢占和使用，从而可以执行其它任务。
    -注意:特殊函数内部，不可以出现不支持异步模块的代码，否则会中断整个异步效果
await关键字:挂起发生阻塞操作的任务对象
    -例如协程引例中 await asyncio.sleep(2)
    -注意，在任务对象表示的操作中凡是阻塞操作的前面都必须加上await关键字进行修饰!!
'''
'''
使用uvloop加速(了解)
uvloop基于libuv,libuv是一个使用c语言实现的高性能异步IO库，uvloop用来替代asyncio默认事件循环，
可以进一步加快异步IO操作的速度
uvloop的使用非常简单,只要在run_until_complete前，调用方法如下，
将asyncio的事件循环策略设置为uvloop的事件循环策略
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

代码实现:
loop =  asyncio.get_event_loop()
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop.run_until_complete(asyncio.wait(tasks))
'''

import time
import asyncio
# 特殊的函数:
async def get_request(url):
    print(f'正在请求的网址是:{url}')
    time.sleep(2)
    print('请求网址结束')
    return 123
# 回调函数的封装
def t_callback(t):
    # 这里如果不加上形式参数运行就会报这样的错误
    '''
    File "D:\python\lib\asyncio\events.py", line 80, in _run
    self._context.run(self._callback, *self._args)
    TypeError: t_callback() takes 0 positional arguments but 1 was given
    即回调函数必须有1个位置参数'''

    data = t.result() #result()可以获取特殊函数的返回值
    print(f'我是任务对象的回调函数!获取到特殊函数的返回值为:{data}')


# 创建了一个协程对象
c = get_request('www.1.com')
# print(c)
'''
<coroutine object get_request at 0x000002E51C346730>
sys:1: RuntimeWarning: coroutine 'get_request' was never awaited'''
# 创建任务对象
task = asyncio.ensure_future(c)

# 新：给任务对象绑定回调函数 add_done_clallback的参数就是要回调的函数的名字
task.add_done_callback(t_callback) #直接当英文理解，即task这个任务对象添加一个它(task)执行完毕后的回调函数
# 查看运行结果
#创建事件循环对象
loop = asyncio.get_event_loop() #注意，新版本的python已经淘汰该语法

# FIXME:下面的新语法是需要掌握的
'''
新语法
loop=asyncio.new_event_loop() #创建新的事件循环对象
asyncio.set_event_loop(loop) #设置新的时间循环对象
'''
# 将任务对象装载在事件循环对象中且启动事件循环对象
loop.run_until_complete(task) #这步的操作就是把事件对象装载在事件循环对象loop当中并启动了事件循环对象

'''
正在请求的网址是:www.1.com
D:\converse_fullstack\converse\04爬虫高级\02进程_线程_协程相关\code\03_协程.py:79: DeprecationWarning: There is no current event loop
  task = asyncio.ensure_future(c)
D:\converse_fullstack\converse\04爬虫高级\02进程_线程_协程相关\code\03_协程.py:84: DeprecationWarning: There is no current event loop
  loop = asyncio.get_event_loop()
请求网址结束
我是任务对象的回调函数! <--可以看到任务对象执行完毕之后这个回调函数t_callback才被调用执行
所以add_done_callback()括号内指定的回调函数确实是任务对象执行完毕之后才执行'''