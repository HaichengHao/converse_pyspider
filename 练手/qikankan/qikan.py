"""
@File    :qikan.py
@Editor  : 百年
@Date    :2025/4/13 14:35 
"""
from urllib.parse import urljoin
import csv
import requests
from lxml import etree
# fp = open('./full_url.csv','a+',encoding='utf-8',newline='')
# writer = csv.writer(fp)
# if fp.tell() == 0:
#     writer.writerow(['所有类别的链接',])
url = 'https://www.iikx.com/sci/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
response.encoding = response.apparent_encoding
page_source = response.text
tree = etree.HTML(page_source)
a_lst = tree.xpath('//div[@class="tab_content"]/a/@href')
full_lst = []
for a_ in a_lst:
    # print(a_)
    #一级页面中二级页面链接获取成功之后，接着来获取二级页面的数据链接，需要逆向
    sec_a = urljoin(url,a_)

    print(sec_a)
    # writer.writerow([sec_a,])
    full_lst.append(sec_a)
# print(page_source)
print(full_lst,len(full_lst))
# writer.writerow(full_lst)
# fp.close()