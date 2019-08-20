# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MyBlogItem


class MyblogCrawlSpider(CrawlSpider):
    name = 'myblog_crawl'
    allowed_domains = ['yhw-miracle.cn']
    start_urls = ['http://yhw-miracle.cn/']

    rules = (
        Rule(LinkExtractor(allow = r'/page/\d+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
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
            print(item)
        # return item
