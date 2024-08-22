# @Editor    : 百年
# @FileName  :09_新发地菜市场.py
# @Time      :2024/6/30 17:37
import random
import requests
import json
fp = open('../others/xfd.txt','a+',encoding='utf-8')
url = 'http://www.xinfadi.com.cn/getPriceData.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
proxies_pool = [
    {'http': '42.63.65.37:80'},
    {'http': '42.63.65.13:80'},
    {'http': '42.63.65.15:80'},
    {'http': '42.63.65.7:80'},
    {'http': '42.63.65.8:80'},
    {'http': '42.63.65.9:80'},
    {'http': '39.173.106.248:80'},
    {'http': '39.173.106.249:80'}
]
proxies=random.choice(proxies_pool)
response=requests.post(url=url,headers=headers)
content=response.text
# print(content)
# print(type(content))

# 反序列化(字典化，将字符串类型转变为字典类型)
# js_content=json.loads(content)
# print(js_content,type(js_content))
vegitable=response.json().get('list')
# print(vegitable)
for veg in vegitable:
    prodname=veg.get('prodName')
    lowprice=veg.get('lowPrice')
    highprice=veg.get('highPrice')
    print(f"菜名:{prodname},低价:{lowprice},高价:{highprice}")
    fp.write(f"菜名:{prodname},低价:{lowprice},高价:{highprice}\n")