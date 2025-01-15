# # Define here the models for your spider middleware
# #
# # See documentation in:
# # https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# import random
# import time
#
# from scrapy import signals
# from scrapy.http import HtmlResponse  # important:scrapy封装的响应对象对应的一个类
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.webdriver import Service
# from selenium import webdriver
#
# class WangyinewsDownloaderMiddleware:
#     #important: 创建浏览器对象
#     service = Service(r'E:\converse_spider\converse_pyspider\06scrapy\wangyinews\chromedriver.exe')
#     browser1 = Chrome(service=service)
#
#     def process_request(self, request, spider):
#         return None
#
#     def process_response(self, request, response, spider):
#         print(request.url+'响应对象拦截成功')
#         # 可以拦截到当前所有的响应对象
#         # tips:有1（起始url）+4(我们要获得的四个板块)+n(每个板块下的新闻数量)个响应对象
#         #QUIZ:如何筛选出指定的四个板块的响应对象呢?
#         #answer:1可以先找出指定4个板块的请求对象request然后根据请求对象定位4个响应对象
#         # 2可以根据四个板块的url定位到四个板块的对象
#         model_urls = request.meta.get('model_urls',[]) #tips:将spider文件中的model_urls赋值给model_urls
#         print(model_urls)
#         # important:这里的判断也就是判断请求的链接是不是四个模块的链接,如果是就按照条件语句来处理
#         #  因为只有在请求这四个板块的链接数据是动态加载的数据，所以要上selenium
#         if request.url in model_urls:
#             browser1 = self.browser1 #tips:从爬虫类中获取创建好的浏览器对象
#             url = request.url
#             print(url+'被拦截到了')
#             browser1.get(request.url)
#             time.sleep(4)
#             page_text = browser1.page_source #important:获取动态加载的数据，将这个数据给body
#                   #tips:如果条件成立，说明该request就是指定响应对象的请求对象
#                   #tips:此处的response就是指定板块对应的响应对象
#             time.sleep(4)
#             response = HtmlResponse(url=request.url,request=request,encoding='utf-8',body=page_text)
#         #           important:body就是响应对象的响应数据，它是只读的
#             return response
#         else: #important:如果不是那四个模块的请求链接，那就按照正常的链接处理
#             return response
#
#
#     def process_exception(self, request, exception, spider):
#         return request
#     def spider_opened(self, spider):
#         spider.logger.info("Spider opened: %s" % spider.name)
#     def spider_closed(self,spider):
#         self.browser1.quit()




# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import requests
from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from time import sleep
from scrapy.http import HtmlResponse#scrapy封装的响应对象对应的类
class WangyinewsDownloaderMiddleware:


    def process_request(self, request, spider):

        return None

    def process_response(self, request, response, spider):
        #可以拦截到所有的响应对象
        #当前项目一共会产生多少个响应对象呢？
         #1 + 4 + n个响应对象，在这些响应对象中只有4这4个响应对象需要被修改
        #如何筛选出指定的4个板块对应的响应对象呢？
            #1.可以先找出指定4个板块的请求对象，然后根据请求对象定位指定4个响应对象
            #2.可以根据4个板块的url定位到四个板块的请求对象
        model_urls = spider.model_urls
        if request.url in model_urls:
            bro = spider.bro #从爬虫类中获取创建好的浏览器对象
            bro.get(request.url)
            sleep(1)
            # bro.execute_script('document.documentElement.scrollTo(0,9000)')
            # sleep(1)
            #获取动态加载的数据
            page_text = bro.page_source
            #说明该request就是指定响应对象的请求对象
            #此处的response就是指定板块对应的响应对象
            response = HtmlResponse(url=request.url,
                                    request=request,
                                    encoding='utf-8',
                                    body=page_text)
                                #body就是响应对象的响应数据
            return response
        else:
            return response

    def process_exception(self, request, exception, spider):
       pass

