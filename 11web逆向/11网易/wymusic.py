"""
@File    :wymusic.py
@Editor  : 百年
@Date    :2025/5/27 12:11
"""
'''
https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=77ddf93cdc2cda59db3e088d3c2e38b6

                    /api/song/enhance/player/url/v1
encodeType: "aac"  音乐解码方式
ids: "[307606]" 音乐id
level: "exhigh"  音质

params    经过两次aes加密得到
encSecKey 经过一次rsa加密得到


npm i rypto-js
'''
import requests
from functools import partial
import subprocess
subprocess.Popen = partial(subprocess.Popen,encoding='utf-8')
import execjs
import json
with open('./扣代码.js','r',encoding='utf-8') as f:
    ctx = execjs.compile(f.read())
musicid = input('请输入歌曲id')
data={
    "encodeType": "aac",
    "ids":f"[{musicid}]",
    "level": "exhigh"
}

param1=json.dumps(data) #将其处理成json字符串,序列化->json字符串化
print(param1)
# funcname = f'myrealfunc({param1})'
res = ctx.call('myrealfunc',param1)
print(res)

realdata={
    'params':res['encText'],
    'encSecKey':res['encSecKey']
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
}
url = f'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=77ddf93cdc2cda59db3e088d3c2e38b6'
response = requests.post(url=url,headers=headers,data=realdata)
response.encoding = response.apparent_encoding
pagesource = response.text
print(pagesource)


dic_page_source = json.loads(pagesource)
print(dic_page_source)
print(type(dic_page_source))
music_url = dic_page_source['data'][0]['url']
print(music_url)
bincontent = requests.get(url=music_url,headers=headers).content
with open('./blue.mp3','wb') as mf:
    mf.write(bincontent)