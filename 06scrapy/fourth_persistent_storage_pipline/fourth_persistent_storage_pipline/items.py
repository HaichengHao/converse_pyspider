# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FourthPersistentStoragePiplineItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()

    # important:爬取的字段有那些，这里就需要写哪些字段,注意不需要一致,但是一致的话可读性好
