# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json


class ItcastTeacherPipeline(object):
    def __init__(self):
        if "data" not in os.listdir("."):
            os.makedirs("data")
        self.file = None

    def open_spider(self, spider):
        if spider.name == "itcast":
            self.file = open("./data/teacher.json", "a", encoding = "utf-8")

    def process_item(self, item, spider):
        if spider.name == "itcast":
            item_to_str = json.dumps(dict(item), ensure_ascii = False)
            self.file.write(item_to_str + ",\n")
        return item

    def close_spider(self, spider):
        if spider.name == "itcast":
            self.file.close()


class DoubanMoviePipeline(object):
    def __init__(self):
        if "data" not in os.listdir("."):
            os.makedirs("data")
        self.file = None

    def open_spider(self, spider):
        if spider.name == "douban_movie":
            self.file = open("./data/movie1.json", "a", encoding = "utf-8")

    def process_item(self, item, spider):
        if spider.name == "douban_movie":
            item_to_str = json.dumps(dict(item), ensure_ascii = False)
            self.file.write(item_to_str + ",\n")
        return item

    def close_spider(self, spider):
        if spider.name == "douban_movie":
            self.file.close()


class JDBookPipeline(object):
    def __init__(self):
        if "data" not in os.listdir("."):
            os.makedirs("data")
        self.file = None

    def open_spider(self, spider):
        if spider.name == "jd_book":
            self.file = open("./data/JDBook_category.json", "a", encoding = "utf-8")

    def process_item(self, item, spider):
        if spider.name == "jd_book":
            item_to_str = json.dumps(dict(item), ensure_ascii = False)
            self.file.write(item_to_str + ",\n")
        return item

    def close_spider(self, spider):
        if spider.name == "jd_book":
            self.file.close()
