import scrapy
from ..items import Zlsdemo2Item
import redis


class JianliSpider(scrapy.Spider):
    name = "jianli"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://sc.chinaz.com/jianli/"]
    conn = redis.Redis(host='127.0.0.1',port=6379)

    model_url = "https://sc.chinaz.com/jianli/index_%d.html"
    page_number = 2
    # slfdpn = int(input('请输入要爬取到第几页>>>')) #important:原来部署是不能这样设置交互的
    def parse(self, response):
        div_lst = response.xpath('//*[@id="container"]/div')
        for div in div_lst:
            title = div.xpath('./p/a/text()').extract_first()
            link = div.xpath('./p/a/@href').extract_first() #important:让详情页面的url充当数据指纹
            item = Zlsdemo2Item()
            item['title'] = title
            ex = self.conn.sadd('data_id',link)  #创建一个对象接收返回的redis插入的结果
            #tips:如果是1，说明是新数据，那么就进行管道操作将这个新的数据存储到redis数据库中
            if ex == 1:
                print('有最新的数据的更新，正在采集该数据')
                yield scrapy.Request(url=link,callback=self.parse_detail,meta={'item':item})
            # print(title,link)
            else:
                print('已有该数据，不再增加')
        if self.page_number<5:
            new_url = self.model_url %self.page_number
            self.page_number+=1
            #tips:重新发送请求
            yield scrapy.Request(url=new_url,callback=self.parse)
    def parse_detail(self,response):
        item = response.meta['item']
        download_url = response.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')
        item['download_url'] = download_url
        yield item
        # print(download_url)