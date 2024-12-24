import scrapy
from ..items import FourthPersistentStoragePiplineItem
# abst:本节利用的持久化存储方式是管道而不再是终端命令
#  大致步骤：
#   1.在爬虫文件中进行数据解析操作
#   2.将解析到的数据封装到item类型的对象中
#       去itmes.py文件中定义相关的字段
#           xx.filed()
#       还要将items.py中的那个封装字段的类引入到爬虫文件当中
#           from items import FourthPersistentStoragePiplineItem
#       接下来再在爬虫文件中实例化一个item对象
#           item = FourthPersistentStoragePiplineItem()
#       将解析到的数据传入给item对象的成员
#           item['title'] = title
#           item['date'] = date
#           item['content'] = content
#   3.将item对象提交给管道piplines.py
#       yiled item
#   4.在管道中接收item类型对象
#       管道只可以接收item类型的对象，不能接收其它类型的对象
#   5.在管道中对接收到的数据进行任意形式的持久化存储操作
#       可以存储到文件中也可以存储到数据库中
#       在piplines.py文件中进行代码编写操作
#       还要重写两个方法open_spider(self,spider)和close_spider(self,spider)
#       在open_spider前要先指定fp=None
#   6.在配置文件中开启管道机制
#       在settings.py中解除ITEM_PIPELINES的注释
class PiplinestorageSpider(scrapy.Spider):
    name = "piplinestorage"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.wogif.com/duanzi/"]

    def parse(self, response):
        alldiv = response.xpath('//div[@class="xxl-item"]/a/div[@class="xxl-con"]')
        for div in alldiv:
            title = div.xpath('./h2').extract_first().replace('<h2>', '').replace('</h2>', '').strip()
            date = div.xpath('./div[1]').extract_first().replace('<div class="xxl-date">', '').replace('</div>', '')
            content = div.xpath('./div[2]').extract_first().replace('<div class="xxl-des">', '').replace('</div>', '')
            #important:下面实例化item对象
            item=FourthPersistentStoragePiplineItem()
            #important:通过中括号的方式访问item对象中的成员，且将解析到的字段赋值给item对象的成员
            item['title'] = title
            item['date'] = date
            item['content'] = content
            #important:将存储好数据的item对象提交给管道
            yield item #tips:将item提交给管道
            #tips:利用生成器可以节省内存，向管道提交了多次item

