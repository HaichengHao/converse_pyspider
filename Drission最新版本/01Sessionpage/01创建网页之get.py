"""
@File    :01创建网页之get.py
@Editor  : 百年
@Date    :2025/7/3 19:31 
"""

'''
`SessionPage`和`WebPage`的 s 模式基于 requests 进行网络连接，因此可使用 requests 内置的所有请求方式，包括`get()`、`post()`、`head()`、`options()`、`put()`
、`patch()`、`delete()`。不过本库目前只对`get()`和`post()`做了封装和优化，其余方式可通过调用页面对象内置的`Session`对象使用。这里只对`SessionPage`
进行说明，后面章节再单独介绍`WebPage`。'''

from DrissionPage import SessionPage

# `get()`方法语法与 requests 的`get()`方法一致，在此基础上增加了连接失败重试功能。与 requests 不一样的是，它不返回`Response`对象。


page = SessionPage()

url = 'https://www.baidu.com'
headers = {'referer': 'gitee.com'}
cookies = {'name': 'value'}
proxies = {'http': '127.0.0.1:1080', 'https': '127.0.0.1:1080'}
page.get(url, headers=headers, cookies=cookies, proxies=proxies)
print(page.html)