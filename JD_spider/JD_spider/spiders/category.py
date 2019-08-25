# -*- coding: utf-8 -*-
import scrapy
import json


class CategorySpider(scrapy.Spider):
    name = 'category'
    allowed_domains = ['dc.3.cn']
    start_urls = ['https://dc.3.cn/category/get']

    def parse(self, response):
        with open("category1.json", "wb") as file:
            file.write(response.body)
