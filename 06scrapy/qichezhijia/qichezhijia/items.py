# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QichezhijiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    car_title = scrapy.Field()
    price = scrapy.Field()
    licheng = scrapy.Field()
    shijian = scrapy.Field()
    leixing = scrapy.Field()
    area = scrapy.Field()
    guobiao = scrapy.Field()
