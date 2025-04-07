"""
@File    :alpha.py
@Editor  : 百年
@Date    :2025/4/6 22:13 
"""
import requests
import uuid
import time

#创建seeion保存cookie
session = requests.Session()

session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}
resp = session.get(url='https://www.bilibili.com/video/BV165RBYJEGT/')
res = session.cookies.get_dict()
buvid3 = res.get('buvid3')
b_nut = res.get('b_nut')
print(f'buvid3:{buvid3},bnut:{b_nut}')
resp.close() #关掉本次链接

# 生成uuid
def gen_uuid():
    uuid_sec = str(uuid.uuid4())
    time_sec = str(int(time.time()*1000 % 1e5))
    time_sec = time_sec.ljust(5,"0")

    return f"{uuid_sec}{time_sec}".upper() + 'infoc'
# _uuid = gen_uuid()

session.cookies['_uuid'] = gen_uuid()
session.cookies['CURRENT_FNVAL'] = '4048'
