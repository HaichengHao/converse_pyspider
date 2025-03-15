"""
@File    :demo1.py
@Editor  : 百年
@Date    :2025/3/15 21:13 
"""

# ABST:用requests和splash做对接
import requests

response = requests.get(url='http://192.168.150.133:8050/render.html',
                        params={
                            "url": "https://www.endata.com.cn/BoxOffice/BO/Year/index.html",
                            "wait": 3
                        })
print(response.text)
