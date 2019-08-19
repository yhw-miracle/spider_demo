# -*- coding: utf-8 -*-
import scrapy
from ..items import MyBlogItem


class MyblogSpider(scrapy.Spider):
    name = 'myblog'
    allowed_domains = ['yhw-miracle.cn']
    start_urls = ['https://yhw-miracle.cn/']

    def parse(self, response):
        post_list = response.xpath('//li')
        for post in post_list:
            item = MyBlogItem()

            item["title"] = post.xpath('.//a/text()').extract_first()

            item["title_url"] = response.urljoin(post.xpath('.//a/@href').extract_first())

            author = post.xpath('.//div[@class="author"]/text()').extract_first()
            author = author.strip().split(" ")[0]
            item["author"] = author

            post_date = post.xpath('.//div[@class="author"]//time/text()').extract_first()
            post_date = post_date.strip()
            item["post_date"] = post_date

            item["tags"] = post.xpath('.//div[@class="tags"]/span/text()').extract()
            item["category"] = post.xpath('.//div[@class="categories"]/span/text()').extract_first()
            yield item

        next_url = response.urljoin(response.xpath('//div[@class ="pagination"]/a[@class="page-item"]/@href').extract()[-1])
        if next_url is not None:
            yield scrapy.Request(
                url = next_url,
                callback = self.parse
            )
