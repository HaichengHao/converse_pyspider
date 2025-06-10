"""
@File    :sessionpage改写天气.py
@Editor  : 百年
@Date    :2025/6/5 9:11 
"""
from DrissionPage import ChromiumPage
from lxml import etree
import csv
page = ChromiumPage()
month = int(input('请输入月份,注意不能超过或等于当前月!!>>'))
url = f'https://m.tianqi.com/lishi/haerbin/20250{month}.html'
page.get(url)
ckgd = page.ele('.linsmore flex_cen show1')
ckgd.click()

page_source = page.html
fp = open('./tianqi.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(fp)
if fp.tell() == 0:
    writer.writerow(['日期', '星期', '最低温度', '最高温度', '天气', '风向', '风力'])
tree = etree.HTML(page_source)

alst = tree.xpath('//div[@class="alioq"]/a')

for a in alst:
    date = a.xpath('./div[1]/span/text()')
    tam_max = a.xpath('./div[2]/text()')
    tam_min = a.xpath('./div[3]/text()')
    weather = a.xpath('./div[4]/text()')
    winddata = a.xpath('./div[5]/span/text()')
    rowdata = [date[0], date[1], tam_min[0], tam_max[0], weather[0], winddata[0], winddata[1]]
    print(rowdata)
    writer.writerow(rowdata)

fp.close()