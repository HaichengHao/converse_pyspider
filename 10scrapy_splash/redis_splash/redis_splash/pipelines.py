# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

from itemadapter import ItemAdapter


class NewsPipeline:
    fp = None
    def open_spider(self,spider):
        self.fp = open('news.csv','a+',encoding='utf-8',newline='')
        self.writer = csv.writer(self.fp)
        if self.fp.tell() == 0:
            self.writer.writerow(['标题','链接'])
    def process_item(self, item, spider):
        title = item['title']
        href = item['href']
        self.writer.writerow([title,href])
        return item
    def close_spider(self,spider):
        self.fp.close()
