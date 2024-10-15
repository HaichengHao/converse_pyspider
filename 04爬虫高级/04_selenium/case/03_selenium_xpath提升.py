# @Editor    : 百年
# @FileName  :03_selenium_xpath提升.py
# @Time      :2024/10/15 20:06
'''
重要思路:
将所有的页面源码数据添加到一个列表当中
然后列表添加页面数据完毕之后，再遍历列表中的每个页面的源码进行解析
最后得到数据
'''
from selenium.webdriver import Chrome
import time
from lxml import etree

# 构建浏览器
browser1 = Chrome(executable_path='../others/chromedriver.exe')

browser1.get('https://ypk.39.net/ganmao/k1')
time.sleep(2)
page_ = browser1.page_source

# 将前五页的页面源码数据放到列表当中
# 首先创建一个列表用于存储得到的所有页面源码数据，记得把第一页得先放进去,后续的几页添加到列表中即可
all_page_lst = [page_]
for i in range(4):
    nxt_btn = browser1.find_element_by_xpath('/html/body/div[4]/div[3]/div[2]/div[2]/div[2]/div/p/a[6]')

    # 点击下一页
    nxt_btn.click()
    # 停留几秒用于加载数据
    time.sleep(3)

    all_page_lst.append(browser1.page_source)

# 解析数据
for page_text in all_page_lst:
    tree = etree.HTML(page_text)
    li_list = tree.xpath('/html/body/div[4]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
    # print(li_list)
    time.sleep(1)
    for li in li_list:
        title = li.xpath("./div[@class='drugs-brief']/p/a/@title")[0]
        print(title)

time.sleep(2)
# 关闭浏览器
browser1.quit()
'''
D:\python\python.exe D:/converse_fullstack/converse/04爬虫高级/04_selenium/case/03_selenium_xpath提升.py
对乙酰氨基酚栓
氯芬黄敏片
阿咖酚散
氨咖黄敏胶囊
氨咖黄敏胶囊
氨咖黄敏胶囊
清凉喉片
阿司匹林肠溶片
阿司匹林肠溶片
阿司匹林肠溶片
阿司匹林肠溶片
阿咖酚散
氯芬黄敏片
新复方大青叶片
对乙酰氨基酚片
感冒消炎片
阿司匹林肠溶片
利巴韦林含片
牛磺酸颗粒
氨咖黄敏片
布洛芬片
小儿氨酚黄那敏片
安乃近片
维C银翘片
阿司匹林肠溶片
阿司匹林肠溶片
对乙酰氨基酚片
对乙酰氨基酚栓
氨咖黄敏胶囊
感冒清胶囊
清火栀麦片
清凉喉片
复方氨酚烷胺片
十滴水
氨咖黄敏胶囊
吲哚美辛肠溶片
阿司匹林肠溶片
阿司匹林肠溶片
穿心莲片
酚氨咖敏片
十滴水
维C银翘片
小儿复方氨酚烷胺片
十滴水
布洛芬片
布洛芬片
牛磺酸颗粒
阿司匹林肠溶片
健步强身丸
壮骨药酒
七杏牌善清软胶囊
洞天长春膏
磷酸奥司他韦胶囊
三奇堂牌京茶
嘉德牌牛蒡茶
热毒宁注射液
娃娃宁泡腾片
清脑止痛胶囊
清宫长春胶囊
血康口服液
复方海蛇胶囊
男康片
同仁堂牌同仁益健茶
百合康牌越橘叶黄素软胶囊
帕拉米韦氯化钠注射液
海蛇药酒
十一味金色丸
野木瓜胶囊

Process finished with exit code 0
'''
