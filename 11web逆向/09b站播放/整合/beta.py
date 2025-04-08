"""
@File    :beta.py
@Editor  : 百年
@Date    :2025/4/7 22:48 
"""
import requests
import re
import hmac
import hashlib
import random
import uuid
import time
from blsid import get_blsid


class PcAnonymous(object):
    """匿名pc播放"""

    def __init__(self, aid, bvid, cid, view_count, duration, proxies):  # 初始化方法
        self.aid = aid
        self.bvid = bvid
        self.cid = cid
        self.view_count = view_count
        self.duration = duration
        self.start_ts = None,  # 设置时间戳为None
        self.session = requests.Session()
        self.session.proxies = proxies
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
        }

    # tips:得到buvid和b_nut
    def get_buvid3(self):
        url = f'https://www.bilibili.com/video/{self.bvid}/'
        res = self.session.get(
            url=url
        )
        res.close()

    # tips:生成_uuid,blsid,CURRTENT_FINAL
    def gen_uuid(self):
        uuid_sec = str(uuid.uuid4())
        time_sec = str(int(time.time() * 1000 % 1e5))
        time_sec = time_sec.ljust(5, "0")
        self._uuid = f"{uuid_sec}{time_sec}".upper() + 'infoc'
        self.session.cookies['_uuid'] = self._uuid
        self.session.cookies['CURRENT_FNVAL'] = '4048'
        self.blsid = get_blsid()
        self.session.cookies['blsid'] = self.blsid

    # tips:通过传入的aid和cid得到sid
    def gen_sid(self):
        res = self.session.get(
            url='https://api.bilibili.com/x/player/wbi/v2?',
            data={
                'aid': self.aid,
                'cid': self.cid,
            }
        )
        res.close()

    # # tips:定义加密方法，方便下面的tickets生成
    # def hmac_sha256(key, message):
    #     """
    #     使用HMAC-SHA256算法对给定的消息进行加密
    #     :param key: 密钥
    #     :param message: 要加密的消息
    #     :return: 加密后的哈希值
    #     """
    #     # 将密钥和消息转换为字节串
    #     key = key.encode('utf-8')
    #     message = message.encode('utf-8')
    #
    #     # 创建HMAC对象，使用SHA256哈希算法
    #     hmac_obj = hmac.new(key, message, hashlib.sha256)
    #
    #     # 计算哈希值
    #     hash_value = hmac_obj.digest()
    #
    #     # 将哈希值转换为十六进制字符串
    #     hash_hex = hash_value.hex()
    #
    #     return hash_hex

    # tips:设置biliticket和ticketexpires
    def gen_ticket(self):
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
        res = self.session.post(url="https://api.bilibili.com/bapis/bilibili.api.ticket.v1.Ticket/GenWebTicket",
                                params={
                                    "key_id": "ec02",
                                    "hexsign": o,
                                    "context[ts]": f"{int(time.time())}",
                                    "csrf": ''
                                }
                                )
        resp2 = res.json()
        ticket = resp2['data'].get('ticket')
        created_at = resp2['data'].get('created_at')
        ttl = resp2['data'].get('ttl')
        bili_ticket_expires = f'{ttl + created_at}'
        self.session.cookies['bili_ticket'] = ticket
        self.session.cookies['bili_ticket_expires'] = bili_ticket_expires
        res.close()

    # tips:设置buvid4
    def gen_buvid4(self):
        res = self.session.get(url='https://api.bilibili.com/x/frontend/finger/spi')
        resp3 = res.json()
        buvid4 = resp3['data']['b_4']
        # print(buvid4)
        self.session.cookies['buvid4'] = buvid4
        res.close()
        self.session.cookies['buvid_fp'] = '87bf7390de851df5d0d8346a105787d3'

    # tips:设置h5请求
    def click_h5(self):
        self.start_ts = int(time.time())
        res = self.session.post(
            url='https://api.bilibili.com/x/click-interface/click/web/h5',
            data={
                "aid": f'{self.aid}',
                "cid": f'{self.cid}',
                "part": "1",
                "lv": "0",
                "ftime": str(self.start_ts - random.randint(10, 100)),  # 或用now_也是可以的
                "stime": str(self.start_ts),
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
        res.close()

    # tips:第一次心跳开始
    def heart_beat(self):
        res = self.session.post(
            url='https://api.bilibili.com/x/click-interface/web/heartbeat',
            data={
                "start_ts": str(self.start_ts),
                "aid": f"{self.aid}",
                "cid": f"{self.cid}",
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
        print(res.text)
        res.close()

    def run(self):
        try:
            self.get_buvid3()
            self.gen_uuid()
            self.gen_sid()
            self.gen_ticket()
            self.gen_buvid4()
            self.click_h5()
            self.heart_beat()
            print('成功!')
        except BaseException as e:
            print('请求异常', e)


# 创建获取视频信息的函数
def getvv(bvid):
    url = 'https://www.bilibili.com/video/' + bvid + '/'
    session = requests.Session()
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'

    }
    res = session.get(url=url)
    page_source = res.text
    obj = re.compile(
        r'''<script>.*?"duration":(?P<duration>\d+).*?</script><script>.*?},"aid":(?P<aid>\d+),"bvid":(?P<bvid_>.*?),"cid":(?P<cid>\d+),.*?"userInteractionCount":(?P<viewcount>\d+).*?''',
        re.S)
    result = obj.finditer(page_source)
    for item in result:
        duration = item.group('duration')
        aid = item.group('aid')
        bvid_ = item.group('bvid_')
        cid = item.group('cid')
        viewcount = item.group('viewcount')
        return aid, bvid_, cid, viewcount, duration



def handler():
    # 先要让用户输入BVID
    bvid = input('输入视频的bvid')
    # 获取视频信息aid\cid
    aid, bvid_, cid, viewcount, duration = getvv(bvid)
    # print(aid, bvid_, cid, viewcount, duration )
    print(f'aid:{aid}, bvid:{bvid_},cid: {cid}, 观看人数:{viewcount}, 时长{duration}')
    # 播放
    # tips:创建类对象，传入参数，由于这里没有用到隧道代理故先不传入
    pc = PcAnonymous(aid, bvid_, cid, viewcount, duration,None)
    pc.run() #tips:调用实例方法，运行代码
if __name__ == '__main__':
    handler()

# https://www.bilibili.com/video/BV1mRRvYsEvD/?spm_id_from=333.788.recommend_more_video.4
# https://www.bilibili.com/video/BV1xfRvYQEtb/?spm_id_from=333.788.recommend_more_video.0