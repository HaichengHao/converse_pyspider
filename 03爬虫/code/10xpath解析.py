# @Editor    : 百年
# @FileName  :10xpath解析.py
# @Time      :2024/7/3 18:24
from lxml import etree
import requests
import random
import time
import csv

fp = open('../others/szzf.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(fp)
# base_url = 'https://sz.zu.anjuke.com/fangyuan/p1/'
# 代理池
proxies_pool = [
    {'http': '183.164.243.155:8089'},
    {'http': '114.231.105.68:8089'},
    {'http': '60.188.5.160:80'},
    {'http': '117.71.155.47:8089'},
    {'http': '117.69.232.13:8089'},
    {'http': '47.99.134.192:80'},
    {'http': '112.124.32.237:80'},
    {'http': '113.223.213.88:8089'},
    {'http': '114.231.46.160:8089'},
    {'http': '117.57.92.22:8089'},
    {'http': '183.164.242.4:8089'},
    {'http': '182.34.33.244:9999'},
    {'http': '113.223.214.227:8089'},
    {'http': '47.95.10.74:8888'},
    {'http': '113.223.213.77:8089'},
    {'http': '121.43.32.135:80'},
    {'http': '117.71.155.147:8089'},
    {'http': '117.71.133.234:8089'},
    {'http': '114.232.110.68:8089'},
    {'http': '117.71.149.175:8089'},
    {'http': '36.6.144.178:8089'},
    {'http': '117.57.93.128:8089'},
    {'http': '58.220.95.55:9400'},
    {'http': '183.164.243.14:8089'},
    {'http': '183.164.243.2:8089'},
    {'http': '139.159.176.147:8090'},
    {'http': '36.6.144.89:8089'},
    {'http': '114.232.109.207:8089'},
    {'http': '114.80.179.210:80'},
    {'http': '117.69.236.252:8089'},
    {'http': '114.231.41.19:8888'},
    {'http': '36.6.144.19:8089'},
    {'http': '36.6.144.2:8089'},
    {'http': '114.231.42.244:8089'},
    {'http': '111.224.212.84:8089'},
    {'http': '125.229.167.69:3128'},
    {'http': '112.17.16.180:80'},
    {'http': '118.178.237.222:80'},
    {'http': '117.69.232.18:8089'},
    {'http': '121.43.32.135:80'},
    {'http': '117.71.155.147:8089'},
    {'http': '117.71.133.234:8089'},
    {'http': '114.232.110.68:8089'},
    {'http': '117.71.149.175:8089'},
    {'http': '36.6.144.178:8089'},
    {'http': '117.57.93.128:8089'},
    {'http': '58.220.95.55:9400'},
    {'http': '183.164.243.14:8089'},
    {'http': '183.164.243.2:8089'},
    {'http': '139.159.176.147:8090'},
    {'http': '36.6.144.89:8089'},
    {'http': '114.232.109.207:8089'},
    {'http': '114.80.179.210:80'},
    {'http': '117.69.236.252:8089'},
    {'http': '114.231.41.19:8888'},
    {'http': '36.6.144.19:8089'},
    {'http': '36.6.144.2:8089'},
    {'http': '114.231.42.244:8089'},
    {'http': '111.224.212.84:8089'},
    {'http': '125.229.167.69:3128'},
    {'http': '112.17.16.180:80'},
    {'http': '118.178.237.222:80'},
    {'http': '117.69.232.18:8089'},
    {'http': '36.6.144.100:8089'},
    {'http': '114.103.88.117:8089'},
    {'http': '49.71.144.207:8089'},
    {'http': '36.6.145.241:8089'},
    {'http': '112.124.7.79:80'},
    {'http': '114.232.110.142:8888'},
    {'http': '125.87.94.137:8888'},
    {'http': '222.190.173.100:8089'},
    {'http': '114.231.41.237:8089'},
    {'http': '114.231.8.138:8888'},
    {'http': '118.31.32.221:80'},
    {'http': '60.188.5.198:80'},
    {'http': '182.34.100.118:9999'},
    {'http': '114.231.42.97:8888'},
    {'http': '113.56.95.6:8111'},
    {'http': '114.231.41.19:8888'},
    {'http': '36.6.144.19:8089'},
    {'http': '36.6.144.2:8089'},
    {'http': '114.231.42.244:8089'},
    {'http': '111.224.212.84:8089'},
    {'http': '125.229.167.69:3128'},
    {'http': '112.17.16.180:80'},
    {'http': '118.178.237.222:80'},
    {'http': '117.69.232.18:8089'},
    {'http': '36.6.144.100:8089'},
    {'http': '114.103.88.117:8089'},
    {'http': '49.71.144.207:8089'},
    {'http': '36.6.145.241:8089'},
    {'http': '112.124.7.79:80'},
    {'http': '114.232.110.142:8888'},
    {'http': '125.87.94.137:8888'},
    {'http': '222.190.173.100:8089'},
    {'http': '114.231.41.237:8089'},
    {'http': '114.231.8.138:8888'},
    {'http': '118.31.32.221:80'},
    {'http': '60.188.5.198:80'},
    {'http': '182.34.100.118:9999'},
    {'http': '114.231.42.97:8888'},
    {'http': '113.56.95.6:8111'},
    {'http': '42.63.65.117:80'},
    {'http': '117.71.155.208:8089'},
    {'http': '112.80.248.75:80'},
    {'http': '117.57.93.15:8089'},
    {'http': '117.57.92.5:8089'},
    {'http': '114.232.110.34:8888'},
    {'http': '47.107.61.215:8000'},
    {'http': '113.207.40.42:8080'},
    {'http': '121.43.232.142:80'},
    {'http': '117.71.155.163:8089'},
    {'http': '114.231.45.243:8089'},
    {'http': '101.37.163.83:80'},
    {'http': '117.69.233.118:8089'},
    {'http': '114.104.135.98:41122'},
    {'http': '47.99.73.126:80'},

]
proxies = random.choice(proxies_pool)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

for i in range(3):
    url = f'https://sz.zu.anjuke.com/fangyuan/p{i + 1}/'
    response = requests.get(url=url, headers=headers, proxies=proxies)
    content = response.text
    tree = etree.HTML(content)
    urls = tree.xpath("//div[@class='zu-itemmod clearfix']/@link")
    for url in urls:
        print(url)
        new_response = requests.get(url=url, headers=headers, proxies=proxies)
        new_content = new_response.text
        n_tree = etree.HTML(new_content)
        try:
            house_title = n_tree.xpath("//h1['house-title']/div[1]/text()")[0]
        except IndexError:
            house_title = ''
        try:
            price = n_tree.xpath("//span[@class='price']/em/b/text()")[0]
        except IndexError:
            price = ''
        try:
            renttype = n_tree.xpath("//ul[@class='house-info-zufang cf']/li[1]/span[2]/text()")[0]
        except IndexError:
            renttype = ''
        try:
            area = n_tree.xpath("//ul[@class='house-info-zufang cf']/li[3]/span[2]/b/text()")[0]
        except IndexError:
            area = ''
        try:
            direction = n_tree.xpath("//ul[@class='house-info-zufang cf']/li[4]/span[2]/text()")[0]
        except IndexError:
            direction = ''
        try:
            floor = n_tree.xpath("//ul[@class='house-info-zufang cf']/li[5]/span[2]/text()")[0]
        except IndexError:
            floor = ''
        try:
            decoration = n_tree.xpath("//ul[@class='house-info-zufang cf']/li[6]/span[2]/text()")[0]
        except IndexError:
            decoration = ''
        try:
            house_ues = n_tree.xpath("//ul[@class='house-info-zufang cf']/li[7]/span[2]/text()")[0]
        except IndexError:
            house_ues = ''
        try:
            block = n_tree.xpath("//ul[@class='house-info-zufang cf']/li[8]/a[1]/text()")[0]
        except IndexError:
            block = ''
        rentinfolst = [house_title, price, renttype, area, direction, floor, decoration, house_ues, block]
        print(rentinfolst)
        writer.writerow(rentinfolst)
# 打印查看结果
# print(content)
fp.close()
print('运行结束')
