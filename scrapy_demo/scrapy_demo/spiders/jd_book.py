# -*- coding: utf-8 -*-
import scrapy
from ..items import JDBookItem
import json


class JdBookSpider(scrapy.Spider):
    name = 'jd_book'
    allowed_domains = ['jd.com', 'p.3.cn', 'ad.3.cn', 'rms.shop.jd.com', 'club.jd.com']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        """
        解析图书分类
        :param response:
        :return:
        """
        category1_list = response.xpath('//div[@class="mc"]//dt')

        for category1 in category1_list:
            item = JDBookItem()

            item["category1"] = category1.xpath('./a/text()').extract_first()
            item["category1_link"] = response.urljoin(category1.xpath('./a/@href').extract_first())

            category2_list = category1.xpath('./following-sibling::dd/em')
            for category2 in category2_list[0:1]:
                item["category2"] = category2.xpath('./a/text()').extract_first()
                item["category2_link"] = response.urljoin(category2.xpath('./a/@href').extract_first())

                yield scrapy.Request(
                    url = item["category2_link"],
                    callback = self.parse_book_list,
                    meta = {"item": item}
                )

    def parse_book_list(self, response):
        """
        解析图书列表页
        :param response:
        :return:
        """
        book_list = response.xpath('//li[@class="gl-item"]')
        # print(len(book_list))
        # print(response.meta["item"])
        item = response.meta["item"]
        for book in book_list:
            # 图书id
            book_id = book.xpath('.//@data-sku').extract_first()
            # 书名
            item["name"] = book.xpath('.//div[@class="p-name"]//em/text()').extract_first().strip()
            # 详情链接
            item["link"] = response.urljoin(book.xpath('.//div[@class="p-img"]//a/@href').extract_first())
            # 封面图链接
            item["image_link"] = response.urljoin(book.xpath('.//div[@class="p-img"]//img/@src '
                                                             '| '
                                                             './/div[@class="p-img"]//img/@data-lazy-img').extract_first())
            # 作者
            item["author"] = book.xpath('.//div[@class="p-bookdetails"]//span[@class="author_type_1"]//a/text()').extract_first()
            # 出版社
            item["publish"] = book.xpath('.//div[@class="p-bookdetails"]//span[@class="p-bi-store"]//a/text()').extract_first()
            # 出版时间
            item["publish_time"] = book.xpath('.//div[@class="p-bookdetails"]//span[@class="p-bi-date"]/text()').extract_first().strip()
            # 店铺ID
            shop_id = book.xpath('.//@jdzy_shop_id').extract_first()

            # 获取价格
            yield scrapy.Request(
                url = "https://p.3.cn/prices/mgets?skuIds=J_{}".format(book_id),
                callback = self.parse_price,
                meta = {"item": item, "book_id": book_id, "shop_id": shop_id}
            )

        # 下一页
        next_url = response.xpath('//a[@class="pn-next"]/@href').extract_first()
        if next_url is not None:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(
                url = next_url,
                callback = self.parse_book_list,
                meta = {"item": item}
            )

    def parse_price(self, response):
        """
        解析价格
        :param response:
        :return:
        """
        item = response.meta["item"]
        book_id = response.meta["book_id"]
        shop_id = response.meta["shop_id"]
        price_dict = json.loads(response.text, encoding = "utf-8")[0]
        if price_dict["id"] == "J_" + book_id:
            item["origin_price"] = price_dict["m"]
            item["real_price"] = price_dict["p"]
            # 获取店铺信息
            yield scrapy.Request(
                url = "https://rms.shop.jd.com/json/pop/shopInfo.action?ids={}".format(shop_id),
                callback = self.parse_shop,
                meta = {"item": item, "book_id": book_id, "shop_id": shop_id}
            )

    def parse_shop(self, response):
        """
        解析店铺信息
        :param response:
        :return:
        """
        item = response.meta["item"]
        book_id = response.meta["book_id"]
        shop_id = response.meta["shop_id"]
        shop_dict = json.loads(response.text, encoding = "utf-8")[0]
        # shop_dict = json.loads(response.body.decode(), encoding = "utf-8")[0]
        if shop_dict["venderId"] == shop_id:
            item["shop"] = shop_dict["name"]
            # 获取广告描述信息
            yield scrapy.Request(
                url = "https://ad.3.cn/ads/mgets?skuids=AD_{}".format(book_id),
                callback = self.parse_description_ad,
                meta = {"item": item, "book_id": book_id, "shop_id": shop_id}
            )

    def parse_description_ad(self, response):
        """
        解析广告描述信息
        :param response:
        :return:
        """
        item = response.meta["item"]
        book_id = response.meta["book_id"]
        description_dict = json.loads(response.text, encoding = "utf-8")[0]
        if description_dict["id"] == "AD_" + book_id:
            item["description_ad"] = description_dict["ad"]
            # 获取评论数量
            yield scrapy.Request(
                url = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds={}".format(book_id),
                callback = self.parse_comment,
                meta = {"item": item, "book_id": book_id}
            )

    def parse_comment(self, response):
        """
        解析评论
        :param response:
        :return:
        """
        item = response.meta["item"]
        book_id = response.meta["book_id"]
        comment_dict = json.loads(response.text, encoding = "utf-8")["CommentsCount"][0]
        if str(comment_dict["SkuId"]) == book_id:
            item["comment"] = comment_dict["CommentCount"]
            yield item
