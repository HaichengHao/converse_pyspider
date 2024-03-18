from lxml import etree
import requests
import random
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',

}
proxies_pool=[
    {'http': '42.63.65.37:80'},
    {'http': '42.63.65.13:80'},
    {'http': '42.63.65.15:80'},
    {'http': '42.63.65.7:80'},
    {'http': '42.63.65.8:80'},
    {'http': '42.63.65.9:80'},
    {'http': '39.173.106.248:80'},
    {'http': '39.173.106.249:80'},
    {'http': '39.173.106.250:80'},
    {'http': '39.173.106.251:80'},
    {'http': '39.173.106.230:80'},
    {'http': '39.173.106.235:80'},
    {'http': '39.173.106.239:80'},
    {'http': '39.173.106.240:80'},
    {'http': '39.173.106.241:80'},
    {'http': '39.173.106.243:80'},
    {'http': '39.173.106.244:80'},
    {'http': '39.173.106.245:80'},
    {'http': '39.173.102.114:80'},
    {'http': '39.173.102.123:80'},
    {'http': '39.173.106.133:80'},
    {'http': '159.226.227.117:80'},
    {'http': '159.226.227.122:80'},
    {'http': '159.226.227.120:80'},
    {'http': '159.226.227.118:80'},
    {'http': '159.226.227.115:80'},
    {'http': '159.226.227.113:80'},
    {'http': '159.226.227.112:80'},
    {'http': '159.226.227.111:80'},
    {'http': '159.226.227.110:80'},
    {'http': '159.226.227.108:80'},
    {'http': '159.226.227.107:80'},
    {'http': '159.226.227.97:80'},
    {'http': '159.226.227.92:80'},
    {'http': '159.226.227.98:80'},
    {'http': '159.226.227.96:80'},
    {'http': '159.226.227.95:80'},
    {'http': '159.226.227.86:80'},
    {'http': '159.226.227.78:80'},
    {'http': '140.249.88.250:80'},
]
proxies=random.choice(proxies_pool)
url='http://www.ip3366.net/'
response=requests.get(url=url,headers=headers,proxies=proxies)
response.encoding=response.apparent_encoding
content=response.text
print(content)
tree=etree.HTML(content)
ips=tree.xpath('//td[1]/text()')
ports=tree.xpath('//td[2]/text()')
print(ips)
print(ports)
my_ip=[]
my_port=[]
for i in range(0,len(ips)):
    new_ips=ips[i]
    new_ports=ports[i]
    my_ip.append(new_ips)
    my_port.append(new_ports)
print(my_ip,my_port)
#
# my_proxy=[]
# for x,y in zip(my_ip,my_port):
#     prox_sock='{\''+'http\''+':'+'\''+x+':'+y+'\''+'}'
#     my_proxy.append(prox_sock)
#
# print(my_proxy)
# for prox in my_proxy:
#     print(prox+',')