"""
@File    :00用了charles.py
@Editor  : 百年
@Date    :2025/5/22 18:35 
"""

'''
如果用了charles来跑代码的时候可能会出问题  
所以可以利用window设置中的代理设置加上http=127.0.0.1:8888;https=127.0.0.1:8888这里的8888是charles的端口号'''
import requests

url = 'https://www.cythb.com/page_2.html'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
}

proxy={
    'https':'http://127.0.0.1:8888'
}
resp = requests.get(url=url,headers=headers,verify=False,proxies=proxy)

resp.encoding = resp.apparent_encoding

page_source = resp.text
print(page_source)

# 或者可以上科技，开全局代理,可以直接干蓝鸟，脸盆网
# 查尔斯和科技有摩擦，要有所取舍