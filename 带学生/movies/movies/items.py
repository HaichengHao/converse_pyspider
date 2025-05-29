# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    score = scrapy.Field()
    country_area =scrapy.Field()
    time_length = scrapy.Field()
    sysj = scrapy.Field()
