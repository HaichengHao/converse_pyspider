# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from redis2 import Redis
import json


class Dosdemo1Pipeline:
    # def open_spider(self, spider):
    #     self.conn = Redis(host='localhost', port=6379, db=12, decode_responses=True)
    #
    # def close_spider(self, spider):
    #     self.conn.close()
    #
    # def process_item(self, item, spider):
    #     json_item = json.dumps(dict(item))
    #     self.conn.sadd("tianya:piplines:item", json_item)
    #     print(json.load(json_item))
    #     return item
    # def open_spider(self, spider):
    #     self.r = Redis(host='localhost', port=6379, db=11, decode_responses=True)

    # def close_spider(self, spider):
    #     self.r.close()

    def process_item(self, item, spider):
        print('success get item',item)
        # # 将item对象转换成字典
        # item_dict = ItemAdapter(item).asdict()
        #
        # # 将字典序列化为json字符串
        # item_json = json.dumps(item_dict)
        #
        # # tips:方案2利用redis存储数据
        # # 1. 引入redis库,将其存入db6,分布式数据库的好处就是这样，数据的判断和数据的存储可以放在两个不同的db
        #
        # # 2. 存入redis
        # # tips:要么用lpush存
        # self.r.lpush('zlsdemo3_spiderpipline', item_json)
        # # tips:要么用sadd存
        # # self.r.sadd("tianya:piplines:items", json.dumps(dict(item)))
        # print(json.loads(item_json))  # 这样看就行了，利用json.loads将json字符串数据加载为python字典即可
        return item
