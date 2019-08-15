# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastTeacherItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    level = scrapy.Field()
    description = scrapy.Field()
    image = scrapy.Field()


class DoubanMovieTop250Item(scrapy.Item):
    """
    豆瓣电影排行 250
    """
    name = scrapy.Field()
    other_name = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()
    info = scrapy.Field()
    rating_num = scrapy.Field()
    rating_people = scrapy.Field()
    quote = scrapy.Field()
