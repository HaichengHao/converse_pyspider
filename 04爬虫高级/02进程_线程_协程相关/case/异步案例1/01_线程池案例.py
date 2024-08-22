# @Editor    : 百年
# @FileName  :01_线程池_案例.py
# @Time      :2024/7/28 17:38

# 本次xpath完整数据定位//li[@class="market-list-item"]/a/span[position()<5]
# 惠农网
import concurrent.futures
import time

import requests
import random
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import csv

proxies_pool = [
    {'http': '117.71.149.86:8089'},
    {'http': '114.232.109.72:8089'},
    {'http': '114.231.8.138:8888'},
    {'http': '123.182.58.79:8089'},
    {'http': '61.160.202.42:80'},
    {'http': '117.57.92.79:8089'},
    {'http': '117.71.133.98:8089'},
    {'http': '36.6.144.217:8089'},
    {'http': '117.69.236.70:8089'},
    {'http': '183.164.243.44:8089'},
    {'http': '39.175.75.144:30001'},
    {'http': '113.223.212.112:8089'},
    {'http': '121.40.160.78:80'},
    {'http': '113.223.213.3:8089'},
    {'http': '117.71.133.95:8089'},
    {'http': '182.204.183.168:8089'},
    {'http': '114.231.45.243:8089'},
    {'http': '118.31.1.154:80'},
    {'http': '36.6.144.84:8089'},
    {'http': '117.69.233.155:8089'},
    {'http': '117.71.133.10:8089'},
    {'http': '221.130.192.241:80'},
    {'http': '117.71.155.219:8089'},
    {'http': '114.231.109.127:8089'},
    {'http': '117.71.132.180:8089'},
    {'http': '113.223.215.142:8089'},
    {'http': '59.124.71.14:80'},
    {'http': '117.71.132.61:8089'},
    {'http': '101.37.26.136:80'},
    {'http': '121.41.97.228:80'},
    {'http': '42.63.65.103:80'},
    {'http': '103.38.183.10:84'},
    {'http': '117.69.236.15:8089'},
    {'http': '221.194.146.140:80'},
    {'http': '36.6.144.54:8089'},
    {'http': '42.63.65.59:80'},
    {'http': '183.164.243.239:8089'},
    {'http': '114.231.45.228:8888'},
    {'http': '36.6.144.211:8089'},
    {'http': '182.204.183.168:8089'},
    {'http': '114.231.45.243:8089'},
    {'http': '118.31.1.154:80'},
    {'http': '36.6.144.84:8089'},
    {'http': '117.69.233.155:8089'},
    {'http': '117.71.133.10:8089'},
    {'http': '221.130.192.241:80'},
    {'http': '117.71.155.219:8089'},
    {'http': '114.231.109.127:8089'},
    {'http': '117.71.132.180:8089'},
    {'http': '113.223.215.142:8089'},
    {'http': '59.124.71.14:80'},
    {'http': '117.71.132.61:8089'},
    {'http': '101.37.26.136:80'},
    {'http': '121.41.97.228:80'},
    {'http': '42.63.65.103:80'},
    {'http': '103.38.183.10:84'},
    {'http': '117.69.236.15:8089'},
    {'http': '221.194.146.140:80'},
    {'http': '36.6.144.54:8089'},
    {'http': '42.63.65.59:80'},
    {'http': '183.164.243.239:8089'},
    {'http': '114.231.45.228:8888'},
    {'http': '36.6.144.211:8089'},
    {'http': '117.69.232.114:8089'},
    {'http': '121.41.122.80:80'},
    {'http': '221.178.85.68:8080'},
    {'http': '60.174.0.98:8089'},
    {'http': '117.71.133.183:8089'},
    {'http': '223.215.177.37:8089'},
    {'http': '117.71.154.70:8089'},
    {'http': '111.40.62.199:9091'},
    {'http': '114.231.82.186:8089'},
    {'http': '114.232.109.73:8089'},
    {'http': '118.178.232.233:80'},
    {'http': '47.106.208.135:7777'},
    {'http': '114.106.137.169:8089'},
    {'http': '47.98.112.7:80'},
    {'http': '36.6.144.185:8089'},
    {'http': '42.63.65.103:80'},
    {'http': '103.38.183.10:84'},
    {'http': '117.69.236.15:8089'},
    {'http': '221.194.146.140:80'},
    {'http': '36.6.144.54:8089'},
    {'http': '42.63.65.59:80'},
    {'http': '183.164.243.239:8089'},
    {'http': '114.231.45.228:8888'},
    {'http': '36.6.144.211:8089'},
    {'http': '117.69.232.114:8089'},
    {'http': '121.41.122.80:80'},
    {'http': '221.178.85.68:8080'},
    {'http': '60.174.0.98:8089'},
    {'http': '117.71.133.183:8089'},
    {'http': '223.215.177.37:8089'},
    {'http': '117.71.154.70:8089'},
    {'http': '111.40.62.199:9091'},
    {'http': '114.231.82.186:8089'},
    {'http': '114.232.109.73:8089'},
    {'http': '118.178.232.233:80'},
    {'http': '47.106.208.135:7777'},
    {'http': '114.106.137.169:8089'},
    {'http': '47.98.112.7:80'},
    {'http': '36.6.144.185:8089'},
    {'http': '36.6.144.98:8089'},
    {'http': '140.249.88.102:80'},
    {'http': '113.223.214.125:8089'},
    {'http': '113.223.215.123:8089'},
    {'http': '114.55.179.125:80'},
    {'http': '36.6.145.151:8089'},
    {'http': '42.63.65.73:80'},
    {'http': '114.231.41.101:8089'},
    {'http': '47.113.230.224:3333'},
    {'http': '117.71.132.26:8089'},
    {'http': '123.182.59.84:8089'},
    {'http': '36.6.144.66:8089'},
    {'http': '113.223.213.118:8089'},
    {'http': '117.69.232.28:8089'},
    {'http': '183.234.218.201:9002'},
]
headers_pool = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",

]

# fp = open('../other/惠农网.csv', 'a+', encoding='utf-8')
# writer = csv.writer(fp)


def download(url):
    headers = {'User-Agent': random.choice(headers_pool)}
    response = requests.get(url, headers=headers, proxies=random.choice(proxies_pool))
    response.encoding = response.apparent_encoding
    content = response.text
    print(content)
    tree = etree.HTML(content)
    all_li = tree.xpath('//li[@class="market-list-item"]')
    # print(all_li)
    for li in all_li:
        date = li.xpath('/a/span[1]/text()')
        print(date)
        # time.sleep(5)
        # for data in alldata:
        #     writer.writerow(data, newline='')


if __name__ == '__main__':
    base_url='https://www.cnhnb.com/hangqing/cdlist-0-0-0-0-0-1/'
    download(base_url)
    # startpage = int(input('请输入起始页>>'))
    # endpage = int(input('请输入结束页>>'))
    # with concurrent.futures.ThreadPoolExecutor(10) as executor:
    #     for page in range(startpage, endpage + 1):
    #         url = f'https://www.cnhnb.com/hangqing/cdlist-0-0-0-0-0-{page}/'
    #         print(url)
    #         executor.submit(download, url)
# fp.close()
