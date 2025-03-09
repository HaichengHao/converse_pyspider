from urllib.parse import urljoin

import scrapy
from ..items import QichezhijiaItem

class CarSpider(scrapy.Spider):
    name = "car"
    # allowed_domains = ["www.xxx.com"] #tips:这次居然被这玩意儿卡住了，果然一开始没注释掉导致无法访问详情页面
    start_urls = ["https://www.che168.com/zhengzhou/dazhong/#pvareaid=108402#listfilterstart"]

    def parse(self, response):
        # //ul[@class="viewlist_ul"]//li[position()<57]/a/@href

        li_lst= response.xpath('//ul[@class="viewlist_ul"]//li[position()<57]')

        # print(response.text)
        for li in li_lst:
            item = QichezhijiaItem()
            a = li.xpath('./a/@href').extract_first()
            url = urljoin(self.start_urls[0], a)
            print(url)
            car_title = li.xpath('./a/div/h4/text()').extract_first().strip()
            unitinfo = li.xpath('./a/div/p/text()').extract_first()
            licheng = unitinfo.split('／')[0]
            item['licheng'] =licheng
            item['car_title'] = car_title
            yield scrapy.Request(meta={'item':item},url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        item = response.meta['item']
        li_lst = response.xpath('//div[@class="car-box"]/ul/li/h4/text()').extract()
        price = response.xpath('/html/body/div[5]/div[2]/div[2]/span/text()').extract_first()
        # licheng = li_lst[0]
        try:
            shijian = li_lst[1]
        except IndexError:
            shijian = ''
        try:
            leixing = li_lst[2]
        except IndexError:
            leixing = ''
        try:
            area = li_lst[3]
        except IndexError:
            area = ''
        try:
            guobiao = li_lst[4].strip()
        except IndexError:
            guobiao = ''
        item['price'] = price
        # item['licheng'] = licheng
        item['shijian'] = shijian
        item['leixing'] = leixing
        item['area'] = area
        item['guobiao'] = guobiao
        yield item

