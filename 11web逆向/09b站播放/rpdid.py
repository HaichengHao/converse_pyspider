"""
@File    :rpdid.py
@Editor  : 百年
@Date    :2025/4/4 20:45 
"""
import requests

url = '''
https://api.bilibili.com/x/click-interface/click/web/h5?w_aid=114277000151219&w_part=1&w_ftime=1743770237&w_stime=1743770238&w_type=3&web_location=1315873&w_rid=8c55f2e0fd5abe1cf66143458436a78b&wts=1743770237
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    ,
    'Cookie': 'buvid3=3BF82F58-3030-1526-A88B-DE2D0570813D30652infoc; b_nut=1743770230; b_lsid=FC127148_19600CE1D35; _uuid=692AB7C10-F19C-10849-F5DA-1107C62AB747230080infoc; CURRENT_FNVAL=4048; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDQwMjk0MzEsImlhdCI6MTc0Mzc3MDE3MSwicGx0IjotMX0.HuUhwf2uKsH_2QkBHcTN6hOKNzELKWcMCy_eyC8bVfM; bili_ticket_expires=1744029371; sid=fdtev7jm; buvid4=84CDC8D3-30D1-D056-FC6E-3C9648044B8516989-024111401-BcE//4bW+MuvI9QMQWCCVg%3D%3D; buvid_fp=372644e63165b811f1813e71dfbe9cde'
}

response = requests.post(url=url, headers=headers)

res = response.cookies.get_dict()
print(res)
