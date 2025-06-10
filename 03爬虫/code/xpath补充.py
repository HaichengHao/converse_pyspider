"""
@File    :xpath补充.py
@Editor  : 百年
@Date    :2025/4/27 10:57 
"""
import requests
from lxml import etree
from fake_useragent.fake import UserAgent
ua = UserAgent().random
url = 'https://ks.wangxiao.cn/exampoint/list?sign=jz1'
#
headers ={
    'User-Agent':ua
}
# print(ua)
response = requests.get(url=url,headers=headers)
page_source = response.text
print(page_source)
tree = etree.HTML(page_source)

# 找到一个类的父类节点
points = tree.xpath('//ul[@class="section-item"]')

fu_points = points.xpath('./ancestor-or-self::ul[@class="chapter-item" or @class="section-item"]')

#找到一个包含有section类的节点
pois = tree.xpath('//div[contains(@class,"section")]')


'''
与案例无关新补充:
以...开头 查找div标签中class属性值以pop开头的节点
res = tree.xpath('//div[starts-with(@class,"pop")]//text()')
'''