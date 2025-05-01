# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline


# 新建imgpipeline
class ImagePipeline(ImagesPipeline):
    def get_media_requests(
            self, item, info
    ):
        img_src = item['pic_url']
        yield scrapy.Request(url=img_src, meta={'title': item['title']})

    def file_path(
            self,
            request,
            response=None,
            info=None,
            *,
            item: None,
    ):
        title = item['title'] + '.jpg'
        print(f'{title}保存成功')
        return title

    def item_completed(
            self, results, item, info
    ):
        return item

# class DeskPipeline:
#     def process_item(self, item, spider):
#         return item
