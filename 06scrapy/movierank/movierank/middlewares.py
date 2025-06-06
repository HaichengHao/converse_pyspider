# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

# 从settings.py 获取代理IP列表
from .settings import PROXY_IP_LIST
from random import choice

class MovierankSpiderMiddleware:
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


class MovierankDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    ua = UserAgent().random
    print(ua)
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        request.headers['User-Agent'] = self.ua
        #important:注意别返回任何东西!!!!



    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

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
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

#免费代理
class ProxyDownloaderMiddleware:

    def process_request(self,request,spider):
        ip = choice(PROXY_IP_LIST)
        print(ip)
        request.meta['proxy'] = ip
        return None #important:放行
    #videotimestamp 1'51''19'''

# 付费代理
class MoneyProxyDownloaderMiddleware:

    def process_request(self,request,spider):
        ip = choice(PROXY_IP_LIST)
        print(ip)
        request.meta['proxy'] = ip
        return None #important:放行
    def process_response(self,request,response,spider):
        if response.status != 200: #如果响应的状态码不对(也就是我们的请求没有正确的发送出去)
            #                           那么我们下次请求就不进入队列而直接发送
            request.dont_filter = True
            return request
        else:
            return response