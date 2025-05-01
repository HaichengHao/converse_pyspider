from urllib.parse import urljoin

import scrapy
from ..items import DeskItem


class ImagesSpider(scrapy.Spider):
    name = "images"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://desk.zol.com.cn/dongman/"]
    model_url = 'https://desk.zol.com.cn/dongman/%d.html'
    page_number = 2;

    # 定义下载图片的方法
    def download_pics(self, response):
        item = response.meta['item']
        pic_url = response.xpath('/html/body/img[1]/@src').extract_first()
        print(f"图片链接:{pic_url}")
        item['pic_url'] = pic_url
        yield item

    # 定义详情页大图获取方法
    def parse_detail(self, response):
        biggest_img_url = response.xpath('//dd[@id="tagfbl"]/a/@href').extract()
        title = response.xpath('//a[@id="titleName"]/text()').extract_first()
        # print(title)
        if len(biggest_img_url) > 1:
            final_url = urljoin(self.start_urls[0], biggest_img_url[0])
            print("最终页面的链接", final_url)
            item = DeskItem()
            item['final_url'] = final_url
            item['title'] = title
            yield scrapy.Request(url=final_url, callback=self.download_pics, meta={'item': item})

    def parse(self, response):
        # //ul/li[@class="photo-list-padding"][position()>2]/a/@href
        # //ul/li[contain(@class,"photo-list-padding")][position()>2]/a/@href

        # 因为链接中有程序文件，但是我们不想要，所以可以利用Xpath直接剔除掉，或者做判断
        first_level_url = response.xpath('//ul/li[@class="photo-list-padding"][position()>2]/a/@href').extract()
        for url in first_level_url:
            print(url)
            # 作判断，剔除掉.exe文件,如果找到的不是-1,即匹配到了.exe则跳过此次循环continue
            if url.find('exe') != -1:  # 这里利用了字符串查找.find()的用法，如果没有匹配到则为-1,匹配到则为非-1的其它值
                continue
            else:
                detail_page_url = urljoin(self.start_urls[0], url)
                print(detail_page_url)
                yield scrapy.Request(url=detail_page_url, callback=self.parse_detail)
                break
        # if self.page_number < 2:
        #     new_page_url = self.model_url % self.page_number
        #     self.page_number += 1
        #     yield scrapy.Request(url=new_page_url, callback=self.parse)
