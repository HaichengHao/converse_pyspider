"""
@File    :06批量获取信息的eles.py
@Editor  : 百年
@Date    :2025/6/1 23:25 
"""
from DrissionPage import ChromiumPage,ChromiumOptions
opt = ChromiumOptions().set_paths(local_port=9111,user_data_path=r'D:\Chromeopts\data1')

page1 = ChromiumPage(addr_or_opts=opt)

page1.get('https://movie.douban.com/top250')

# 定位到标题
titles = page1.eles('xpath://span[@class="title"]')

for title in titles:
    print(title.text)

#定位到链接
movie_hrefs = page1.ele('.grid_view').eles('t:a') #找到grid_view下的所有a标签

for movie_href in movie_hrefs:
    print(movie_href.link)