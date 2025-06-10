"""
@File    :01get请求.py
@Editor  : 百年
@Date    :2025/6/3 9:04 
"""
'''
`get()`方法语法与 requests 的`get()`方法一致，在此基础上增加了连接失败重试功能。
与 requests 不一样的是，它不返回`Response`对象，而是返回一个bool值，表示请求是否成功。
'''
from DrissionPage import SessionPage

page = SessionPage()
url = 'https://movie.douban.com/top250'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
}
cookies={
    'll':"118123"
}
# proxies_pool={'http': '127.0.0.1:1080', 'https': '127.0.0.1:1080'}
# param = {
#
# }

page.get(url=url,headers=headers,params=None,proxies=None,cookies=cookies,retry=None,interval=None,timeout=None)

print(page.html,page.title)
