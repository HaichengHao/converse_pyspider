# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


#
# class WangyiproPipeline:
#     def process_item(self, item, spider):
#         print(item)
#         return item

# 高级
from aip import AipNlp


class WangyiproPipeline:
    def open_spider(self,spider):
        """ 你的 APPID AK SK """
        APP_ID = '117587424'
        API_KEY = 'Zwi5fEC9nH3P32v70SVooMJ8'
        SECRET_KEY = 'LoWxISDCgkTkAeX6PDCMep7768gMUiXr'
        self.client = AipNlp(APP_ID, API_KEY, SECRET_KEY) #important:只需要在spider开启时创立一次

    def process_item(self, item, spider):
        title = item['title']
        title = title.encode('utf-8').decode('utf-8')
        content = item['content']
        result = self.client.topic(title, content)
        class_new = result['item']['lv2_tag_list']
        # print(class_new)
        for class_ in class_new:
            print(class_['tag'])

        return item
