import scrapy
from ..items import DeepproItem

class DpproSpider(scrapy.Spider):
    name = "dppro"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://ypk.39.net/pifu/p1/"]
    page_number = 2
    model_url = f"https://ypk.39.net/pifu/p{page_number}/"

    # important:新写一个详情页面的数据获取规则
    def parse_moreinfo(self,response):
        meta = response.meta #tips:接收请求传参过来的meta
        item = meta['item'] #tips:我们要的是meta字典当中的item，所以这样就接收到了
        power = response.xpath('//ul[@class="drug-layout-r-ul"]/li[1]/div/p').extract_first().split('>')[1].split('<')[0]
        # important:这样就可以向管道提交了
        item['power'] = power
        # print(power)
        yield item

    def parse(self, response):
        li_lst = response.xpath('//ul[@class="drugs-ul"]/li')
        for li in li_lst:
            name = li.xpath('./a/@title').extract_first()
            moreinfo_href = li.xpath('./a/@href').extract_first()
            # print(name)
            # print(moreinfo_href)
            # tips:实例化item对象
            item = DeepproItem()
            item['name'] = name
            # important:手动生成对于详情页面的请求
            yield scrapy.Request(meta={'item':item}, url=moreinfo_href, callback=self.parse_moreinfo)  # important:对详情页的url发起请求
        #important:一定注意这里的缩进
        if self.page_number < 10:
            new_url = self.model_url
            self.page_number+=1
            scrapy.Request(new_url,callback=self.parse)
# important:我们发现表层页面和深层页面输出的数据并不是一一对应的且现在我们需要进行持久化存储，当然不能将item实例化为全局变量
#  所以我们现在需要做的是进行请求传参

#QUIZ:现在需要解决的问题:如何把parse中的item对象传递给parse_moreinfo?
#answer: 在生成请求的时候将scrapy.Request()中设置meta，参数meta可以将自身的字典传递给callback指定的回调函数
#  所以我们只需要将item对象作为参数传递给指定的callback函数即刚好需要它的parse_moreinfo
#  且parse_moreinfo需要接收这个meta,只需要写上response.meta即可



# summary:本节重点就是请求传参以及编写对新的页面的链接的爬取方法，当然最重要的就是meta传参!!
