import scrapy
from scrapy_redis.spiders import RedisSpider, RedisCrawlSpider
# 现在用的不再是scrapy.spider 了，改为用RedisSpider
# 如果用的是连接提取器那一套的crawl_spider的话可以用RedisCrawlSpider
from urllib.parse import urljoin
from redis2 import Redis
from ..items import Dosdemo1Item


class TianyaSpider(RedisSpider):  # 注意括号内的内容也要跟着换
    # conn = redis.Redis(
    #     host='localhost',
    #     port=6379,
    #     db=12
    # )

    name = "tianyaa"
    # allowed_domains = ["www.xxx.com"]
    # start_urls = ["https://xintianya.net/"] #important:start_urls不直接写了而是被下方的redis-key取代
    redis_key = "ty_start_url"
    # jurl = "https://xintianya.net/"
    model_url = 'https://xintianya.net/index-%d.htm'

    page_number = 2

    def __init__(self, name=None, **kwargs):
        self.redis = Redis(
            host="localhost",
            port=6379,
            db=12,
        )
        # 让父类初始化
        super(TianyaSpider, self).__init__(name, **kwargs)

    def parse(self, response):
        urls = response.xpath(
            '//div[@class="card card-threadlist"]//ul/li/div[@class="media-body"]/div/a/@href').extract()
        for url in urls:
            detail_url = 'https://xintianya.net/' + url
            print(detail_url)
            # tips:和之前不同的是，这里不用判断是否出现重复,所有的判断工作，全都交给scrapy-redis完成
            yield scrapy.Request(
                url=detail_url,
                callback=self.parse_detail
            )

        # if self.page_number < 10:
        #     new_url = self.model_url % self.page_number
        #     self.page_number += 1
        #     yield scrapy.Request(url=new_url, callback=self.parse)

        # tips:写法2
        next_href = response.xpath('//div[@class="btn btn-light btn-block mt-2 loadmore"]/@data-url').extract_first()
        yield scrapy.Request(
            url='https://xintianya.net/' + next_href,
            callback=self.parse
        )

    def parse_detail(self, response):
        usrname = response.xpath('//a[@class="text-muted"]/b/text()').extract_first()
        title = response.xpath('//span[@class="break-all"]/text()').extract_first().strip()
        # tips:实例化item对象
        item = Dosdemo1Item()
        item['usrname'] = usrname
        item['title'] = title
        # self.redis.sadd("tianya:ty:detail:url", response.url)
        yield item
