"""
@File    :补充之处理响应.py
@Editor  : 百年
@Date    :2025/6/5 22:51 
"""
import subprocess

'''
有时候会遇到response.json()不好用
而且json.loads(response.text())也不好使的情况
'''

import execjs

from functools import partial
from subprocess import Popen
subprocess.Popen = partial(subprocess.Popen,encoding='utf-8')
response = '{"data":[{"id":2614079478,"url":"http://m701.music.126.net/20250605232222/11dbdc8a88b6e571c4722e3b1694d831/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/45007773612/71c3/7a90/4714/8991783b8e21dedc7a30d9190cc5d7a1.m4a?vuutv=U9UNyOfk1Ikzrcuj2an+8pgDywVVL74wbfzwerPRWwZqWYeRzp8tsT78lKMlqMcUyMvHxHxYy+nfc2XkvBO4JpsHNiIwvc8d/CCtqVOEJOkF7JjLnDYI1lfsRK1eet/28+0CbL64MtnExoQ2LYk61g==","br":256011,"size":7316611,"md5":"8991783b8e21dedc7a30d9190cc5d7a1","code":200,"expi":1200,"type":"m4a","gain":0.0,"peak":1.0606,"closedGain":0.0,"closedPeak":0.0,"fee":8,"uf":null,"payed":0,"flag":4,"canExtend":false,"freeTrialInfo":null,"level":"exhigh","encodeType":"aac","channelLayout":null,"freeTrialPrivilege":{"resConsumable":false,"userConsumable":false,"listenType":null,"cannotListenReason":null,"playReason":null,"freeLimitTagType":null},"freeTimeTrialPrivilege":{"resConsumable":false,"userConsumable":false,"type":0,"remainTime":0},"urlSource":0,"rightSource":0,"podcastCtrp":null,"effectTypes":null,"time":227234,"message":null,"levelConfuse":null,"musicId":"11296934978","accompany":null,"sr":48000,"auEff":null}],"code":200}'
print(type(response))


js_code = execjs.compile(r"function fn(s){return JSON.parse(s+'')}")
dic = js_code.call("fn",response)

print(dic,type(dic))


# 可以看到是从字符串类型转换为字典类型了
'''
<class 'str'>
{'data': [{'id': 2614079478, 'url': 'http://m701.music.126.net/20250605232222/11dbdc8a88b6e571c4722e3b1694d831/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/45007773612/71c3/7a90/4714/8991783b8e21dedc7a30d9190cc5d7a1.m4a?vuutv=U9UNyOfk1Ikzrcuj2an+8pgDywVVL74wbfzwerPRWwZqWYeRzp8tsT78lKMlqMcUyMvHxHxYy+nfc2XkvBO4JpsHNiIwvc8d/CCtqVOEJOkF7JjLnDYI1lfsRK1eet/28+0CbL64MtnExoQ2LYk61g==', 'br': 256011, 'size': 7316611, 'md5': '8991783b8e21dedc7a30d9190cc5d7a1', 'code': 200, 'expi': 1200, 'type': 'm4a', 'gain': 0, 'peak': 1.0606, 'closedGain': 0, 'closedPeak': 0, 'fee': 8, 'uf': None, 'payed': 0, 'flag': 4, 'canExtend': False, 'freeTrialInfo': None, 'level': 'exhigh', 'encodeType': 'aac', 'channelLayout': None, 'freeTrialPrivilege': {'resConsumable': False, 'userConsumable': False, 'listenType': None, 'cannotListenReason': None, 'playReason': None, 'freeLimitTagType': None}, 'freeTimeTrialPrivilege': {'resConsumable': False, 'userConsumable': False, 'type': 0, 'remainTime': 0}, 'urlSource': 0, 'rightSource': 0, 'podcastCtrp': None, 'effectTypes': None, 'time': 227234, 'message': None, 'levelConfuse': None, 'musicId': '11296934978', 'accompany': None, 'sr': 48000, 'auEff': None}], 'code': 200} <class 'dict'>

Process finished with exit code 0
'''