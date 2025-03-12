# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from redis import Redis
import json
# important:记得看踩坑笔记!!!!
class Zlsdemo3Pipeline:
    def open_spider(self,spider):
        self.r = Redis(host='localhost', port=6379, db=7, decode_responses=True)
    def close_spider(self,spider):
        self.r.close()
    def process_item(self, item, spider):

        # 将item对象转换成字典
        item_dict = ItemAdapter(item).asdict()

        # 将字典序列化为json字符串
        item_json = json.dumps(item_dict)

        #tips:方案2利用redis存储数据
        # 1. 引入redis库,将其存入db6,分布式数据库的好处就是这样，数据的判断和数据的存储可以放在两个不同的db


        # 2. 存入redis
        # tips:要么用lpush存
        # r.lpush('zlsdemo3', item_json)
        # tips:要么用sadd存
        self.r.sadd("tianya:piplines:items",json.dumps(dict(item)))
        # print(json.loads(item_json))
        # print(json.dumps(json.loads(item_json), indent=4, ensure_ascii=False))
        print(json.loads(item_json)) #这样看就行了，利用json.loads将json字符串数据加载为python字典即可
        return item


#         或者这样写在一个库里
#         print(json.dumps(dict(item)))
#         r = self.redis.sadd("tianya:pipline:items",json.dumps(dict(item)))
#         if r:
#             print('data_saved',item['title'])
#         else:
#             print('data_exists',item['title'])
#         return item
#     def open_spider(self,spider):
#         self.redis = Redis(db=6)
#     def close_spider(self,spider):
#         self.redis.close()

