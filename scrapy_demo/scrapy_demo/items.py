# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastTeacherItem(scrapy.Item):
    """
    Itcast 教师信息
    """
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
    description_ad = scrapy.Field()
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


class KuaiDaiLiItem(scrapy.Item):
    """
    快代理免费 ip
    """
    # ip
    ip = scrapy.Field()
    # port
    port = scrapy.Field()
    # 匿名度
    anonymity = scrapy.Field()
    # 类型
    http_type = scrapy.Field()
    # 位置
    location = scrapy.Field()
    # 快代理网站的响应速度
    response_speed_from_kuaidaili = scrapy.Field()
    # 快代理网站最后验证时间
    verification_time_from_kuaidaili = scrapy.Field()
    # 自测响应时间
    response_speed_from_me = scrapy.Field()
    # 最后自测时间
    verification_time_from_me = scrapy.Field()
