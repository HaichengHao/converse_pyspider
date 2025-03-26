import scrapy
from scrapy_redis.spiders import RedisSpider
from redis2 import Redis
from ..items import SecondItem
class TyzxSpider(RedisSpider): #important:注意这里换成了继承与RedisSpider
    conn = Redis(
        host='localhost',
        port=6379,
        db=14
    )
    name = "tyzx"
    # allowed_domains = ["www.xxx.com"]
    # start_urls = ["https://www.xxx.com"]
    redis_key = "tyzx_start_url"
    model_url = 'https://xintianya.net/index-%d.htm'
    page_number = 2

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

        if self.page_number < 15:
            new_url = self.model_url % self.page_number
            self.page_number += 1
            yield scrapy.Request(url=new_url, callback=self.parse)
    def parse_detail(self, response):
        usrname = response.xpath('//a[@class="text-muted"]/b/text()').extract_first()
        title = response.xpath('//span[@class="break-all"]/text()').extract_first().strip()
        # tips:实例化item对象
        item = SecondItem()
        item['usrname'] = usrname
        item['title'] = title
        # self.redis.sadd("tianya:ty:detail:url", response.url)
        yield item

