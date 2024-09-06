# @Editor    : 百年
# @FileName  :01美剧网.py
# @Time      :2024/9/6 15:29
import requests
import random
# 导入urljoin,实现链接的拼接
from urllib.parse import urljoin
# urljoin可以实现不同的链接之间拼接，相同的地方会合并
import os
dirname = '../others/tsl2'
if not os.path.exists(dirname):
    os.mkdir(dirname)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
proxies_pool = [
    {'http': '101.43.217.237:7890'},
    {'http': '220.181.111.37:80'},
    {'http': '113.223.212.23:8089'},
    {'http': '117.71.155.96:8089'},
    {'http': '47.113.219.226:9091'},
    {'http': '118.178.237.222:80'},
    {'http': '61.175.214.2:9091'},
    {'http': '113.223.214.102:8089'},
    {'http': '117.69.232.88:8089'},
    {'http': '121.43.103.197:80'},
    {'http': '117.71.154.95:8089'},
    {'http': '117.57.93.8:8089'},
    {'http': '47.113.230.224:3333'},
    {'http': '47.99.139.203:80'},
    {'http': '117.57.93.206:8089'},
    {'http': '47.113.221.120:1080'},
    {'http': '36.6.145.60:8089'},
    {'http': '183.164.242.40:8089'},
    {'http': '159.226.227.96:80'},
    {'http': '113.223.215.161:8089'},
    {'http': '121.40.139.129:80'},
    {'http': '117.71.149.176:8089'},
    {'http': '125.87.88.192:8089'},
    {'http': '113.121.47.154:9999'},
    {'http': '36.6.144.183:8089'},
    {'http': '117.57.93.90:8089'},
    {'http': '120.196.207.10:80'},
    {'http': '36.6.144.95:8089'},
    {'http': '36.6.144.23:8089'},
    {'http': '114.231.45.119:8089'},
    {'http': '113.223.212.139:8089'},
    {'http': '183.164.243.115:8089'},
    {'http': '58.20.248.139:9002'},
    {'http': '61.160.202.109:80'},
    {'http': '114.231.46.104:8089'},
    {'http': '117.69.236.23:8089'},
    {'http': '117.71.132.7:8089'},
    {'http': '47.96.39.52:80'},
    {'http': '117.71.154.175:8089'}

]
proxies = random.choice(proxies_pool)
base_url = 'https://vod6.bdzybf11.com/20240904/i1WOYJkk/index.m3u8'
response = requests.get(url=base_url, headers=headers, proxies=proxies)
content = response.text.strip()#利用strip()去除回车
# print(content)
for line in content.split('\n'):
    if not line.startswith('#'):
        stp2_url = line
        print(stp2_url)
        newurl = urljoin(base_url,stp2_url)
        # print(newurl)
        stp2_response = requests.get(url=newurl,headers=headers,proxies=proxies)
        stp2_content = stp2_response.text.strip()
        # print(stp2_content)
        for line in stp2_content.split('\n'):
            if not line.startswith('#'):
                stp3_url = urljoin(base_url,line)
                print(stp3_url)
                final_response = requests.get(url=stp3_url,headers=headers,proxies=proxies)
                bin_content = final_response.content
                ts_name = stp3_url.split('/')[-1]
                print(ts_name)
                s_path = dirname + '/' + ts_name
                with open(s_path, 'wb') as f:
                    f.write(bin_content)
                break #只爬一段就行，电脑放不下太多，当然如果刚好就是你喜欢的你也恰好想看那随意即可
#                 拼接ts,ffmpg就行

