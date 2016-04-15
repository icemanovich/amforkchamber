# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmericanforkchamberItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DirectoryItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    address = scrapy.Field()
    link = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    info_link = scrapy.Field()

