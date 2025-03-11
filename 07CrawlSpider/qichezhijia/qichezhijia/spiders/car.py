import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CarSpider(CrawlSpider):
    name = "car"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.che168.com/zhengzhou/dazhong/#pvareaid=108402#listfilterstart"]
    le = LinkExtractor(restrict_xpaths=('//ul[@class="viewlist_ul"]//li[position()<57]/a',))
    le2 = LinkExtractor(restrict_xpaths=('//div[@id="listpagination"]/a[position()>1]',))
    rules = (
        Rule(le, callback="parse_item", follow=False), #获取详情页的链接
        Rule(le2, follow=True), #获取分页链接
    )

    def parse_item(self, response):
        try:
            title = response.xpath('//h3[@class="car-brand-name"]/text()').extract_first()
        except IndexError:
            title = response.xpath('/html/body/div[5]/div[2]/h3').extract_first()
        try:
            price = response.xpath('//div[@class="brand-price-item"]/span[@id="overlayPrice"]/text()').extract_first()
        except None:
            print(response.url)
        print(title,price)
