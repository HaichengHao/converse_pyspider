"""
@File    :05线程池案例.py
@Editor  : 百年
@Date    :2024/12/22 18:27 
"""
# 目标网站url https://ypk.39.net/pifu/p1/

import requests
from concurrent.futures.thread import ThreadPoolExecutor
import random
from lxml import etree
import csv

fp = open('../dataset/druginfo.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(fp)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1660.57",
}

proxies_pool = [
    {'http': '114.232.109.88:8089'},
    {'http': '114.231.42.23:8888'},
    {'http': '113.223.215.204:8089'},
    {'http': '117.69.236.23:8089'},
    {'http': '120.55.37.254:80'},
    {'http': '111.225.152.116:8089'},
    {'http': '36.6.145.4:8089'},
    {'http': '118.178.239.78:80'},
    {'http': '117.71.155.32:8089'},
    {'http': '117.57.92.25:8089'},
    {'http': '114.231.45.207:8888'},
    {'http': '113.223.214.141:8089'},
    {'http': '114.231.82.16:8089'},
    {'http': '111.225.152.64:8089'},
    {'http': '113.223.213.132:8089'},
    {'http': '117.69.233.129:8089'},
    {'http': '119.183.249.236:9000'},
    {'http': '36.6.145.95:8089'},
    {'http': '36.6.145.83:8089'},
    {'http': '117.69.233.19:8089'},
    {'http': '113.121.22.221:9999'},
    {'http': '183.164.242.59:8089'},
    {'http': '117.69.233.60:8089'},
    {'http': '121.41.79.83:80'},
    {'http': '42.63.65.99:80'},
    {'http': '36.6.144.210:8089'},
    {'http': '36.6.144.113:8089'},
    {'http': '183.164.243.43:8089'},
    {'http': '123.56.13.137:80'},
    {'http': '117.69.236.25:8089'},
    {'http': '117.71.154.141:8089'},
    {'http': '121.40.160.78:80'},
    {'http': '42.63.65.78:80'},
    {'http': '106.14.255.124:80'},
    {'http': '125.87.94.168:8089'},
    {'http': '47.94.207.215:3128'},
    {'http': '42.63.65.19:80'},
    {'http': '223.100.178.167:9091'},
    {'http': '117.70.49.102:8089'},
]


# proxies = random.choice(proxies_pool)


def download(url):
    proxies = random.choice(proxies_pool)
    response = requests.get(url=url, headers=headers, proxies=proxies)
    content = response.text
    tree = etree.HTML(content)  # IMPORTANT:调用etree解析页面源码
    namelst = tree.xpath('//div[@class="drugs-brief"]/p/a/@title')  # TIPS:获取药品名称
    efficacylst = tree.xpath('//div[@class="drugs-brief"]/p[2]/text()')  # TIPS:药品功效概述
    pricelst = tree.xpath('//div[@class="drugs-brief"]/p[4]/span/text()')  # TIPS:药品价格
    for i in range(len(namelst)):
        name = namelst[i].strip()
        efficacy = efficacylst[i].strip()
        try:
            price = pricelst[i].strip()
        except IndexError:
            price = ' '
        infolst = [name, efficacy, price]
        # tips:当然这里还可以用拼接字符串的写法
        print(infolst)
        writer.writerow(infolst)


if __name__ == '__main__':
    with ThreadPoolExecutor(10) as t:  # important:开启大小为20的线程池
        for j in range(2, 80):
            url = f'https://ypk.39.net/pifu/p{j}/'
            t.submit(download, url)
