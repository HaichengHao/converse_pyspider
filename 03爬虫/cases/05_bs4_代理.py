# @Editor    : 百年
# @FileName  :05_bs4_代理.py
# @Time      :2024/7/3 17:09
from bs4 import BeautifulSoup
import requests

ip_lst = []
number = int(input('请输入你要爬取到的页数:'))
for i in range(number):

    url = 'https://www.89ip.cn/index_' + f'{i + 1}' + '.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    content = response.text
    # print(content)

    page_source = BeautifulSoup(content, 'lxml')
    # 获取所有的tr中的第一个td和第二个td
    # print(page_source)
    trs = page_source.select('tbody>tr:not(:first-child)')

    # print(trs)
    for tr in trs:
        ip = tr.findAll('td')[0].text.strip()  # 去掉前后的空格
        port = tr.findAll('td')[1].text.strip()
        prox = '{\'http\':' + '\'' + f'{ip}:{port}' + '\'},'
        print(prox)
        # ip_lst.append(prox)
        # print()
# print(ip_lst)
'''
请输入你要爬取到的页数:2
{'http':'114.99.7.225:8089'}
{'http':'36.6.145.196:8089'}
{'http':'36.6.144.48:8089'}
{'http':'117.69.232.220:8089'}
{'http':'42.63.65.56:80'}
{'http':'120.79.16.132:8499'}
{'http':'183.164.242.138:8089'}
{'http':'117.71.155.163:8089'}
{'http':'183.164.242.160:8089'}
{'http':'114.231.45.52:8089'}
{'http':'120.26.13.191:80'}
{'http':'114.106.136.157:8089'}
{'http':'139.196.151.191:3333'}
{'http':'121.40.251.172:80'}
{'http':'36.6.145.21:8089'}
{'http':'120.205.70.102:8060'}
{'http':'39.108.145.28:8080'}
{'http':'106.14.255.124:80'}
{'http':'58.20.20.78:2323'}
{'http':'117.71.154.135:8089'}
{'http':'183.166.170.138:41122'}
{'http':'117.71.133.12:8089'}
{'http':'123.182.59.180:8089'}
{'http':'183.164.243.140:8089'}
{'http':'183.164.242.255:8089'}
{'http':'47.109.57.93:6969'}
{'http':'114.231.42.107:8089'}
{'http':'114.231.82.92:8888'}
{'http':'183.164.243.246:8089'}
{'http':'117.69.233.77:8089'}
{'http':'47.94.57.119:80'}
{'http':'47.93.232.37:80'}
{'http':'121.194.10.72:80'}
{'http':'121.41.98.168:80'}
{'http':'121.5.15.118:80'}
{'http':'123.56.13.137:80'}
{'http':'60.174.1.219:8089'}
{'http':'112.17.16.199:80'}
{'http':'111.225.153.123:8089'}

Process finished with exit code 0
'''