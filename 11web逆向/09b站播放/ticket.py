"""
@File    :ticket.py
@Editor  : 百年
@Date    :2025/4/6 15:18 
"""
import requests
import time
ts  = int(time.time()*1000)
url = '''
https://api.bilibili.com/bapis/bilibili.api.ticket.v1.Ticket/GenWebTicket?key_id=ec02&hexsign=e8c179543cd0784b6edbdc0e8a85a4c6e7d25cd62c03e314e6aabf95dec3be0a&context[ts]=1743921735&csrf=
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}
data={
    'key_id':'ec02',
    # 'hexsign':'',
    'context[ts]':f'{ts}'
}
response = requests.post(url=url,headers=headers,data=data)
resp = response.json()
print(resp)