"""
@File    :sklm.py
@Editor  : 百年
@Date    :2025/3/27 11:33 
"""
# important:动态提取rsa_n的值
import requests
import re
import execjs
url = 'http://login.shikee.com/getkey?v=97434350dfd69718c42d82249257621d'
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

page_text=requests.get(url=url,headers=headers).text
rsa_n = re.findall(pattern='var rsa_n="(.*?)"',string=page_text)[0]
print(rsa_n)

# 创建节点
node=execjs.get()
# 读取js文件
fp = open('shikelianmeng.js','r',encoding='utf-8')
ctx = node.compile(fp.read())
pwd = '123456'
# 调用函数
funcName = 'getPwd("%s","%s")'%(pwd,rsa_n)
result = ctx.eval(funcName)
print(result)