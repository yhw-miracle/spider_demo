# -*- coding: utf-8 -*-
import scrapy
from ..items import ItcastTeacherItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        teacher_list = response.xpath('//div[@class="tea_con"]//li')

        for teacher in teacher_list:
            teacher_item = ItcastTeacherItem()
            teacher_item["name"] = teacher.xpath('./div[@class="li_txt"]/h3').extract_first()
            teacher_item["level"] = teacher.xpath('./div[@class="li_txt"]/h4').extract_first()
            teacher_item["description"] = teacher.xpath('./div[@class="li_txt"]/p').extract_first()
            # teacher_item["image"] = "http://www.itcast.cn" + teacher.xpath('./div[@class="li_img"]/img/@data-original').extract_first()
            teacher_item["image"] = response.urljoin(teacher.xpath('./div[@class="li_img"]/img/@data-original').extract_first())

            """
            <img data-original="/images/teacher/2018221215222100.jpg"> 
            <img data-original="/images/teacher/20154825094803449.jpg" src="/images/teacher/20154825094803449.jpg" style="display: inline;" class="">
            """
            # print(teacher.xpath('./div[@class="li_img"]/img/@data-original').extract_first())

            yield teacher_item
