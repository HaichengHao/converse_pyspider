"""
@File    :scrape.py
@Editor  : 百年
@Date    :2025/5/16 16:12 
"""
import requests
import json


headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept":"application/json, text/plain, */*",
    "Referer":"https://spa15.scrape.center/page/1",
}

params={
    "limit":10,
    "offset":0,
    "token":"NTBhYmNlOTk0YmYwNGU1ODMwMzhjMGQ3MzZhNGY0NjQxYTU1YmNjOCwxNzQ3MzgyODMy"
}

url="https://spa15.scrape.center/api/movie/?"

response = requests.get(url=url,headers=headers,params=params)
print(response.text)
if response.status_code == 200:
    print("成功")
    data = response.json()
    print(data)