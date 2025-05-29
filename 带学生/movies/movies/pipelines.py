# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import csv
class MoviesPipeline:
    fp = None
    def open_spider(self,spider):
        self.fp = open('movieinfo.csv','a+',encoding='utf-8',newline='')
        self.writer = csv.writer(self.fp)
        if self.fp.tell() == 0:
            self.writer.writerow(['电影名称','评分','国家/地区','时长','上映时间'])


    def process_item(self, item, spider):
        name = item['name']
        score = item['score']
        country_area = item['country_area']
        time_length = item['time_length']
        sysj = item['sysj']
        self.writer.writerow([name,score,country_area,time_length,sysj])
        return item
    def close_item(self,spider):
        self.fp.close()