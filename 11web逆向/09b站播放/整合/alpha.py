"""
@File    :alpha.py
@Editor  : 百年
@Date    :2025/4/6 22:13 
"""
import re

import requests
import uuid
import time
from blsid import get_blsid
#创建seeion保存cookie
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
resp.close() #关掉本次链接

# step2:生成uuid
def gen_uuid():
    uuid_sec = str(uuid.uuid4())
    time_sec = str(int(time.time()*1000 % 1e5))
    time_sec = time_sec.ljust(5,"0")

    return f"{uuid_sec}{time_sec}".upper() + 'infoc'
# _uuid = gen_uuid()
# 设置_uuid和curent_fnval然后将其加入到session中
session.cookies['_uuid'] = gen_uuid()
session.cookies['CURRENT_FNVAL'] = '4048'

# 获取blsid
blsid = get_blsid()
session.cookies['blsid'] = blsid

#step3: 有了这些之后对v2?发起请求来获取sid

obj = re.compile(r'</script><script>.*?},"aid":(?P<aid>\d+),"bvid":.*?,"cid":(?P<cid>\d+),',re.S)
result = obj.finditer(page_source)
for item in result:
    aid = item.group('aid')
    cid = item.group('cid')
    # print(f"aid:{aid}\ncid:{cid}")
sid_url = 'https://api.bilibili.com/x/player/wbi/v2?'+f'aid={aid}&'+f'cid={cid}'
print(sid_url)
resp1 = session.get(sid_url)
cookiedict = resp1.cookies.get_dict()
# print(cookiedict)
sid = cookiedict['sid']
# print(sid)
session.cookies['sid'] = sid
resp1.close()
# step4:设置biliticket和