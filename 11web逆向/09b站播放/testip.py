"""
@File    :testip.py
@Editor  : 百年
@Date    :2025/4/8 14:51 
"""
"""
@File    :tunnelproxies.py
@Editor  : 百年
@Date    :2025/4/8 14:24 
"""
import requests



def tunnel_proxies():
    url = 'https://share.proxy.qg.net/get?key=073A3D69&num=1&area=&isp=0&format=txt&seq=,&distinct=true'
    resp = requests.get(url=url)
    c = 'http://'+resp.text
    # print('http://'+c)
    return c
if __name__ == '__main__':
    c = tunnel_proxies()
    print(c)