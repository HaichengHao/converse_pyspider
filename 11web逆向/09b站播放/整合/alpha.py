"""
@File    :alpha.py
@Editor  : 百年
@Date    :2025/4/6 22:13 
"""
import re
import hmac
import hashlib
import random

import requests
import uuid
import time
from blsid import get_blsid

# 创建seeion保存cookie
session = requests.Session()

session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}
resp = session.get(url='https://www.bilibili.com/video/BV165RBYJEGT/')
res = session.cookies.get_dict()
page_source = resp.text
# step1:得到buvid和b_nut
buvid3 = res.get('buvid3')
b_nut = res.get('b_nut')
print(f'buvid3:{buvid3},bnut:{b_nut}')
resp.close()  # 关掉本次链接


# step2:生成_uuid
def gen_uuid():
    uuid_sec = str(uuid.uuid4())
    time_sec = str(int(time.time() * 1000 % 1e5))
    time_sec = time_sec.ljust(5, "0")

    return f"{uuid_sec}{time_sec}".upper() + 'infoc'


# _uuid = gen_uuid()
# 设置_uuid和curent_fnval然后将其加入到session中
session.cookies['_uuid'] = gen_uuid()
session.cookies['CURRENT_FNVAL'] = '4048'

# step3:获取blsid
blsid = get_blsid()
session.cookies['blsid'] = blsid

# step4: 有了这些之后对v2?发起请求来获取sid
obj = re.compile(
        r'''"seek_type":"offset","dash":{"duration":(?P<duration>\d+).*?</script><script>.*?},"aid":(?P<aid>\d+),"bvid":(?P<bvid_>.*?),"cid":(?P<cid>\d+),.*?"userInteractionCount":(?P<viewcount>\d+).*?''',
        re.S)
result = obj.finditer(page_source)
for item in result:
    aid = item.group('aid')
    cid = item.group('cid')
    # print(f"aid:{aid}\ncid:{cid}")
sid_url = 'https://api.bilibili.com/x/player/wbi/v2?' + f'aid={aid}&' + f'cid={cid}'
print(sid_url)
resp1 = session.get(sid_url)
cookiedict = resp1.cookies.get_dict()
# print(cookiedict)
sid = cookiedict['sid']
print(sid)
# session.cookies['sid'] = sid
resp1.close()


# step5:设置biliticket和ticketexpire
def hmac_sha256(key, message):
    """
    使用HMAC-SHA256算法对给定的消息进行加密
    :param key: 密钥
    :param message: 要加密的消息
    :return: 加密后的哈希值
    """
    # 将密钥和消息转换为字节串
    key = key.encode('utf-8')
    message = message.encode('utf-8')

    # 创建HMAC对象，使用SHA256哈希算法
    hmac_obj = hmac.new(key, message, hashlib.sha256)

    # 计算哈希值
    hash_value = hmac_obj.digest()

    # 将哈希值转换为十六进制字符串
    hash_hex = hash_value.hex()

    return hash_hex


o = hmac_sha256("XgwSnGZ1p", f"ts{int(time.time())}")
# url = "https://api.bilibili.com/bapis/bilibili.api.ticket.v1.Ticket/GenWebTicket"
# params = {
#     "key_id": "ec02",
#     "hexsign": o,
#     "context[ts]": f"{int(time.time())}",
#     "csrf": ''
# }
resp = session.post(url="https://api.bilibili.com/bapis/bilibili.api.ticket.v1.Ticket/GenWebTicket",
                    params={
                        "key_id": "ec02",
                        "hexsign": o,
                        "context[ts]": f"{int(time.time())}",
                        "csrf": ''
                    }
                    )
resp2 = resp.json()
ticket = resp2['data'].get('ticket')
created_at = resp2['data'].get('created_at')
ttl = resp2['data'].get('ttl')
bili_ticket_expires = f'{ttl + created_at}'
session.cookies['bili_ticket'] = ticket
session.cookies['bili_ticket_expires'] = bili_ticket_expires
resp.close()
# # step6 :拼接buvid4

resp = session.get(url='https://api.bilibili.com/x/frontend/finger/spi')
resp3 = resp.json()
buvid4 = resp3['data']['b_4']
print(buvid4)
session.cookies['buvid4'] = buvid4
resp.close()
session.cookies['buvid_fp'] = '87bf7390de851df5d0d8346a105787d3'

print(session.cookies.get_dict())

# step7 :获取now
resp = session.get(
    url='https://api.bilibili.com/x/click-interface/click/now'
)
resp4 = resp.json()
now_ = resp4['data'].get('now')
print(now_)
resp.close()

start_ts = int(time.time())
# step8: 对h5发起请求，传入参数
resp = session.post(
    url='https://api.bilibili.com/x/click-interface/click/web/h5',
    data={
        "aid": f'{aid}',
        "cid": f'{cid}',
        "part": "1",
        "lv": "0",
        "ftime": str(start_ts - random.randint(10, 100)),  # 或用now_也是可以的
        "stime": str(start_ts),
        "type": "3",
        "sub_type": "0",
        "refer_url": "",
        "outer": "0",
        "statistics": "%7B%22appId%22%3A100%2C%22platform%22%3A5%2C%22abtest%22%3A%22%22%2C%22version%22%3A%22%22%7D",
        "mobi_app": "web",
        "device": "web",
        "platform": "web",
        "spmid": "333.788.0.0",
        "from_spmid": "333.788.0.0",
        "session": "afc7fe8b01129556602f4e02eac88cd4",
        "csrf": ""
    }

)
# print(resp.text)
resp.close()

# step9:心跳机制第一次
resp = session.post(
    url='https://api.bilibili.com/x/click-interface/web/heartbeat',
    data={
        "start_ts": str(start_ts),
        "aid": f"{aid}",
        "cid": f"{cid}",
        "type": "3",
        "sub_type": "0",
        "dt": "2",
        "play_type": "2",
        "realtime": "3",
        "played_time": "3",
        "real_played_time": "0",
        "refer_url": "",
        "quality": "0",
        "video_duration": "7520",
        "last_play_progress_time": "3",
        "max_play_progress_time": "3",
        "outer": "0",
        "statistics": "%7B%22appId%22%3A100%2C%22platform%22%3A5%2C%22abtest%22%3A%22%22%2C%22version%22%3A%22%22%7D",
        "mobi_app": "web",
        "device": "web",
        "platform": "web",
        "spmid": "333.788.0.0",
        "from_spmid": "333.788.0.0",
        "session": "afc7fe8b01129556602f4e02eac88cd4",
        "extra": "%7B%22player_version%22%3A%224.9.29%22%7D",
        "csrf": ""
    }
)
print(resp.text)
resp.close()