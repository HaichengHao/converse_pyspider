import time

import scrapy

from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from scrapy.http import HtmlResponse #important:由于彩票网站改版了，所以简单例子没法使用,刚好之前未修整部分的wangyipro是用selenium写的
                                     # 但是也是修修改改，尤其是Response的性质，单纯作为requests学习时期的理解是不行的,它不是个字符串
#                                      所以需要用HtmlResponse来将我们的请求打包成在scrapy框架中可以理解的数据形式
from ..items import CaipiaoItem
service = Service('E:/converse_spider/converse_pyspider/06scrapy/chromedriver.exe')






class SsqSpider(scrapy.Spider):
    # tips:创建浏览器对象
    browser = Chrome(service=service)
    name = "ssq"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://datachart.500.com/ssq/?"]
    model_urls = ["https://datachart.500.com/ssq/?"]
    print(start_urls[0])
    browser.get(url=start_urls[0])
    time.sleep(8)
    page_text = browser.page_source
    myresponse = HtmlResponse(url=model_urls[0],encoding='utf-8', body=page_text)

    print(myresponse)

    def parse(self, response):
        myresponse = self.myresponse
        tr_lst = myresponse.xpath('//*[@id="tdata"]/tr')
        for tr in tr_lst:
            if tr.xpath("./@class").extract_first() == "tdbck":
                continue
            date = tr.xpath('./td[1]/text()').extract_first()
            red_ball = tr.xpath('./td[@class="chartBall01"]/text()').extract()
            blue_ball = tr.xpath('./td[@class="chartBall01 chartBall07"]/text()').extract()
            # important:scrapy支持xpath和css混合使用
            # red_ball = tr.css(".chartBall01::text").extract() #这里就是使用了类选择器
            # print(red_ball)
            # print(blue_ball)

            # 要么这样写
            # dic = {
            #     'qihao':date,
            #     'red_ball':red_ball,
            #     'blue_ball':blue_ball
            # }
            # yield dic #tips:将会对其传入管道
            # # tips: 要么就引入item一个个好好写
            item= CaipiaoItem()
            item['date'] = date
            item['red_ball'] = red_ball
            item['blue_ball'] = blue_ball
            yield item
            # step :注意，要是用这个方式需要到items文件中进行各个键的Filed