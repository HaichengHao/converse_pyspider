"""
@File    :sec_get.py
@Editor  : 百年
@Date    :2025/4/13 15:01 
"""
import time
from urllib.parse import urljoin

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from lxml import etree

service = Service('../chromedriver.exe')
bro1 = Chrome(service=service)

url = 'https://www.iikx.com/sci/list.html?classid=18&orderby=IF2024&ph=1&jcr21=%E4%B8%B4%E5%BA%8A%E7%A5%9E%E7%BB%8F%E7%97%85%E5%AD%A6'
bro1.get(url=url)
time.sleep(2)
page_ = bro1.page_source
tree = etree.HTML(page_)
# 创建一个用于存储得到的所有页面源码的列表
all_page_lst = [page_]
# 获取到总共有多少页

page_number = tree.xpath('//ul[@class="el-pager"]/li[last()]/text()')
page_num = int(page_number[0])
print(page_num)

# tips:发现页面是ajax请求，没办法直接遍历网页，所以这里直接定位到下一页按钮来进行访问
for i in range(page_num + 1):  # tips:因为最后一页也要获取到，所以+1
    # tips:定位到下一页按钮
    nxt_btn = bro1.find_element(By.XPATH, '//button[@class="btn-next"]')
    #  tips:点击下一页按钮
    nxt_btn.click()
    # 然后停留几秒让网页加载
    time.sleep(2)
    all_page_lst.append(bro1.page_source)

for page_text in all_page_lst:
    tree = etree.HTML(page_text)
    a_lst = tree.xpath('//table[@class="sci-table-info"]/tbody/tr/td[1][position()]/a/@href')
    for a in a_lst:
        full_url = 'https://www.iikx.com/' + a
        print('\''+full_url+'\'')

# def get_every_url(url):
#     bro1.get(url=url)
#     time.sleep(3)
#     page_source = bro1.page_source
#     print(page_source)
#     tree = etree.HTML(page_source)
#     a_lst = tree.xpath('//table[@class="sci-table-info"]/tbody/tr/td[1][position()]/a/@href')
#     for a in a_lst:
#         # print(a)
#         full_url = 'https://www.iikx.com/'+a
#         print(full_url)
#     next_btn = bro1.find_element(By.XPATH,'//button[@class="btn-next"]')
#     next_btn.click()
#     time.sleep(2)
