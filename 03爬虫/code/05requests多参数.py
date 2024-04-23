# @Editor    : 百年
# @FileName  :05requests多参数.py
# @Time      :2024/4/21 18:55

# https://movie.douban.com/j/chart/top_list?

import requests

import random
from  lxml import etree

url = 'https://movie.douban.com/j/chart/top_list?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
# proxies_pool=[
#
# ]
# proxies = random.choice(proxies_pool)

data_={
    'type': '13',
    'interval_id':'100:90',
    'action':'',
    'start': '0',
    'limit': '20'

}
response  = requests.get(url=url,headers=headers,params=data_)
content = response.text
print(content)
# 我们再看一眼发送请求之后的生成的url变成了什么样子
print(response.request.url)

# https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=0&limit=20
# 同样的因为返回的是json数据，我们可以利用.json()方法来查看
print(response.json())