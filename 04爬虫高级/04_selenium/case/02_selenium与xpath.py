# @Editor    : 百年
# @FileName  :02_selenium与xpath.py
# @Time      :2024/10/14 22:53
from selenium.webdriver import Chrome
import time
from lxml import etree

# 构建浏览器
browser1 = Chrome(executable_path='../others/chromedriver.exe')

browser1.get('https://ypk.39.net/ganmao/k1')
time.sleep(2)
page_ = browser1.page_source
tree = etree.HTML(page_)
li_list = tree.xpath('/html/body/div[4]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
# print(li_list)
time.sleep(1)
for li in li_list:
    title = li.xpath("./div[@class='drugs-brief']/p/a/@title")[0]
    print(title)

time.sleep(2)
# 关闭浏览器
browser1.quit()