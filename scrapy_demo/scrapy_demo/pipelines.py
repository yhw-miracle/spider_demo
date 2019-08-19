# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
from pymongo import MongoClient


class ItcastTeacherPipeline(object):
    """
    Itcast 教师信息存储文件管道
    """
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
    """
    豆瓣排行 250 电影信息存储文件管道
    """
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
    """
    京东图书存储文件管道
    """
    def __init__(self):
        if "data" not in os.listdir("."):
            os.makedirs("data")
        self.file = None

    def open_spider(self, spider):
        if spider.name == "jd_book":
            # self.file = open("./data/JDBook_category.json", "a", encoding = "utf-8")
            self.file = open("./data/JDBook_book.json", "a", encoding = "utf-8")

    def process_item(self, item, spider):
        if spider.name == "jd_book":
            item_to_str = json.dumps(dict(item), ensure_ascii = False)
            self.file.write(item_to_str + ",\n")
        return item

    def close_spider(self, spider):
        if spider.name == "jd_book":
            self.file.close()


class JDBookToMongoDBPipeline(object):
    """
    京东图书信息存储 MongoDB 数据库管道
    """
    def __init__(self):
        self.mongo_client = None

    def open_spider(self, spider):
        if spider.name == "jd_book":
            self.mongo_client = MongoClient("mongodb://root:q@192.168.159.132:27017")

    def process_item(self, item, spider):
        if spider.name == "jd_book":
            book_collection = self.mongo_client["JD"]["book"]
            book_collection.insert(dict(item))
        return item

    def close_spider(self, spider):
        if spider.name == "jd_book":
            self.mongo_client.close()


class KuaiDaiLiItem(object):
    def __init__(self):
        if "data" not in os.listdir("."):
            os.makedirs("data")
        self.file = None
        self.mongodb_client = None

    def open_spider(self, spider):
        if spider.name == "kuaidaili_ip":
            self.file = open("./data/kuaidaili.json", "a", encoding = "utf-8")
            self.mongodb_client = MongoClient("mongodb://root:q@192.168.159.132:27017")

    def process_item(self, item, spider):
        if spider.name == "kuaidaili_ip":
            item_to_dict = dict(item)
            self.file.write(json.dumps(item_to_dict, ensure_ascii = False) + "\n")
            kuaidaili_collection = self.mongodb_client["proxies"]["kuaidaili"]
            kuaidaili_collection.insert(item_to_dict)
        return item

    def close_spider(self, spider):
        if spider.name == "kuaidaili_ip":
            self.file.close()
            self.mongodb_client.close()


class MyBlogItem(object):
    """
    yhw-miracle's blog 文章数据管道
    """
    def __init__(self):
        if "data" not in os.listdir("."):
            os.makedirs("data")
        self.file = None
        self.mongodb_client = None

    def open_spider(self, spider):
        if spider.name == "myblog":
            self.file = open("./data/myblog.json", "a", encoding = "utf-8")
            self.mongodb_client = MongoClient("mongodb://root:q@192.168.159.132:27017")

    def process_item(self, item, spider):
        if spider.name == "myblog":
            item_to_dict = dict(item)
            self.file.write(json.dumps(item_to_dict, ensure_ascii = False) + "\n")
            myblog_collection = self.mongodb_client["myblog"]["post_list"]
            myblog_collection.insert(item_to_dict)
        return item

    def close_spider(self, spider):
        if spider.name == "myblog":
            self.file.close()
            self.mongodb_client.close()


class Position163Item(object):
    """
    网易招聘信息数据管道
    """
    def __init__(self):
        if "data" not in os.listdir("."):
            os.makedirs("data")
        self.file = None
        self.mongodb_client = None

    def open_spider(self, spider):
        if spider.name == "hr_163":
            self.file = open("./data/position163.json", "a", encoding = "utf-8")
            self.mongodb_client = MongoClient("mongodb://root:q@192.168.159.132:27017")

    def process_item(self, item, spider):
        if spider.name == "hr_163":
            item_to_dict = dict(item)
            self.file.write(json.dumps(item_to_dict, ensure_ascii = False) + "\n")
            position_collection = self.mongodb_client["position"]["wy163"]
            position_collection.insert(item_to_dict)
        return item

    def close_spider(self, spider):
        if spider.name == "hr_163":
            self.file.close()
            self.mongodb_client.close()
