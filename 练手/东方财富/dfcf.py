"""
@File    :dfcf.py
@Editor  : 百年
@Date    :2025/5/9 14:46 
"""
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from lxml import etree
import csv

service = Service('../chromedriver.exe')

bro1 = Chrome(service=service)

bro1.get('https://data.eastmoney.com/gstc/default.html?keyword=%E7%A9%BA%E8%B0%83%E8%AE%BE%E5%A4%87')

time.sleep(3)

page_source = bro1.page_source
# print(bro1.page_source)
# print(page_source)

tree = etree.HTML(page_source)
i = 1
for i in range(21):
    tr_lst = tree.xpath(f'//*[@id="dataview"]/div[4]/div[1]/table/tbody/tr[{i}]')
    for tr in tr_lst:
        gupiao = tr.xpath('./td[2]/a[1]/text()')
        piaohao = tr.xpath('./td[2]/a[2]/text()')
        shoupan = tr.xpath('./td[3]/span/text()')
        zhangdiefu = tr.xpath('./td[4]/span/text()')
        gongsijianjie = tr.xpath('./td[6]/div/p[1]/text()')
        suoshubankuai = tr.xpath('./td[6]/div/p[2]/text()')
        zhuyingyewu = tr.xpath('./td[6]/div/p[3]/text()')
        zongshizhi = tr.xpath('./td[7]/text()')
        shiyinglv = tr.xpath('./td[8]/text()')
        shijinglv = tr.xpath('./td[9]/text()')
        print(gupiao)
        # rowdata = [gupiao[0],piaohao[0],shoupan[0],zhangdiefu[0],gongsijianjie[0],suoshubankuai[0],zhuyingyewu[0],zongshizhi[0],shiyinglv[0],shijinglv[0]]
        # print(rowdata)


