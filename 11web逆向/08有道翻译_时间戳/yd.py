"""
@File    :yd.py
@Editor  : 百年
@Date    :2024/3/28 13:58
"""
import requests
import fake_useragent

useragent = fake_useragent.UserAgent.random
import execjs
import time

url = 'https://dict.youdao.com/webtranslate'
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    'Cookie':"OUTFOX_SEARCH_USER_ID=-949120315@2001:da8:9000:a835:611c:f5ae:87f8:cf85; OUTFOX_SEARCH_USER_ID_NCOO=1052122220.6186857; _uetsid=b1c02df02c1911f080426bbe57cdc13d; _uetvid=a4bcc1900af711f090db7fac1e6cb752; ___rl__test__cookies=1746714947009"
}
word = input('输入单词>>')

# 创建节点
node = execjs.get()

# 读取js文件创建上下文对象
with open('youdao.js', 'r', encoding='utf-8') as fp:
    ctx = node.compile(fp.read())  # important:调用节点对js文件进行预编译
# e = 'puppy'  # 传入要翻译的单词

pytime = time.time()
i = int(pytime * 1000)
print(i)
funcname = f'getSign("{word}","{i}")'
print(funcname)
result = ctx.eval(funcname)
print(result)
data = {
    "i": word,
    "from": "en",
    'to': 'zh-CHS',
    "useTerm": "false",
    "domain":0,
    "dictResult": "true",
    "keyid": "webfanyi",
    "sign": result,
    "client": "fanyideskweb",
    "product": "webfanyi",
    "appVersion": "1.0.0",
    "vendor": "web",
    "pointParam": "client,mysticTime,product",
    "mysticTime": f"{i}",
    "keyfrom": "fanyi.web",
    "mid": "1",
    "screen": "1",
    "model": "1",
    "network": "wifi",
    "abtest": "0",
    "yduuid": "abcdefg",

}

response = requests.post(url=url, headers=headers, data=data)
print(response.text)
# print(response.json())
