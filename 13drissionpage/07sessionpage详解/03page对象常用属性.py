"""
@File    :03page对象常用属性.py
@Editor  : 百年
@Date    :2025/6/3 9:19
"""
'''
url:此属性返回当前访问的 url。
title:此属性返回当前页面title文本。
raw_data:此属性返回访问到的二进制数据，即Response对象的content属性。
html：此属性返回当前页面 html 文本。
json：此属性把返回内容解析成 json。比如请求接口时，若返回内容是 json 格式，
用html属性获取的话会得到一个字符串，用此属性获取可将其解析成dict。'''

#结合lxml与sessionpage来获取豆瓣的电影信息以及图片信息
from DrissionPage import SessionPage
from lxml import etree
page = SessionPage()
url = 'https://movie.douban.com/top250'
page.get(url)
print(page.url)
print(page.title)
# print(page.html)
page_source = page.html
tree = etree.HTML(page_source)

# movies_title = tree.xpath('//span[@class="title"][1]/text()')
# movie_pic = tree.xpath('//div[@class="item"]//img/@src')
movie_title = page.ele('xpath://li[1]//span[@class="title"][1]')
imgs_url = page.ele('xpath://ol[@class="grid_view"]/li[1]//img/@src')
print(movie_title.text,imgs_url)


save_path = f'./demo/{movie_title.text}.jpg'
res = page.download(imgs_url,save_path)
print(res)