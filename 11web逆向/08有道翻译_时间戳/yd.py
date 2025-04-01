"""
@File    :yd.py
@Editor  : 百年
@Date    :2025/3/28 13:58 
"""
import requests
import fake_useragent

useragent = fake_useragent.UserAgent.random
import execjs
import time

url = 'https://dict.youdao.com/webtranslate'
headers = {
    'User-Agent': useragent
}
word = input('输入单词>>')


# 创建节点
node = execjs.get()

# 读取js文件创建上下文对象
with open('youdao.js', 'r', encoding='utf-8') as fp:
    ctx = node.compile(fp.read())  # important:调用节点对js文件进行预编译
e = 'puppy'  # 传入要翻译的单词
pytime = time.time()
i = int(pytime * 1000)
print(i)
funcname = f'getSign("{e}","{i}")'
print(funcname)
result = ctx.eval(funcname)
print(result)
data = {
    'i': word,
    "from": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "i": "dog",
    "from": "auto",
    'to': '',
    "useTerm": "false",
    "dictResult": "true",
    "keyid": "webfanyi",
    "sign": result,
    "client": "fanyideskweb",
    "product": "webfanyi",
    "appVersion": "1 .0.0",
    "vendor": "web",
    "pointParam": "client,mysticTime,product",
    "mysticTime": "1743482642347",
    "keyfrom": "fanyi.web",
    "mid": "1",
    "screen": "1",
    "model": "1",
    "network": "wifi",
    "abtest": "0",
    "yduuid": "abcdefg",

}

response = requests.post(url=url,headers=headers,data=data)