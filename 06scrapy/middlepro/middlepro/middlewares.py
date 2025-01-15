# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import random

#tips:爬虫中间件
class MiddleproSpiderMiddleware:
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

#tips:下载中间件
class MiddleproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    # tips:创建UA池子
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    # tips:创建代理池
    proxies_pool =[
        'http://114.231.46.157:8089',
        'http://183.237.222.52:9002',
        'http://114.231.8.234:8089',
        'http://120.26.200.176:80',
        'http://114.231.42.91:8089',
        'http://120.194.4.157:5443',
        'http://223.247.46.104:8089',
        'http://117.71.132.198:8089',
        'http://114.55.108.157:80',
        'http://121.41.92.60:80',
        'http://117.71.155.198:8089',
        'http://114.231.42.53:8888',
        'http://42.63.65.86:80',
        'http://114.231.8.190:8089',
        'http://117.57.92.198:8089',
        'http://114.231.45.73:8089',
        'http://116.63.128.247:10000',
        'http://117.69.236.85:8089',
        'http://36.6.145.54:8089',
        'http://117.71.155.126:8089',
        'http://117.71.154.36:8089',
        'http://114.55.176.8:80',
        'http://114.231.45.179:8089',
        'http://36.6.145.128:8089',
        'http://114.231.42.203:8888',
        'http://113.121.42.98:9999',
        'http://111.225.152.174:8089',
        'http://117.160.250.138:81',
        'http://117.71.154.124:8089',
        'http://61.133.66.69:9002',
        'http://114.55.179.125:80',
        'http://117.71.155.127:8089',
        'http://47.113.224.182:9999',
        'http://114.231.46.129:8888',
        'http://117.57.92.138:8089',
        'http://117.71.155.163:8089',
        'http://111.225.153.123:8089',
        'http://114.231.46.27:8089',
        'http://117.71.149.55:8089',
    ]
    proxy = random.choice(proxies_pool)
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    #tips:拦截处理所有(注意是所有的，它啥请求对象都能拦截，包括异常的请求对象)的请求对象
    # 参数
    # request就是拦截到的请求对象,
    # spider是爬虫文件中爬虫类实例化的对象
    # spider参数的作用可以实现爬虫类(就是主要的爬虫文件.py中的MidWareSpider(scrapy.Spider))和中间类(middlewares.py)的数据交互
    def process_request(self, request, spider):
        # important:设置cookie
        request.headers['cookie'] = "_ga=GA1.1.810589771.1731661878; .AspNetCore.Antiforgery.b8-pDmTq1XM=CfDJ8DfB03_iObVLoqH7ndAeeDgA8xRboGahkSQ8CVk6yIJDuHcBg8cgip0_k1lxBoTi5sa4UycX9ULQsZvhPycViGVMqL6WSpg_jiBdhE8hS9Mf_vhU9ZAutalf-BmjfbODPY1jaYG-lPM1SJ9f-Muc19o; Hm_lvt_866c9be12d4a814454792b1fd0fed295=1735102606,1736669597; Hm_lpvt_866c9be12d4a814454792b1fd0fed295=1736669597; HMACCOUNT=36598DCD2F5A4067; _ga_M95P3TTWJZ=GS1.1.1736669597.4.0.1736669597.0.0.0"
        # tips:也可以这样写
        #  request.cookies='_ga=GA1.1.810589771.1731661878; .AspNetCore.Antiforgery.b8-pDmTq1XM=CfDJ8DfB03_iObVLoqH7ndAeeDgA8xRboGahkSQ8CVk6yIJDuHcBg8cgip0_k1lxBoTi5sa4UycX9ULQsZvhPycViGVMqL6WSpg_jiBdhE8hS9Mf_vhU9ZAutalf-BmjfbODPY1jaYG-lPM1SJ9f-Muc19o; Hm_lvt_866c9be12d4a814454792b1fd0fed295=1735102606,1736669597; Hm_lpvt_866c9be12d4a814454792b1fd0fed295=1736669597; HMACCOUNT=36598DCD2F5A4067; _ga_M95P3TTWJZ=GS1.1.1736669597.4.0.1736669597.0.0.0'
        #important:设置UA
        request.headers['User-Agent'] = random.choice(self.user_agent_list)
        # tips:尝试打印输出拦截到的请求
        print(request.url+':拦截成功!')



        #important:若想所有的请求都是用代理，则代理操作可以写在该方法当中
        # request.meta['proxy'] = self.proxy
        #tips:弊端-会使得整体的请求效率变低

        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    #tips: 拦截处理所有的响应对象
    # 参数:
    # response就是拦截到的响应对象
    # request是被拦截到响应的对象对应的唯一的请求对象
    # spider对应的仍然四爬虫类实例化的对象
    def process_response(self, request, response, spider):
        print(request.url+':响应对象拦截成功!!')
        # Called with the response returned from the downloader.
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    #tips: 处理和拦截发生异常的请求对象
    # 参数:
    # request就是拦截到的发生异常的请求对象
    # exception就是异常类
    # spider对应的仍然是爬虫类实例化的对象
    #QUIZ:process_exception存在的意义是什么?
    #answer:将发生异常的请求拦截到，对其进行修正，修正之后的请求对象重新进行发送，本着不放弃任何请求的准则
    def process_exception(self, request, exception, spider):
        print(request.url+':发生异常的请求对象被拦截到了!!')
        print('目前使用的代理为:',self.proxy)
        request.meta['proxy'] = self.proxy
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        return request #tips:对请求对象进行重新发送
    #tips:控制日志输出的(忽略)
    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

#tips:代理操作可以写在process_request当中，也可以写在process_exception当中
# 但是，推荐写在process_exception当中