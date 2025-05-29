# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import csv
class DuanziPipeline:
    fp = None
    def open_spider(self,spider):
        self.fp = open('Data.csv','a+',encoding='utf-8',newline='')
        self.writer = csv.writer(self.fp)
        # 判读表头是否为空，如果为空就写入表头
        if self.fp.tell() == 0:
            self.writer.writerow(['段子内容'])
        print('csv文件创建成功')
    def process_item(self,item,spider):
        content = item['content']
        self.writer.writerow([content,])
        return item
    def close_spider(self,spider):
        self.fp.close()