# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import pymongo


class MongoPipeLine(object):
    def __init__(self, db_host, db_port, db_name, db_collection='subjects'):
        self.mongo_host = db_host
        self.mongo_port = db_port
        self.mongo_db = db_name
        self.collection = db_collection
        self.client = None
        self.db = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            db_host=crawler.settings.get('DB_HOST', 'localhost'),
            db_port=crawler.settings.get('DB_PORT', '27017'),
            db_name=crawler.settings.get('DB_NAME', 'amforkchamber'),
            db_collection=crawler.settings.get('MONGO_COLLECTION', 'items'),
        )

    def open_spider(self, spider):
        if not self.mongo_host:
            raise Exception

        self.client = pymongo.MongoClient(self.mongo_host)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        """
        Filter duplicated items and save it into DB
        """
        if self.db[self.collection].find({'link': item['link']}).count():
            raise DropItem("Duplicate item {0}".format(item['link']))
        else:
            self.db[self.collection].insert(dict(item))
        return item


class CsvPipeLine(object):
    def process_item(self, item, spider):
        return item
