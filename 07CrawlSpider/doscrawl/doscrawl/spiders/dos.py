import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from ..items import DoscrawlItem
# important:导入需要的包
#  修改爬虫类的父类为导入的RedisCrawlSpider
#  将start_urls注释掉 新写redis_key
class DosSpider(RedisCrawlSpider): #tips:继承自RedisCrawlSpider
    name = "dos"
    # allowed_domains = ["www.xxx.com"]
    # start_urls = ["https://www.xxx.com"] #important:注意，起始url是最后添加的,详细查看md文件，目前不用添加
    redis_key = 'queueTitle' #tips:表示调度器队列的名称
    rules = (Rule(LinkExtractor(allow=r"id=1&page=\d+"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        li_list = response.xpath('//ul[@class="title-state-ul"]/li')
        for li in li_list:
            title = li.xpath('./span[3]/a/text()').extract_first()
            status = li.xpath('./span[2]/text()').extract_first()
            # print(title,status)
            item = DoscrawlItem()
            item['title'] = title
            item['status'] = status
            print(item)
            yield item

