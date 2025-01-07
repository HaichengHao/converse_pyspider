import scrapy
from ..items import SeventhpicpicItem
class BookpicSpider(scrapy.Spider):
    name = "bookpic"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.shuqi.com/store?spm=aliwx.pc-web-bookstore.0.0"]
    # start_urls = ["https://ypk.39.net/pifu/p3/"]

    def parse(self, response):
#         //div[@class="store-content"]/ul/li/a/img/@src <--图片链接
# //div[@class="store-content"]/ul/li/a[1]/@title <--书籍名称
        li_lst = response.xpath('//div[@class="store-content"]/ul/li')
        # li_lst = response.xpath('//ul[@class="drugs-ul"]/li')

        for li in li_lst:
            src = li.xpath('./a/img/@src').extract_first()
            # book_title = li.xpath('./a[1]/@title').extract_first()
            # tips:先打印看看是否获取成功
            print(src)
            # print(book_title)
            # important:实例化item对象
            item = SeventhpicpicItem()
            item['src'] = src
            # item['book_title'] = book_title
            #
            # #important:生成item对象，提交给管道
            yield item
