"""
@File    :14新豆瓣.py
@Editor  : 百年
@Date    :2025/4/15 22:40 
"""
import requests

url = 'https://movie.douban.com/top250?start='
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
response = requests.get(url=url,headers=headers)
response.encoding = response.apparent_encoding
page_source = response.text
print(page_source)
