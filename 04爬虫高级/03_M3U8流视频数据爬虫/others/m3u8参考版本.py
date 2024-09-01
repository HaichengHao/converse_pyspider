# @Editor    : 百年
# @FileName  :01初体验.py
# @Time      :2024/9/1 10:55
import requests
import random
import os
from urllib.parse import urljoin
from lxml import etree
# 解密文件
# pip install pycryptodome
# 导入解密AES 的模块
from crypto.Cipher import AES
# 要解析key文件我们需要用正则模块
import re

dirname = '../others/tsLib'
if not os.path.exists(dirname):
    os.mkdir(dirname)
proxies_pool = [
    {'http': '114.231.45.224:8888'},
    {'http': '114.103.88.253:8089'},
    {'http': '223.215.177.237:8089'},
    {'http': '114.231.41.56:8089'},
    {'http': '118.31.1.128:80'},
    {'http': '121.41.99.161:80'},
    {'http': '117.71.149.168:8089'},
    {'http': '112.243.228.40:9000'},
    {'http': '182.34.20.6:9999'},
    {'http': '183.164.242.35:8089'},
    {'http': '42.63.65.104:80'},
    {'http': '183.166.170.138:41122'},
    {'http': '114.231.8.26:8888'},
    {'http': '47.96.38.188:80'},
    {'http': '113.223.215.142:8089'},
    {'http': '123.182.58.95:8089'},
    {'http': '123.182.58.217:8089'},
    {'http': '114.55.109.154:80'},
    {'http': '114.232.110.136:8089'},
    {'http': '114.231.8.15:8089'},
    {'http': '113.121.40.189:9999'},
    {'http': '117.71.149.67:8089'},
    {'http': '60.174.1.54:8089'},
    {'http': '121.40.160.211:80'},
    {'http': '111.225.153.246:8089'},
    {'http': '111.225.153.150:8089'},
    {'http': '49.71.144.83:8089'},
    {'http': '101.37.163.83:80'},
    {'http': '111.225.152.48:8089'},
    {'http': '117.71.132.26:8089'},
    {'http': '182.34.26.109:9999'},
    {'http': '61.160.202.73:80'},
    {'http': '60.5.254.16:8080'},
    {'http': '39.173.106.239:80'},
    {'http': '210.13.117.18:443'},
    {'http': '114.231.45.3:8888'},
    {'http': '42.63.65.73:80'},
    {'http': '117.57.92.207:8089'},
    {'http': '114.231.46.104:8089'},
    {'http': '123.182.58.95:8089'},
    {'http': '123.182.58.217:8089'},
    {'http': '114.55.109.154:80'},
    {'http': '114.232.110.136:8089'},
    {'http': '114.231.8.15:8089'},
    {'http': '113.121.40.189:9999'},
    {'http': '117.71.149.67:8089'},
    {'http': '60.174.1.54:8089'},
    {'http': '121.40.160.211:80'},
    {'http': '111.225.153.246:8089'},
    {'http': '111.225.153.150:8089'},
    {'http': '49.71.144.83:8089'},
    {'http': '101.37.163.83:80'},
    {'http': '111.225.152.48:8089'},
    {'http': '117.71.132.26:8089'},
    {'http': '182.34.26.109:9999'},
    {'http': '61.160.202.73:80'},
    {'http': '60.5.254.16:8080'},
    {'http': '39.173.106.239:80'},
    {'http': '210.13.117.18:443'},
    {'http': '114.231.45.3:8888'},
    {'http': '42.63.65.73:80'},
    {'http': '117.57.92.207:8089'},
    {'http': '114.231.46.104:8089'},
    {'http': '120.26.14.131:80'},
    {'http': '117.71.154.175:8089'},
    {'http': '120.27.143.33:80'},
    {'http': '223.215.176.10:8089'},
    {'http': '111.225.153.238:8089'},
    {'http': '114.106.172.37:8089'},
    {'http': '118.31.247.119:80'},
    {'http': '117.71.149.113:8089'},
    {'http': '42.63.65.15:80'},
    {'http': '183.165.245.254:8089'},
    {'http': '61.135.169.121:80'},
    {'http': '36.6.145.49:8089'},
    {'http': '221.122.91.64:80'},
    {'http': '111.225.153.81:8089'},
    {'http': '36.6.144.6:8089'}

]
proxies = random.choice(proxies_pool)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
base_url = "https://two.svipplay.com/lzm3u8/20d71cfa5b0a15762e155668380568d8.m3u8?token=7aGefVkrV2BD6B6xtu-ETg&expires=1725159095"

