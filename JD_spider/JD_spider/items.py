# -*- coding: utf-8 -*-
# @Time: 2019/8/24 20:07
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo.py
# @Software: PyCharm
# use scrapy

import scrapy


class JdGoodsCategoryItem(scrapy.Item):
    """
    京东商品分类数据
    """

    # 一级分类
    category1_name = scrapy.Field()
    # 一级分类链接
    category1_url = scrapy.Field()
    # 二级分类
    category2_name = scrapy.Field()
    # 二级分类链接
    category2_url = scrapy.Field()
    # 三级分类
    category3_name = scrapy.Field()
    # 三级分类链接
    category3_url = scrapy.Field()


class JdGoodsItem(scrapy.Item):
    """
    京东商品数据
    """

    # 商品所属分类
    category3 = scrapy.Field()
    # 商品id
    sku_id = scrapy.Field()
    # 商品名称
    name = scrapy.Field()
    # 商品图片链接
    image_url = scrapy.Field()
    # 商品信息
    info = scrapy.Field()
    # 商品价格
    price = scrapy.Field()
    # 商品选项
    option = scrapy.Field()
    # 商品店铺
    shop = scrapy.Field()
    # 商品促销信息
    advertisement = scrapy.Field()
    # 商品评论量
    comment = scrapy.Field()
