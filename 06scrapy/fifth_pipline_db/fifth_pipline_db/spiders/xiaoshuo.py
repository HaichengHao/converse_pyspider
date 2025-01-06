import scrapy
from ..items import FifthPiplineDbItem

class XiaoshuoSpider(scrapy.Spider):
    name = "xiaoshuo"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.shicimingjv.com/bookindex/8.html"]
#important:注意，写解析的时候一定要注意xpath解析的节点关系，最开始写成了//ul[@class="book-tags"]
# 然后遍历ul,其实就只有一个ul,所以遇到很多坑点，一定要规范层级
    def parse(self, response):
        all_li = response.xpath('//ul[@class="book-tags"]/li')
        # print(all_ul)
        for li in all_li:
            # print(li)
            title = li.xpath('./a/text()').extract_first()
            # print(title)
            # important:实例化item对象
            item = FifthPiplineDbItem()
            item['title'] = title
            yield item