response = requests.get(url=base_url, headers=headers, proxies=proxies)
response.encoding = response.apparent_encoding
content = response.text.strip()  # 利用strip()方法去除回车换行以及左右空格
for line in content.split('\n'):
    if not line.startswith('#'):  # 如果遍历出的这一行不是以井号开头那就是我们需要的二级地址
        m2_url = line
        # 将base_url和m2_url的不同之处拼接到m2_url中
        # 即 m2_url = base_url|m2_url - base_url^m2_url
        m2_url = urljoin(base_url, m2_url)
        # 至此就获取到了完整的二级文件地址，但是在code文件中我写的链接请求已经是二级，所以对这个代码不适用，如果想爬取的视频确实做了一级不加载ts而二级加载ts,那么你就可以以这个py文件的代码作为参考
        # 将会对其进行优化
        # 如果有加密，那么我们需要对加密的key进行破解
        # 接下来要做两件事情，
        # 1解析出mw_url中解密密钥key的地址
        key_loc = re.findall('URL="(.*?)"', m2_url, re.S)
        print(key_loc)
        # 2请求key的地址，获取密钥
        keyresponse = requests.get(url=key_loc)
        key_info = keyresponse.text
        print(key_info)  # 打印key_info
        # 接着我们要拼接请求链接来得到完整的url
        key_url = urljoin(base_url, key_info)
        # 接下来请求key_url来获得密钥,注意:key和iv(加密向量)需要为bytes类型
        key = requests.get(url=key_url, headers=headers)
        key_content = key.content  # 注意,requsets模块如果得到的是二进制返回值那么就不能用.text了，得用获得二进制内容的模块.content
        # 如果无加密向量就自己写16个0，也就是两个字节的全0
        iv = b'0000000000000000'
        print(key_content)
        # 3解析出每一个ts切片的地址
        # 创建一个列表保存所有的ts链接
        ts_lst = []
        for line in m2_url.split('\n'):
            if not line.startswith('#'):
                ts_url = line
                #         拼接链接
                ts_url = urljoin(base_url, ts_url)
                # 将每一个ts_url都添加到ts_lst列表中
                ts_lst.append(ts_url)
        #         这样我们就得到了所有的ts

        # 4请求到每个ts切片的数据
        for url in ts_lst:
            # 获取ts片段的数据
            ts_data = requests.get(url=url, headers=headers).content
            # 需要对ts片段数据进行解密,密钥就是我们刚才获取到的密钥
            aes = AES.new(key=key_content, mode=AES.MODE_CBC, iv=iv)
            desc_data = aes.decrypt(ts_data) #获取了解密后的数据
            ts_name = url.split('/')[-1]
            ts_path = dirname + '/' + ts_name
            with open(ts_path, 'wb') as fp:
                fp.write(desc_data)
            break  # 加上break是因为目前只想爬取一个片段，不然太多会耗费时间和流量
        #     可以新建一个文件用来保存所有的ts

        # 5使用密钥key和iv向量对ts片段进行解密
        # 需要引入crypto
        # from crypto.Cipher import AES
        # 之后再解密每个ts片段
        # 6拼接每一个ts片段合并成完整的视频文件(可能会很慢，所以不全爬，之后会用协程来优化)
        # 不过这里的ts文件的合并最好是找网上专业的合并工具。。。。。自己手动合并经常会出问题!!
        # 在终端中的合并(linux) cat *.ts > fina.mp4
        # 工具推荐用ffmpeg
        # 官网https://ffmpeg.org/