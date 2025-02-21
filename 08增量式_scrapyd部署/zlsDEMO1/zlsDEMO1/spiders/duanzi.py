import scrapy
import hashlib #important:导入生成数据指纹的模块

import redis
from ..items import Zlsdemo1Item

class DuanziSpider(scrapy.Spider):
    name = "duanzi"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.wogif.com/duanzi/"]
    # tips:创建Redis的链接对象
    conn = redis.Redis(host='127.0.0.1',port=6379)
    def parse(self, response):
        div_lst = response.xpath('/html/body/div[1]/div[2]/div/a/div')
        for div in div_lst:
            title = div.xpath('./h2').extract_first().replace('<h2>', '').replace('</h2>', '').strip()
            content = div.xpath('./div[@class="xxl-des"]').extract_first().replace('<div class="xxl-date">', '').replace('</div>', '')
            # print(title,content)
            #important:不需要存储数据本身而是存储数据指纹(即数据的唯一标识)
            all_data = title+content
            #

            # important:将哈希值作为数据的指纹，实现增量式爬取，有新数据就添加，没新数据就不添加，这就是增量式
            # # tips:生成该数据的数据指纹，数据指纹需要是唯一的表示数据即可，譬如一个网页的图片的每个图片的链接都不相同，那便可以将其作为数据指纹
            md5 = hashlib.md5() #important: 构建生成指纹的工具，可以将数据转换为32位或64位的二进制唯一标识
            md5.update(all_data.encode('utf-8')) #tips:对数据进行编码
            data_id = md5.hexdigest()
            ex = self.conn.sadd('data_id',data_id) #tips:往集合中插入数据指纹
            if ex == 1: #如果执行成功(数据指纹在集合中不存在，则新增)
                print('有最新数据的更新，正在爬取')
                item = Zlsdemo1Item()
                item['title'] = title
                item['content'] = content
                yield item   #next_step:将数据存储到redis中,到管道文件中去操作

            else: #数据指纹在集合中存在(即已经有这条指纹了)
                print('暂无最新数据更新，请等待')



            print(data_id)
