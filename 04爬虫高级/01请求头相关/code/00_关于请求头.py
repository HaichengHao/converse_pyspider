# @Editor    : 百年
# @FileName  :00_关于请求头.py
# @Time      :2024/7/10 12:25
'''
session本意是服务器端用来保存用户状态的一个超大号字典
sessionid 是保存在浏览器端的一个值，一般情况下浏览器会把SessionID写入到cookie中
session 保持会话
cookie 本质是浏览器端的一个文件，里面存储着一个超大号的字符串
在发送请求的时候，你的浏览器会自动的带着所有的cookie 访问到服务器
cookie里面有url,字符串的键值对，过期时间

'''
import random

import requests
from lxml import etree

session = requests.session()
proxies_pool = [
    {'http': '182.204.178.124:8089'},
    {'http': '114.232.110.17:8888'},
    {'http': '223.247.47.1:8089'},
    {'http': '183.164.243.232:8089'},
    {'http': '159.226.227.116:80'},
    {'http': '117.71.155.98:8089'},
    {'http': '117.69.236.26:8089'},
    {'http': '117.71.132.105:8089'},
    {'http': '117.69.236.238:8089'},
    {'http': '113.121.47.64:9999'},
    {'http': '116.62.34.88:80'},
    {'http': '175.178.62.35:8880'},
    {'http': '61.186.204.158:7001'},
    {'http': '114.231.46.149:8089'},
    {'http': '47.96.43.57:80'},
    {'http': '114.231.42.107:8089'},
    {'http': '117.71.132.21:8089'},
    {'http': '114.55.176.8:80'},
    {'http': '117.69.237.27:8089'},
    {'http': '121.43.101.160:80'},
    {'http': '120.27.140.17:80'},
    {'http': '111.225.152.202:8089'},
    {'http': '221.194.146.156:80'},
    {'http': '27.147.24.205:8080'},
    {'http': '182.204.178.124:8089'},
    {'http': '114.232.110.17:8888'},
    {'http': '223.247.47.1:8089'},
    {'http': '183.164.243.232:8089'},
    {'http': '159.226.227.116:80'},
    {'http': '117.71.155.98:8089'},
    {'http': '117.69.236.26:8089'},
    {'http': '117.71.132.105:8089'},
    {'http': '117.69.236.238:8089'},
    {'http': '113.121.47.64:9999'},
    {'http': '116.62.34.88:80'},
    {'http': '175.178.62.35:8880'},
    {'http': '117.71.155.214:8089'},
    {'http': '114.231.46.200:8888'},
    {'http': '114.231.45.79:8089'},
    {'http': '60.174.0.143:8089'},
    {'http': '117.57.92.191:8089'},
    {'http': '36.6.144.124:8089'},
    {'http': '47.96.70.163:8888'},
    {'http': '118.31.105.240:80'},
    {'http': '210.61.216.63:60808'},
    {'http': '117.71.132.130:8089'},
    {'http': '47.100.69.29:8888'},
    {'http': '111.225.153.150:8089'},
    {'http': '42.63.65.94:80'},
    {'http': '112.51.96.118:9091'},
    {'http': '111.225.152.47:8089'},
    {'http': '183.164.243.232:8089'},
    {'http': '159.226.227.116:80'},
    {'http': '117.71.155.98:8089'},
    {'http': '117.69.236.26:8089'},
    {'http': '117.71.132.105:8089'},
    {'http': '117.69.236.238:8089'},
    {'http': '113.121.47.64:9999'},
    {'http': '116.62.34.88:80'},
    {'http': '175.178.62.35:8880'},
    {'http': '117.71.155.214:8089'},
    {'http': '114.231.46.200:8888'},
    {'http': '114.231.45.79:8089'},
    {'http': '60.174.0.143:8089'},
    {'http': '117.57.92.191:8089'},
    {'http': '36.6.144.124:8089'},
    {'http': '47.96.70.163:8888'},
    {'http': '118.31.105.240:80'},
    {'http': '210.61.216.63:60808'},
    {'http': '117.71.132.130:8089'},
    {'http': '47.100.69.29:8888'},
    {'http': '111.225.153.150:8089'},
    {'http': '42.63.65.94:80'},
    {'http': '112.51.96.118:9091'},
    {'http': '111.225.152.47:8089'},
    {'http': '36.6.145.203:8089'},
    {'http': '117.71.154.249:8089'},
    {'http': '159.226.227.96:80'},
    {'http': '111.225.152.189:8089'},
    {'http': '120.55.14.64:80'},
    {'http': '117.69.237.90:8089'},
    {'http': '114.231.45.93:8089'},
    {'http': '113.223.213.178:8089'},
    {'http': '223.100.178.167:9091'},
    {'http': '113.121.22.221:9999'},
    {'http': '117.71.133.139:8089'},
    {'http': '114.232.109.30:8089'},
    {'http': '114.231.45.228:8888'},
    {'http': '60.174.0.139:8089'},
    {'http': '113.143.37.82:9002'},
]
proxies = random.choice(proxies_pool)
User_Agent = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR "
    "2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center "
    "PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET "
    "CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR "
    "3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR "
    "2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; "
    ".NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) "
    "Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 "
    "Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 "
    "Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 "
    "TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 "
    "Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET "
    "CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 "
    "Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET "
    "CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET "
    "CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; "
    "360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET "
    "CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) "
    "Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 "
    "Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) "
    "Firefox/3.6.10 "
]

headers = {
    'User_Agent': random.choice(User_Agent)
}

data = {
    "loginName": "18864771568",
    "password": "HHCzio20."
}
url = "https://passport.17k.com/ck/user/login"
session.post(url=url, headers=headers, data=data, proxies=proxies)
# content = response.text
# cookie = response.cookies
# print(cookie)


# 拿到书架上的数据
new_url = 'https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919'
newresp = session.get(url=new_url)
newcontent = newresp.text
print(newcontent)
