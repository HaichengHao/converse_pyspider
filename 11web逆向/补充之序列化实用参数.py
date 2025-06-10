"""
@File    :补充之序列化实用参数.py
@Editor  : 百年
@Date    :2025/6/6 9:47 
"""
import json

response = '{"data":[{"id":2614079478,"url":"http://m701.music.126.net/20250605232222/11dbdc8a88b6e571c4722e3b1694d831/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/45007773612/71c3/7a90/4714/8991783b8e21dedc7a30d9190cc5d7a1.m4a?vuutv=U9UNyOfk1Ikzrcuj2an+8pgDywVVL74wbfzwerPRWwZqWYeRzp8tsT78lKMlqMcUyMvHxHxYy+nfc2XkvBO4JpsHNiIwvc8d/CCtqVOEJOkF7JjLnDYI1lfsRK1eet/28+0CbL64MtnExoQ2LYk61g==","br":256011,"size":7316611,"md5":"8991783b8e21dedc7a30d9190cc5d7a1","code":200,"expi":1200,"type":"m4a","gain":0.0,"peak":1.0606,"closedGain":0.0,"closedPeak":0.0,"fee":8,"uf":null,"payed":0,"flag":4,"canExtend":false,"freeTrialInfo":null,"level":"exhigh","encodeType":"aac","channelLayout":null,"freeTrialPrivilege":{"resConsumable":false,"userConsumable":false,"listenType":null,"cannotListenReason":null,"playReason":null,"freeLimitTagType":null},"freeTimeTrialPrivilege":{"resConsumable":false,"userConsumable":false,"type":0,"remainTime":0},"urlSource":0,"rightSource":0,"podcastCtrp":null,"effectTypes":null,"time":227234,"message":null,"levelConfuse":null,"musicId":"11296934978","accompany":null,"sr":48000,"auEff":null}],"code":200}'

# 如果想要去掉json序列化时候带的: ,和, 注意这里是冒号空格和逗号空格的意思,想去掉这些空格,但是用replace的话有点极端
# 那么可以使用json序列化时候自带的一个参数
res = json.dumps(response,separators=(":",","))
print(res)