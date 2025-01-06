import scrapy
from ..items import SixthGetpicItem

class ImgSpider(scrapy.Spider):
    name = "img"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://pic.netbian.com/4kfengjing/"]

    def parse(self, response):
        li_lst = response.xpath('//div[@class="slist"]/ul/li')
        for li in li_lst:
            img_src = 'https://pic.netbian.com'+li.xpath('./a/img/@src').extract_first()
            print(img_src)
            # important:实例化item对象
            item = SixthGetpicItem()
            item['src'] = img_src
            yield item