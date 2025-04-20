"""
@File    :01尝试请求.py
@Editor  : 百年
@Date    :2025/4/19 16:50 
"""
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

url = 'https://player-api.yangshipin.cn/v1/player/get_video_info'

response = requests.post(url=url,headers=headers)
res_json = response.json()
print(res_json)
