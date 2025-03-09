"""
@File    :00新代理爬取.py
@Editor  : 百年
@Date    :2024/12/22 18:40 
"""
import requests
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from lxml import etree
# 想毙掉图形界面就给注释解开
from selenium.webdriver.chrome.options import Options
# opts = Options()
# opts.add_argument('--headless')
# opts.add_argument('--disable-gpu')
# 创建浏览器对象
service = Service('E:/converse_spider/converse_pyspider/06scrapy/chromedriver.exe')
browser1 = Chrome(service=service)

browser1.get('https://www.89ip.cn/index_')
time.sleep(2)
page_ = browser1.page_source
# print(page_)

# IMPORTANT:先验证第一页有没有拿到
# 创建一个用于存储得到所有页面源码的列表
all_page_lst=[page_]

# all_page_lst=[]
# 实现自定义爬取
page_number = int(input('请输入要爬取到的页数>>'))
for i in range(page_number):
    # 定位到下一页按钮
    nxt_btn = browser1.find_element(By.XPATH,"//div[@class='layui-box layui-laypage layui-laypage-default']/a[last()]")
#     点击下一页
    nxt_btn.click()
#     然后停留几秒用于数据加载
    time.sleep(3)

#     然后将新拿到的页面源码添加到源码列表当中
    all_page_lst.append(browser1.page_source)

# 验证一下
#
# print(all_page_lst)
#
# browser1.quit()
# 验证成功，之后开始解析数据拿到我们要爬取的内容，分别是ip地址和端口号



for page_text in all_page_lst:
    tree = etree.HTML(page_text)
    trs =tree.xpath('//tr[position()>1]/td[1]/text()')
    ports = tree.xpath('//tr[position()>1]/td[2]/text()')
    for i in range(len(trs)):
        ip = trs[i].strip()  # 去掉前后的空格
        port = ports[i].strip()
        # prox = '{\'http\':' + '\'' + f'{ip}:{port}' + '\'},'
        # prox_othertype =  f'\"{ip}:{port}' + '\",'
        prox_othertype =  f'\"http://{ip}:{port}' + '\",'
        # print(prox)
        print(prox_othertype)

'''
{'http':'114.232.109.88:8089'},
{'http':'114.231.42.23:8888'},
{'http':'113.223.215.204:8089'},
{'http':'117.69.236.23:8089'},
{'http':'120.55.37.254:80'},
{'http':'111.225.152.116:8089'},
{'http':'36.6.145.4:8089'},
{'http':'118.178.239.78:80'},
{'http':'117.71.155.32:8089'},
{'http':'117.57.92.25:8089'},
{'http':'114.231.45.207:8888'},
{'http':'113.223.214.141:8089'},
{'http':'114.231.82.16:8089'},
{'http':'111.225.152.64:8089'},
{'http':'113.223.213.132:8089'},
{'http':'117.69.233.129:8089'},
{'http':'119.183.249.236:9000'},
{'http':'36.6.145.95:8089'},
{'http':'36.6.145.83:8089'},
{'http':'117.69.233.19:8089'},
{'http':'113.121.22.221:9999'},
{'http':'183.164.242.59:8089'},
{'http':'117.69.233.60:8089'},
{'http':'121.41.79.83:80'},
{'http':'42.63.65.99:80'},
{'http':'36.6.144.210:8089'},
{'http':'36.6.144.113:8089'},
{'http':'183.164.243.43:8089'},
{'http':'123.56.13.137:80'},
{'http':'117.69.236.25:8089'},
{'http':'117.71.154.141:8089'},
{'http':'121.40.160.78:80'},
{'http':'42.63.65.78:80'},
{'http':'106.14.255.124:80'},
{'http':'125.87.94.168:8089'},
{'http':'47.94.207.215:3128'},
{'http':'42.63.65.19:80'},
{'http':'223.100.178.167:9091'},
{'http':'117.70.49.102:8089'},
成功'''