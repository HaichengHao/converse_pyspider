"""
@File    :tunnelproxies.py
@Editor  : 百年
@Date    :2025/4/8 14:24 
"""
import requests
# url = 'https://share.proxy.qg.net/get?key=073A3D69&num=50&area=210100,210200,210300,210400,210500,210600,210700,210800,210900,211000,211100,211200,211300,211400&isp=0&format=txt&seq=\r\n&distinct=false'
# # url = 'https://share.proxy.qg.net/get?key=073A3D69&num=50&area=210100,210200,210300,210400,210500,210600,210700,210800,210900,211000,211100,211200,211300,211400&isp=0&format=json&distinct=false'
# resp = requests.get(url=url)
# c = resp.json()
# print(c)


def tunnel_proxies():
    # url = url = 'https://share.proxy.qg.net/get?key=073A3D69&num=50&area=210100,210200,210300,210400,210500,210600,210700,210800,210900,211000,211100,211200,211300,211400&isp=0&format=json&distinct=false'
    # url = 'https://share.proxy.qg.net/get?key=073A3D69&num=50&area=210100,210200,210300,210400,210500,210600,210700,210800,210900,211000,211100,211200,211300,211400&isp=0&format=txt&seq=\r\n&distinct=false'
    # url = 'https://share.proxy.qg.net/get?key=073A3D69&num=50&area=210100,210200,210300,210400,210500,210600,210700,210800,210900,211000,211100,211200,211300,211400&isp=0&format=json&distinct=false'
    # url = 'https://share.proxy.qg.net/get?key=073A3D69&num=50&area=210100,210200,210300,210400,210500,210600,210700,210800,210900,211000,211100,211200,211300,211400&isp=0&format=txt&seq=,&distinct=false'
    url = 'https://share.proxy.qg.net/get?key=073A3D69&num=1&area=210100,210200,210300,210400,210500,210600,210700,210800,210900,211000,211100,211200,211300,211400&isp=0&format=txt&seq=,&distinct=true'
    resp = requests.get(url=url)
    c = resp.text
    # print(c)
    # print(type(c))
    return c

if __name__ == '__main__':
    ips = tunnel_proxies()
    # ip = ips.split(',')
    # for item in ip:
    #     item = 'http://{}'
    print(ips)
