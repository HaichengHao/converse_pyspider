"""
@File    :03UA测试.py
@Editor  : 百年
@Date    :2025/6/15 16:47 
"""
import requests

url = 'http://127.0.0.1:5000/getinfo'

resp = requests.get(url)

print(resp.text)