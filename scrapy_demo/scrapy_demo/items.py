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


class JDBookItem(scrapy.Item):
    """
    京东图书信息
    """
    # 书名
    name = scrapy.Field()
    # 详情链接
    link = scrapy.Field()
    # 封面图
    # image = scrapy.Field()
    # 封面图链接
    image_link = scrapy.Field()
    # 描述信息
    description = scrapy.Field()
    # 原价
    origin_price = scrapy.Field()
    # 实际销售价格
    real_price = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 出版社
    publish = scrapy.Field()
    # 出版时间
    publish_time = scrapy.Field()
    # 电子书价格，若没有电子书，该值为None
    e_books_price = scrapy.Field()
    # 评价数
    comment = scrapy.Field()
    # 售卖店铺
    shop = scrapy.Field()
    # 一级分类
    category1 = scrapy.Field()
    # 一级分类链接
    category1_link = scrapy.Field()
    # 二级分类
    category2 = scrapy.Field()
    # 二级分类链接
    category2_link = scrapy.Field()
