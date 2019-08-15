# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanMovieTop250Item


class DoubanMovieSpider(scrapy.Spider):
    name = 'douban_movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_li_list = response.xpath('//ol[@class="grid_view"]/li')

        for movie in movie_li_list:
            item = DoubanMovieTop250Item()

            item["name"] = movie.xpath('.//div[@class="info"]//span[@class="title"]/text()').extract_first()
            item["other_name"] = movie.xpath('.//div[@class="info"]//span[@class="other"]/text()').extract_first().strip()
            item["image"] = movie.xpath('.//div[@class="pic"]//img/@src').extract_first()
            item["link"] = movie.xpath('.//div[@class="pic"]//a/@href').extract_first()
            item["info"] = movie.xpath('.//div[@class="bd"]//p[1]/text()').extract_first().strip()
            item["rating_num"] = movie.xpath('.//div[@class="star"]//span[@class="rating_num"]/text()').extract_first()
            item["rating_people"] = movie.xpath('.//div[@class="star"]//span[last()]/text()').extract_first()
            item["quote"] = movie.xpath('.//p[@class="quote"]/span/text()').extract_first()

            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract_first()
        if next_url:
            yield scrapy.Request(
                url = response.urljoin(next_url),
                callback = self.parse
            )
