# -*- coding: utf-8 -*-
import scrapy
from ..items import KuaiDaiLiItem


class KuaidailiIpSpider(scrapy.Spider):
    name = 'kuaidaili_ip'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/{}/']

    def start_requests(self):
        i = 1
        while True:
            yield scrapy.Request(
                url = self.start_urls[0].format(i),
                callback = self.parse
            )
            i += 1

    def parse(self, response):
        if response.text == "page error":
            print(response.text)
            return
        tr_list = response.xpath('//tbody/tr')
        for tr in tr_list:
            item = KuaiDaiLiItem()
            item["ip"] = tr.xpath('./td[@data-title="IP"]/text()').extract_first()
            item["port"] = tr.xpath('./td[@data-title="PORT"]/text()').extract_first()
            item["anonymity"] = tr.xpath('./td[@data-title="匿名度"]/text()').extract_first()
            item["http_type"] = tr.xpath('./td[@data-title="类型"]/text()').extract_first()
            item["location"] = tr.xpath('./td[@data-title="位置"]/text()').extract_first()
            item["response_speed_from_kuaidaili"] = tr.xpath('./td[@data-title="响应速度"]/text()').extract_first()
            item["verification_time_from_kuaidaili"] = tr.xpath('./td[@data-title="最后验证时间"]/text()').extract_first()
            yield item
