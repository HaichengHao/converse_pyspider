# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Zlsdemo1Pipeline:
    def process_item(self, item, spider):
        conn = spider.conn #important:拿到爬虫文件中的链接对象
        # dic={
        #     'title':item['title'],
        #     'content':item['content']
        # }
        # conn.lpush('duanzilib',dic) #important:如果Redis版本高于2.10.6可以使用注释掉的方法，即将数据转换为json格式
        # 或者加一个 item = str(item) 将列表转化为字符串存入字典当中
        conn.lpush('duanzilib',item) #tips:将item存到duanzilib名字的列表当中去
        #important:注意redis模块一定要是2.10.6版本的，只有这样才能够将字典用lpush存进去
        # next_step:去settings.py中开启管道
        return item
