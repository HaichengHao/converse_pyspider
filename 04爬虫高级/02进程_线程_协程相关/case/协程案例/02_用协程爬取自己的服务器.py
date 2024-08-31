# @Editor    : 百年
# @FileName  :02_用协程爬取自己的服务器.py
# @Time      :2024/8/31 19:42
import asyncio
# import requests
# import uvloop tips:如果你用的是windows,那么不用纠结，这个你用不了，你可以换linux或macos
import aiohttp
import time
from lxml import etree

start_t = time.time()
# 由于自己写的网页中也就pycharm快捷键这个适合开启异步爬取，所以就令一个网页作为三次请求的url,并将其作为url列表
urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/bobo'
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}


# 1设置一个特殊函数用来对指定的url发起请求,获得响应数据
async def get_request(url):
    # 注意，requests模块是不支持异步的，这事情就大了，我们必须替换它
    # aiohttp:是一个基于网络请求的模块，和requests相似，但是requests不支持异步，可是aiohttp是支持的
    # response= await requests.get(url,headers=headers) #在特殊函数之中,request是阻塞操作
    # response.encoding = response.apparent_encoding
    # content = response.text
    # return content

    #     下面使用aiohttp
    #     1创建请求对象
    async with aiohttp.ClientSession() as sess:
        #         2基于请求对象发起请求
        # 如果是get请求，那么常用参数就是和普通的requests请求的参数差不多url,headers,proxy,parama
        # 如果是post请求，那么常用参数就是和post请求的参数差不多url,headers,data,proxy
        # 其实主要就是proxies换成了proxy,而且aiohttp的请求的proxy不是requests的字典形式的代理{'http': '182.204.178.124:8089'}，而是字符串形式的代理'http://182.204.178.124:8089'
        async with await sess.get(url=url, headers=headers) as response:
            content = await response.text()  # 注意这里也有不同，这里用的是text()方法，而在requests中我们用的是.text属性
            # 并且返回值也不一样，.text()方法返回的是字符串，而requests中的.text返回的是html对象
            # 它也有另外一个方法.read(),返回的是二进制的响应数据

            return content
'''
补充:
在每一个with前面都加上关键字
在阻塞操作前加上await关键字
'''

# 设置回调函数，爬虫中回调函数一般写为解析数据用的函数
def parse_content(t):
    page_text = t.result()  # 利用.result()获取特殊函数的返回值
    tree = etree.HTML(page_text)
    # 设置要获取的数据的xpath
    result = tree.xpath("//tr[1]/td[1]")
    print(result)


tasks = []
for url in urls:
    # 设置协程对象
    c = get_request(url)
    # 设置任务对象
    task = asyncio.ensure_future(c)
    tasks.append(task)
    # 任务对象的回调函数在爬虫之中一般是用来做数据解析的
    task.add_done_callback(parse_content)
# 设置事件循环对象
loop = asyncio.get_event_loop()
# 如果想使用uvloop加速只需要加上下面这行代码,当然，需要导入uvloop的包
# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop.run_until_complete(asyncio.wait((tasks)))
print(f'总耗时{time.time() - start_t}')
'''
D:\python\python.exe D:/converse_fullstack/converse/04爬虫高级/02进程_线程_协程相关/case/协程案例/02_用协程爬取自己的服务器.py
D:\converse_fullstack\converse\04爬虫高级\02进程_线程_协程相关\case\协程案例\02_用协程爬取自己的服务器.py:64: DeprecationWarning: There is no current event loop
  task = asyncio.ensure_future(c)
D:\converse_fullstack\converse\04爬虫高级\02进程_线程_协程相关\case\协程案例\02_用协程爬取自己的服务器.py:69: DeprecationWarning: There is no current event loop
  loop = asyncio.get_event_loop()
[<Element td at 0x1c457f78740>]
[<Element td at 0x1c457790180>]
[<Element td at 0x1c457f78580>]
总耗时2.1194396018981934'''