import scrapy

from ..items import ImgproItem


class PicproSpider(scrapy.Spider):
    name = "picpro"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://ypk.39.net/pifu/p1/"]
    model_url = "https://ypk.39.net/pifu/p%d/"
    page_number = 2

    def detail_parse(self, response):
        meta = response.meta
        item = meta['item']
        title = response.xpath('//div[@class="drug-layout-r-stor"]/h1').extract_first().split('>')[1].split('<')[0]
        # print(title)
        item['title'] = title
        yield item

    def parse(self, response):
        li_lst = response.xpath('//ul[@class="drugs-ul"]/li')
        for li in li_lst:
            title = li.xpath('./a/@title').extract_first()
            img_src = li.xpath('./a/img/@src').extract_first()
            detail_url = li.xpath('./a/@href').extract_first()
            print(img_src)
            # print(detail_url)
            # print(title)
            # tips:实例化item对象
            item = ImgproItem()
            item['img_src'] = img_src
            yield scrapy.Request(meta={'item': item}, url=detail_url, callback=self.detail_parse)
        if self.page_number <= 2:
            new_url = self.model_url % self.page_number
            # print(new_url)
            self.page_number += 1
            yield scrapy.Request(url=new_url, callback=self.parse)
