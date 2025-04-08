"""
@File    :bvid.py
@Editor  : 百年
@Date    :2025/4/7 13:20 
"""
import requests
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

