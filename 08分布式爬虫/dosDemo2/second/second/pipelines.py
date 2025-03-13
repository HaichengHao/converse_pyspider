# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SecondPipeline:
    def close_spider(self,spider):
        spider.conn.close()
    def process_item(self, item, spider):
        print('success get item', item)
        return item
