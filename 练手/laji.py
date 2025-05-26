# @Author    : 百年
# @FileName  :laji.py
# @DateTime  :2025/5/20 20:36
import requests

from lxml import etree

fp = open('lj.txt','a+')
url = 'https://domei.cn/wenan/27637.html'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
}


resp = requests.get(url=url,headers=headers)
resp.encoding = resp.apparent_encoding
page_source = resp.text

tree = etree.HTML(page_source)

p_lst = tree.xpath('//div[@class="content"]/p[position()>1]/text()')
# print(page_source)
# print(p_lst)
for p in p_lst:
    p = p.split('、')[1]
    fp.write(p)
    print(p)
fp.close()