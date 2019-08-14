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
        self.file = open("./data/teacher.json", "a", encoding = "utf-8")

    def process_item(self, item, spider):
        item_to_str = json.dumps(dict(item), ensure_ascii = False)
        self.file.write(item_to_str + ",\n")
        return item

    def __del__(self):
        self.file.close()
