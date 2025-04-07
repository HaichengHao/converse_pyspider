"""
@File    :ticket.py
@Editor  : 百年
@Date    :2025/4/6 15:18 
"""
import requests
import time
ts  = int(time.time()*1000)
# url = '''
# https://api.bilibili.com/bapis/bilibili.api.ticket.v1.Ticket/GenWebTicket?key_id=ec02&hexsign=e8c179543cd0784b6edbdc0e8a85a4c6e7d25cd62c03e314e6aabf95dec3be0a&context[ts]=1743921735&csrf=
# '''
url = '''
https://api.bilibili.com/bapis/bilibili.api.ticket.v1.Ticket/GenWebTicket
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}
data={
    'key_id':'ec02',
    'hexsign':'7011726bb222c87c95a42d08fc02cc798b9bddfc57d8f1db656d482f5be6a6c3',
    'context[ts]':f'{ts}'
}
response = requests.post(url=url,headers=headers,data=data)
resp = response.json()
print(resp)
ticket = resp['data'].get('ticket')
created_at = resp['data'].get('created_at')
ttl = resp['data'].get('ttl')
print(f'Ticket: {ticket}\n,created_at:{created_at}\n,ttl:{ttl}')
# print(type(ttl),type(created_at))
bili_ticket_expires = created_at+ttl
print(f'ticket_expires: {bili_ticket_expires}')