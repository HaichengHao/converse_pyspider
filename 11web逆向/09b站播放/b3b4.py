"""
@File    :b3b4.py
@Editor  : 百年
@Date    :2025/4/6 17:57 
"""
import requests

url = 'https://api.bilibili.com/x/frontend/finger/spi'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
resp = response.json()
b3=resp['data']['b_3']
b4=resp['data']['b_4']
print(resp)
print(f'b3: {b3}\nb4: {b4}')