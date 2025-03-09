# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class QichezhijiaPipeline:
    fp = None
    def open_spider(self,spider):
        self.fp=open('carinfo.csv','a+',encoding='utf-8',newline='')
        self.writer=csv.writer(self.fp)
        # 检查表头是否为空，如果是空的就写入表头!!
        if self.fp.tell() == 0:
            self.writer.writerow(['Car Title', 'Price', 'Licheng', 'Shijian', 'Leixing', 'Area', 'Guobiao'])
    def process_item(self, item, spider):
        car_title = item['car_title']
        price = item['price']
        licheng = item['licheng']
        shijian = item['shijian']
        leixing = item['leixing']
        area = item['area']
        guobiao = item['guobiao']
        self.writer.writerow([car_title, price, licheng, shijian, leixing, area, guobiao])
        print(item)
        return item
    def close_spider(self, spider):
        self.fp.close()
