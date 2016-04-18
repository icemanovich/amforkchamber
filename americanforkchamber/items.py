# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DirectoryItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    author_job = scrapy.Field()
    address = scrapy.Field()
    link = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    address_book_link = scrapy.Field()

