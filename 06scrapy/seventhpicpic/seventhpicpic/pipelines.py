# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# tips:导入我们下载二进制数据需要用到的包ImagePipline
# important:原始的pipline我们是不用的，我们需要定义一个新的pipline用来下载图片数据

import requests
import scrapy
from itemadapter import ItemAdapter

# tips:从scrapy的管道类中导入一个ImagesPipline 其除了保存图片数据外也可以保存其它二进制数据
from scrapy.pipelines.images import ImagesPipeline


class mediaPipline(ImagesPipeline):  # important:自己定义的管道类一定要继承与父类
    # important: 重写三个父类的方法来完成图片二进制数据的请求和持久化存储
    # tips:可以根据图片地址，对其进行请求，获取图片数据
    #  参数item:就是接收到的item对象
    def get_media_requests(self, item, info):  # tips:可以对图片数据的地址对图片数据进行请求获取图片数据
        img_src = item['img_src']  # tips:先拿到图片地址
        yield scrapy.Request(img_src)  # important:生成一个scrapy内置的request请求

    # 指定图片的存储路径，(important:只需要返回图片存储的名称即可)
    def file_path(self, request, response=None, info=None, *, item=None, ):
        # imgName = item['book_title']
        imgName = request.url.split('/')[-1]  # tips:利用split将图片链接进行分割，只取最后一个来作为图片的名称
        print(f'{imgName}下载成功')
        return imgName

    # 如果没有下一步管道类，例如没有存储到数据库操作，那这一步就不写↓
    def item_completed(
            self, results, item, info
    ):
        return item  # important:可以将当前管道类接收到的item对象传递给下一个管道类
    # tips:如果没印象可以去看项目5
