"""
@File    :名单.py
@Editor  : 百年
@Date    :2025/4/9 14:18 
"""
import requests
from lxml import etree
# url='https://www.dxsbb.com/news/1596.html'
url='https://www.dxsbb.com/news/64928.html'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}
resp = requests.get(url=url,headers=headers)
resp.encoding = resp.apparent_encoding
page_source = resp.text
tree = etree.HTML(page_source)
# print(page_source)
td_lst = tree.xpath('//tbody/tr[position()>1]')
for item in td_lst:
    rank=item.xpath('./td[2]')
    for i in rank:
        print(i)
    print(rank,type(rank))