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
url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers={
    'User-Agent':useragent

}
word = input('输入单词>>')
data = {
    'i':word,
    "from":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",

}
# 创建节点
node = execjs.get()

# 读取js文件创建上下文对象
with open('youdao.js','r',encoding='utf-8') as fp:
    ctx = node.compile(fp.read()) #important:调用节点对js文件进行预编译
e='puppy' #传入要翻译的单词
pytime = time.time()
i = int(pytime*1000)
print(i)
funcname = f'getSign("{e}","{i}")'
print(funcname)
result = ctx.eval(funcname)
print(result)
