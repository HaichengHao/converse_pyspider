"""
@File    :获取加密base64串.py
@Editor  : 百年
@Date    :2025/5/31 22:23 
"""
import requests

# i = int(input('请输入要获取的页数>>>'))
url=f'https://ctbpsp.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/24?type__1017='
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
}

resp = requests.get(url=url,headers=headers)
b64s = resp.text
print(b64s)