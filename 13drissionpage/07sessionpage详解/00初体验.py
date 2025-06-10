"""
@File    :00初体验.py
@Editor  : 百年
@Date    :2025/6/2 23:36 
"""
'''
顾名思义，SessionPage是一个使用Session（requests 库）对象的页面，
且它还封装了网络连接和 html 解析功能，使收发数据包也可以像操作页面一样便利。
并且，由于加入了本库独创的查找元素方法，使数据的采集便利性远超 requests + beautifulsoup 等组合。
'''

from DrissionPage import SessionPage

#创建页面对象
page = SessionPage()
page.get(url = 'https://movie.douban.com/top250')

# 定位到标题
titles = page.eles('xpath://span[@class="title"]')

for title in titles:
    print(title.text.strip())

#定位到链接
movie_hrefs = page.ele('.grid_view').eles('t:a') #找到grid_view下的所有a标签

for movie_href in movie_hrefs:
    print(movie_href.link)
