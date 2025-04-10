"""
@File    :demo.py
@Editor  : 百年
@Date    :2025/4/10 11:37 
"""
import requests
# from fake_useragent import UserAgent
from lxml import etree

# print(usera)
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}
url='https://www.hangzhou.gov.cn/art/2024/9/20/art_1229063407_4300152.html'
resp = requests.get(url=url,headers=headers)
resp.encoding = resp.apparent_encoding
page_source=resp.text
tree = etree.HTML(page_source)
artical = tree.xpath('//div[@class="article"]/p/text()')
# print(page_source)
print(artical)