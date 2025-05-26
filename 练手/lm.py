# @Author    : 百年
# @FileName  :lm.py
# @DateTime  :2025/5/20 20:51
import requests
from lxml import etree
import random
fp = open('lj.txt','r')
url='https://www.qqxiuzi.cn/zh/luanma/'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
}
session = requests.session()
resp = session.get(url=url,headers=headers)
resp.encoding = resp.apparent_encoding
page_source = resp.text
# print(page_source)
tree =etree.HTML(page_source)

token = tree.xpath('//input[@name="token"]/@value')[0]
options_lst  = tree.xpath('//select[@name="code"]/optgroup/option/text()')
print(token)
print(options_lst)
sec_url = 'https://www.qqxiuzi.cn/zh/luanma/show.php'
# tx = input('请输入文本>>>')
tx = fp.readlines()
# print(tx)
selcode = random.choice(options_lst[2:])
print(selcode)
data={
    'text':tx,
    'code':selcode,
    'token':token
}
res = session.post(url=sec_url,data=data)
print(res.text)

fp.close()