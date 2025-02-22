import random

from fake_useragent import UserAgent
from scrapy import signals


class Random_UserAgent_Proxy_Middleware:

    ua = UserAgent().random
    # print(ua)

    # tips:创建代理池
    proxies_pool = [
        'http://114.231.46.157:8089',
        'http://183.237.222.52:9002',

    ]
    proxy = random.choice(proxies_pool)
    def process_request(self, request, spider):

        # tips:这里用你说的fake_ua
        request.headers['User-Agent'] = self.ua
        print(request.headers['User-Agent'])
        # request.meta['proxy'] = self.proxy
        # print(request.meta['proxy'])

    def spider_opened(self, spider):
        pass