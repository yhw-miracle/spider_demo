# -*- coding: utf-8 -*-
import scrapy
from ..items import JDBookItem


class JdBookSpider(scrapy.Spider):
    name = 'jd_book'
    allowed_domains = ['jd.com']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        category1_list = response.xpath('//div[@class="mc"]//dt')

        for category1 in category1_list[0:1]:
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
            item["image_link"] = response.urljoin(book.xpath('.//div[@class="p-img"]//img/@src').extract_first())
            book.xpath('.//div[@class="p-name"]//a/@href').extract_first()
            book.xpath('.//div[@class="p-name"]//em/text()').extract_first()
            book.xpath('.//div[@class="p-name"]//i[@class="promo-words"]/text()').extract_first()
            # 待续
