import scrapy
from urllib.parse import urljoin
from scrapy.linkextractors import LinkExtractor #导入链接提取器

class CarsSpider(scrapy.Spider):
    name = "cars"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.che168.com/zhengzhou/dazhong/#pvareaid=108402#listfilterstart"]

    def parse(self, response):
        # hrefs = response.xpath('//ul[@class="viewlist_ul"]//li[position()<57]/a/@href').extract()
        # for href in hrefs:
        #     # print(href)
        #     yield scrapy.Request(
        #         url=urljoin(response.url, href),
        #         callback=self.parse_detail
        #     )
        #scrapy 还提供了连接提取器这个东西,当然按照顺序之前已经在crawl spider中写过了这里作为非crawl spider的引申
        le = LinkExtractor(restrict_xpaths=('//ul[@class="viewlist_ul"]//li[position()<57]/a',))
        #important:可查看LinkExtractor的初始化方法,其对传入的数据有相应的要求,传的restrict_xpaths是个元组，记得元组的特性
        #  单元素的元组需要加上逗号
        links = le.extract_links(response) #tips: 从response响应对象中提取链接对象
        '''
                 [Link(url='https://www.che168.com/dealer/106700/53389619.html?pvareaid=100519&userpid=410000&userc
        id=410100&offertype=850&offertag=0&activitycartype=0&fromsxmlist=0&platfrom=36', text='            跨年焕新
                                                               揽境 2022款 380TSI 四驱豪华佳境版Pro 6座            10.01
        万公里／2022-09／郑州／12年黄金会员            17.58万36.57万                      ', fragment='', nofollow=False
        ), Link(url='https://www.che168.com/dealer/106700/53435413.html?pvareaid=100519&userpid=410000&usercid=410100&off
        ertype=850&offertag=0&activitycartype=0&fromsxmlist=0&platfrom=36', text='            跨年焕新
                                                  探岳GTE插电混动 2023款 280TSI 豪华Plus进阶版            0.1万公里／2024
        -08／郑州／12年黄金会员            14.58万准新车原厂质保26.37万                      ', fragment='', nofollow=Fal
        se), .... ]  #important: 注意，这就是提取器返回的列表，是一个link对象，里面是键值对组成的列表
        '''
        # print(links) #tips:打印查看所有的链接对象
        for link in links:
            # print(link.text.replace(" ","").strip(),link.url) #tips:提取出a标签中的文本和href
            yield scrapy.Request(
                url=link.url, #有重复的url没关系,因为调度器中的过滤器会将相同的请求链接过滤掉只保留一份
                # dont_filter=True, #不过滤，直接交给队列，直接发送请求
                callback=self.parse_detail
            )

        # tips:开始分页
        # 创建分页a标签的链接提取器
        page_le = LinkExtractor(restrict_xpaths=('//div[@id="listpagination"]/a[position()>1]',))
        page_links = page_le.extract_links(response)  #提取分页url
        for page_link in page_links:
            print(page_link.url) #拿到了分页的url
            yield scrapy.Request(url=page_link.url,callback=self.parse)
            #tips:这样写会有非常大的问题，因为每一页都会有上一页的链接，它就会重复请求链接



    def parse_detail(self, response):
        print(response.url)

#         timestamp 1'03''15'''
