"""
@File    :02post请求.py
@Editor  : 百年
@Date    :2025/7/3 19:37 
"""

from DrissionPage import SessionPage

page = SessionPage()
url = 'http://www.cpta.com.cn/category/search'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
}
data={
    'keywords':'财务',
    '搜 索':'搜 索'
}
page.post(url=url,headers=headers,data=data)
print(page.html,page.title)

'''
注意：在get和post请求中，headers中的User-Agent可以不写，
因为SessionPage和WebPage在创建页面对象时会自动加载一个ini的
配置文件，该配置文件中已经存在了User-Agent。'''

