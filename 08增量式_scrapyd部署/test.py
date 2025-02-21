"""
@File    :test.py
@Editor  : 百年
@Date    :2025/2/21 12:58 
"""
# abst: 使用requests模块控制scrapy项目,前提是你已经scrapyd-deploy 部署名 -p 项目名
import requests

#important:我将会新写一份，这份太简陋
# 启动爬虫
url = 'http://localhost:6800/schedule.json'
data = {
	'project':'zlsDEMO2',
	'spider': 'jianli',
}
resp = requests.post(url, data=data)

# 停止爬虫
# url = 'http://localhost:6800/cancel.json'
# data = {
# 	'project': zlsDEMO2,
# 	'job': 启动爬虫时返回的jobid,
# }
resp = requests.post(url, data=data)
print(resp.json())