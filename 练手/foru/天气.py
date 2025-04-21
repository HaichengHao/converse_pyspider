from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from lxml import etree
import csv

fp = open('./tianqi.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(fp)
if fp.tell() == 0:
    writer.writerow(['日期', '星期', '最低温度', '最高温度', '天气', '风向', '风力'])

service = Service('./chromedriver.exe')

bro1 = Chrome(service=service)

bro1.get('https://m.tianqi.com/lishi/haerbin/202503.html')
time.sleep(2)
more_btn = bro1.find_element(By.XPATH, '//div[contains(@class,"linsmore")][1]')
more_btn.click()
time.sleep(3)

page_source = bro1.page_source
# print(page_source)

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
bro1.close()
