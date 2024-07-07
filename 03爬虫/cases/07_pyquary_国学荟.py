# @Editor    : 百年
# @FileName  :07_pyquary_.py
# @Time      :2024/7/7 19:35
from pyquery import PyQuery
import requests
import random

proxies_pool = [
    {'http': '114.231.46.79:8888'},
    {'http': '36.6.145.90:8089'},
    {'http': '117.69.233.98:8089'},
    {'http': '117.71.149.82:8089'},
    {'http': '117.71.154.81:8089'},
    {'http': '117.69.232.117:8089'},
    {'http': '117.69.154.91:41122'},
    {'http': '114.106.172.19:8089'},
    {'http': '123.182.59.184:8089'},
    {'http': '123.182.59.34:8089'},
    {'http': '36.6.144.104:8089'},
    {'http': '183.165.250.45:8089'},
    {'http': '121.230.211.163:8089'},
    {'http': '36.6.144.77:8089'},
    {'http': '223.215.177.245:8089'},
    {'http': '121.40.137.141:80'},
    {'http': '43.243.234.21:8000'},
    {'http': '60.174.0.61:8089'},
    {'http': '47.95.10.74:8888'},
    {'http': '117.71.154.177:8089'},
    {'http': '120.78.194.53:8888'},
    {'http': '111.224.10.69:8089'},
    {'http': '111.225.153.196:8089'},
    {'http': '112.17.16.199:80'},
    {'http': '36.6.145.167:8089'},
    {'http': '111.225.153.115:8089'},
    {'http': '112.17.16.213:80'},
    {'http': '114.231.45.194:8888'},
    {'http': '117.69.233.126:8089'},
    {'http': '117.69.237.184:8089'},
    {'http': '113.121.39.175:9999'},
    {'http': '121.43.102.172:80'},
    {'http': '114.232.109.246:8089'},
    {'http': '182.34.21.33:9999'},
    {'http': '117.69.232.202:8089'},
    {'http': '120.55.13.197:80'},
    {'http': '117.71.149.36:8089'},
    {'http': '121.40.103.179:80'},
    {'http': '112.17.16.156:80'}

]
proxies = random.choice(proxies_pool)
url = 'https://www.gushicimingju.com/gushi/gushisanbaishou/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
response = requests.get(url=url, headers=headers, proxies=proxies)
response.encoding = response.apparent_encoding
content = response.text
# print(content)
srctarget=PyQuery(content)
# 找到类名为simple-shiciqu的ul下的所有li
li=srctarget("ul.simple-shiciqu li")
# print(ul)
# li = ul('li')
# print(li)
# title_lst=[]
# 再找到所有的li的第一个子元素a,即为我们要找的诗词标题
title_all = li('a:first-child')
print(type(title_all))
dynasty_all = li('a:nth-child(2)')
# print(a.text())
# 这样获取的是一整块
it_dynasty=dynasty_all.items()
for dy in it_dynasty:
    print(dy.text())
# 为了获取所有的对象，要利用好.items(),因为以前是一整块儿
# it_title = title_all.items()
# for item in it_title:
#     print(item.text())
