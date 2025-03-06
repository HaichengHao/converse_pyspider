# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter

from scrapy.pipelines.images import ImagesPipeline
class ImgproPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     print(item)
    #     return item
    def get_media_requests(
        self, item, info
    ):
        img_src = item['img_src']
        # important:请求传参，将item中的图片名称传递给file_path
        # important:meta会将自身传递给file_path
        yield scrapy.Request(url=img_src,meta={'title':item['title']}) #tips:用的还是请求传参
    # important:注意，在settings.py里声明一个IMAGES_STORE='指定的路径'
    def file_path(
        self,
        request,
        response = None,
        info = None,
        *,
        item= None,
    ):
        # tips:返回图片的名称
        # important:接收请求传参过来的数据
        title = request.meta['title']+'.jpg'
        print(f'{title}保存成功')
        return title
    def item_completed(
        self, results, item, info
    ):
        return item
