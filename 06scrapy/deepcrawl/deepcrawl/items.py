# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DeepcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    booktitle = scrapy.Field()
    author = scrapy.Field()
    category = scrapy.Field()
    abstract = scrapy.Field()
    img_src = scrapy.Field()

