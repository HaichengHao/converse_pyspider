"""
@File    :demo3.py
@Editor  : 百年
@Date    :2025/2/22 15:38 
"""
import requests
#动态获取rsa的公钥数据
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
}
url = 'https://store.steampowered.com/login/getrsakey/'
data = {
    "donotcache": "1647951542258",
    "username": "bobo@qq.com"
}
json_data = requests.post(url,headers=headers,data=data).json()
mod = json_data['publickey_mod']
exp = json_data['publickey_exp']

import execjs
node = execjs.get()
fp = open('tst.js','r',encoding='utf-8')
ctx = node.compile(fp.read())
pwd = "123456"
jsFunc = 'getPwd("%s","%s","%s")'%(pwd,mod,exp)
result = ctx.eval(jsFunc)
print(result)