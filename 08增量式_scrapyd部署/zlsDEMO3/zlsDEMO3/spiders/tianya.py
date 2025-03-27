import scrapy
from urllib.parse import urljoin
from redis import Redis
from ..items import Zlsdemo3Item


# abst:demo3和之前的demo1,demo2有相似之处，但是也有不同的写法，比较难理解,譬如初始化Redis对象的方法
# important: 增量式解决的就是相同内容的问题,也就是去重，有重复的数据产生就对其去除
# 方法1：使用python的集合进行去重>>但是这样效率很低，且存储起来很麻烦
# 方法2: 使用redis的集合进行去重
# tips: 放法2的两个方案
#  1存储url，作为数据指纹来判断是否该条数据已经被抓取 优点是简单，快捷方便，缺点:如果url内部进行了更新会损失数据
#  2存储数据,优点是准确性高，但是缺点是如果数据集非常庞大，那么对于reids而言是不利的(这个操作的话进入到piplines.py里进行)

# conn = Redis(
#     host="localhost",
#     port=6379,
#     db=15,
# )


class TianyaSpider(scrapy.Spider):
    name = "tianya"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://xintianya.net/"]
    model_url = 'https://xintianya.net/index-%d.htm'
    page_number = 2  # tips:定义类属性page_number,用于我们进行多页爬取的页数的初始化

    # tips:重写初始化方法，让redis实例在爬虫开始时就调用
    def __init__(self, name=None, **kwargs):
        self.redis = Redis(
            host="localhost",
            port=6379,
            db=9,
        )
        # 让父类初始化
        super(TianyaSpider, self).__init__(name, **kwargs)

    def parse(self, response):
        urls = response.xpath(
            '//div[@class="card card-threadlist"]//ul/li/div[@class="media-body"]/div/a/@href').extract()
        for url in urls:
            # print(url)
            detail_url = urljoin(self.start_urls[0], url)
            # tips:进入详情页的前提是:之前这个详情页的url没有被存储过，换句话说这是个新的才存，旧的不存
            #  1方案1:往集合里存，存进去就是新的，存不进去就是老的
            # result = self.redis.sadd("tianya:ty:detail:url",detail_url)
            # if result: #如果插入成功，说明数据是新的数据
            # #     那就插入新的数据
            #     print('get new url, the data will be add to redis')
            #     yield scrapy.Request(url=detail_url, callback=self.parse_detail)
            # else:
            #     print('this url have been saved,continue')

            # tips 其实我们只是想redis来高效的对url进行判定是否是新的
            # 但是这样有一个问题,redis并不会因为spider程序被迫停止就会停止，它仍然会进行请求
            # QUIZ:如何解决这个问题
            # answer :利用sismember来进行判断即可，不进行数据的插入,和刚才的逻辑刚好是反的
            # result = conn.sismember("tianya:ty:detail:url",detail_url)
            result = self.redis.sismember("tianya:ty:detail:url", detail_url)
            if result:  # 如果已经存在了，那就不存
                print('this url have been saved,will take no operation')
            else:  # 如果不存在那就往redis里存
                print('get new url ,the data will be add to redis')
                # 往里存
                # QUIZ:但是存的话应该写哪里合适呢?
                # answer:放到parse_detail里边，因为存在的话就不调用parse_detail
                #  或者像之前那样写到pipline里(推荐)
                yield scrapy.Request(url=detail_url, callback=self.parse_detail)

        # tips:可以继续考虑爬取下一页
        if self.page_number < 6:  # 只爬前6页当个例子看
            new_url = self.model_url % self.page_number
            self.page_number += 1
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        usrname = response.xpath('//a[@class="text-muted"]/b/text()').extract_first()
        title = response.xpath('//span[@class="break-all"]/text()').extract_first().strip()
        # print(f'username:{usrname},title:{title}')
        # tips:实例化item对象
        item = Zlsdemo3Item()
        item['usrname'] = usrname
        item['title'] = title
        self.redis.sadd("tianya:ty:detail:url", response.url)
        yield item

#         important:想验证是否成功可以运行两遍看看，第二遍就会抛出数据已经存储过
