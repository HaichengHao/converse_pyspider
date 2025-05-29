"""
@File    :02urlencode.py
@Editor  : 百年
@Date    :2025/5/29 15:21 
"""
'''
在访问url的时候可能会遇到奇奇怪怪的url，浏览器上明明是能看到中文的 
但是一复制出来,就成了好多%xxx%xxx这种 ，但是这种并非是加密  
我们在访问一个url的时候,浏览器会自动的进行urlencode操作,
会对我们请求的url进行编码,这种编码的规则成为百分号编码  
是专门为url准备的一套编码规则  
一个完整的url组成  
协议://域名:端口(一般是被隐藏的http默认80,https默认443)/虚拟路径/.../文件?参数1=参数值&参数2=参数值#(锚点,定位到页面的某个位置)
锚点的实现<a href='#haha'></a>
<a name='haha'></a>
scheme(协议)://host:port/dir/file?p1=v1&v2#anchor
http://www.baidu.com/tieba/index.html?name=hero&age=20
参数key=value
服务器可以通过key访问value

此时,如果参数中出现一些特殊的符号,比如‘=’想给服务器传递a=b=c的操作 
就会让整个url产生歧义 
'''

from urllib.parse import urlencode

url = 'http://www.baidu.com/s?'

params={
    'wd':'爱情'
}

p = urlencode(params)
print(p)

final_url = url+p
print(final_url)

'''
了解即可,因为requests直接就给我们处理好了'''

import requests
r = requests.get(url=url,params=params)
print(r.request.url)

# http://www.baidu.com/s?wd=%E7%88%B1%E6%83%85