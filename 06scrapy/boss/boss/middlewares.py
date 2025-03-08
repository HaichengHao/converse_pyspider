# # Define here the models for your spider middleware
# #
# # See documentation in:
# # https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# import time
#
import time

from scrapy import signals
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse
from boss.request import SeleniumRequest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service


class BossDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s


    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
        service = Service('E:/converse_spider/converse_pyspider/06scrapy/chromedriver.exe')
        self.bro = Chrome(service=service)  # 创建浏览器对象

    def spider_closed(self, spider):
        spider.logger.info("Spider closed: %s" % spider.name)
        self.bro.quit()

    def process_request(self, request, spider):
        if isinstance(request, SeleniumRequest):  # tips:可以看看isinstance的说明,isinstance(x,A_tiple),判断x是否在A_tuple内
            # tips:其实这里就是做了个判断，判断request是否是SeleniumRequest
            print('开始')
            self.bro.get(url=request.url)
            time.sleep(6)  # 让selenium操作的元素加载出来
            page_source = self.bro.page_source
            # 因为返回对象只能是None,Request,Response这三种，所以我们需要将page_source转换成HtmlResponse，将其从字符串对象封装成Response
            # response = HtmlResponse(url=request.url, body=page_source, encoding='utf-8')
            # return response
            return HtmlResponse(url=request.url, body=page_source, encoding='utf-8',request=request)
        else:  # tips:如果请求不是Selenium的就放行
            print('普通请求')
            return None
        # tips:所有的请求都会到这里
        # 需要进行判断，判断是否需要selenium
        # 开始selenium的操作，返回页面源代码组装的Response
        # self.bro.get(url=request.url)
        # time.sleep(6)
        # page_source = self.bro.page_source
        # # 因为返回对象只能是None,Request,Response这三种，所以我们需要将page_source转换成HtmlResponse，将其从字符串对象封装成Response
        # response = HtmlResponse(url=request.url, body=page_source, encoding='utf-8')
        # return response



# from scrapy import signals
# from scrapy.http import HtmlResponse
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from boss.request import SeleniumRequest
#
# class BossDownloaderMiddleware:
#     @classmethod
#     def from_crawler(cls, crawler):
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
#         return s
#
#     def spider_opened(self, spider):
#         spider.logger.info("Spider opened: %s" % spider.name)
#         service = Service('E:/converse_spider/converse_pyspider/06scrapy/chromedriver.exe')
#         self.bro = Chrome(service=service)
#
#     def spider_closed(self, spider):
#         spider.logger.info("Spider closed: %s" % spider.name)
#         self.bro.quit()
#
#     def process_request(self, request, spider):
#         if isinstance(request, SeleniumRequest):
#             self.bro.get(request.url)
#             try:
#                 # 使用WebDriverWait等待某个元素加载完成作为页面准备好的标志
#                 element = WebDriverWait(self.bro, 10).until(
#                     EC.presence_of_element_located((By.XPATH, '//ul[@class="job-list-box"]'))
#                 )
#                 page_source = self.bro.page_source
#                 return HtmlResponse(url=request.url, body=page_source, encoding='utf-8', request=request)
#             except Exception as e:
#                 spider.logger.error(f"Error processing Selenium request: {e}")
#                 return HtmlResponse(url=request.url, status=500, request=request)
#         else:
#             return None
