# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent
import random
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MidmidSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)



class MidmidDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    ua = UserAgent().random
    print(ua)

    proxies_pool=[
        {'http': '61.160.202.63:80'},
        {'http': '117.71.149.139:8089'},
        {'http': '61.160.202.99:80'},
        {'http': '36.6.145.190:8089'},
        {'http': '183.164.243.160:8089'},
        {'http': '140.207.229.171:80'},
        {'http': '61.160.202.107:80'},
        {'http': '159.226.227.78:80'},
        {'http': '117.69.232.185:8089'},
        {'http': '120.26.200.176:80'},
        {'http': '113.223.215.45:8089'},
        {'http': '36.6.144.245:8089'},
        {'http': '61.160.202.101:80'},
        {'http': '36.6.144.13:8089'},
        {'http': '114.231.46.111:8089'},
        {'http': '117.69.236.189:8089'},
        {'http': '114.231.46.247:8089'},
        {'http': '117.71.133.217:8089'},
        {'http': '47.101.153.1:80'},
        {'http': '36.6.145.143:8089'},
        {'http': '121.40.118.246:80'},
        {'http': '122.136.212.132:53281'},
        {'http': '183.164.242.203:8089'},
        {'http': '117.57.92.22:8089'},
        {'http': '114.103.81.215:8089'},
        {'http': '113.223.213.37:8089'},
        {'http': '114.231.82.87:8089'},
        {'http': '120.55.13.197:80'},
        {'http': '117.57.92.185:8089'},
        {'http': '114.231.8.213:8089'},
        {'http': '112.17.16.206:80'},
        {'http': '123.182.59.140:8089'},
        {'http': '144.255.49.190:9999'},
        {'http': '101.37.80.123:80'},
        {'http': '183.164.242.189:8089'},
        {'http': '183.164.242.243:8089'},
        {'http': '117.71.154.159:8089'},
        {'http': '113.223.213.80:8089'},
        {'http': '114.231.8.209:8888'},
        {'http': '117.69.236.189:8089'},
        {'http': '114.231.46.247:8089'},
        {'http': '117.71.133.217:8089'},
        {'http': '47.101.153.1:80'},
        {'http': '36.6.145.143:8089'},
        {'http': '121.40.118.246:80'},
        {'http': '122.136.212.132:53281'},
        {'http': '183.164.242.203:8089'},
        {'http': '117.57.92.22:8089'},
        {'http': '114.103.81.215:8089'},
        {'http': '113.223.213.37:8089'},
        {'http': '114.231.82.87:8089'},
        {'http': '120.55.13.197:80'},
        {'http': '117.57.92.185:8089'},
        {'http': '114.231.8.213:8089'},
        {'http': '112.17.16.206:80'},
        {'http': '123.182.59.140:8089'},
        {'http': '144.255.49.190:9999'},
        {'http': '101.37.80.123:80'},
        {'http': '183.164.242.189:8089'},
        {'http': '183.164.242.243:8089'},
        {'http': '117.71.154.159:8089'},
        {'http': '113.223.213.80:8089'},
        {'http': '114.231.8.209:8888'},
        {'http': '117.71.154.235:8089'},
        {'http': '223.123.100.138:8080'},
        {'http': '117.71.133.220:8089'},
        {'http': '183.164.243.74:8089'},
        {'http': '118.193.102.3:7890'},
        {'http': '47.98.107.25:80'},
        {'http': '117.71.149.146:8089'},
        {'http': '117.69.233.123:8089'},
        {'http': '183.164.242.161:8089'},
        {'http': '117.69.236.8:8089'},
        {'http': '175.178.195.7:80'},
        {'http': '114.231.41.190:8089'},
        {'http': '113.124.86.253:9999'},
        {'http': '120.194.4.157:5443'},
        {'http': '36.6.145.212:8089'}
    ]
    proxy =random.choice(proxies_pool)
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # return None #tips:return None则当前中间件不进行拦截
        # tips:如果返回的是request，后续的中间件将不再执行，请求重新交给引擎，引擎重新扔给调度器
        # tips:如果返回的是Response,后续的中间件将不再执行，将响应信息交给引擎，引擎再交给spider,进行数据处理
        # important:process的返回值不是瞎给的，瞎给会出问题
        # step 2:再执行process_request，对请求进行处理
        print('我是proecess_request')
        request.headers['User-Agent'] = self.ua
        # request.meta['proxy'] = self.proxy
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        print('我是process_reqponse') #step 3:然后执行process_response对响应进行处理
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        # pass
        print('我是process_response,只有报错的时候你才会看到这条信息')
    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
        print('我是spider_opened') #step 1:先执行这个方法



class MidmidDownloaderMiddleware2:

    def process_request(self, request, spider):

        print('我是proecess_request2')

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        print('我是process_reqponse2') #step 3:然后执行process_response对响应进行处理

        return response

    def process_exception(self, request, exception, spider):

        print('我是process_response2,只有报错的时候你才会看到这条信息')
    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
        print('我是spider_opened2') #step 1:先执行这个方法