# -*- coding: utf-8 -*-
import scrapy
from ..items import Position163Item


class Hr163Spider(scrapy.Spider):
    name = 'hr_163'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/position/list.do']

    def parse(self, response):
        position_list = response.xpath('//table[@class="position-tb"]/tbody/tr')
        for index, position in enumerate(position_list):
            if index % 2 == 0:
                item = Position163Item()
                item["position_name"] = position.xpath('./td[1]/a/text()').extract_first()
                # 职位链接
                item["position_url"] = response.urljoin(position.xpath('./td[1]/a/@href').extract_first())
                # 所属部门
                item["department"] = position.xpath('./td[2]/text()').extract_first()
                # 职位类别
                item["position_type"] = position.xpath('./td[3]/text()').extract_first()
                # 工作类型
                item["work_type"] = position.xpath('./td[4]/text()').extract_first()
                # 工作地点
                item["location"] = position.xpath('./td[5]/text()').extract_first()
                # 招聘人数
                item["number"] = position.xpath('./td[6]/text()').extract_first().strip()
                # 发布时间
                item["publish_date"] = position.xpath('./td[7]/text()').extract_first()
                # 职位 id
                position_id = position.xpath('./td[8]/span/@data-id').extract_first()

                position_detail = position.xpath('./following-sibling::tr[@id="j-job{}"]'.format(position_id))

                # 学历
                education = position_detail.xpath('.//li[1]/text()').extract_first()
                if education is not None:
                    education = education.split("：")[1]
                    item["education"] = education
                else:
                    item["education"] = None
                # 工作年限
                work_time = position_detail.xpath('.//li[2]/text()').extract_first()
                if work_time is not None:
                    work_time = work_time.split("：")[1]
                    item["work_time"] = work_time
                else:
                    item["work_time"] = None

                # 岗位描述
                description_list = position_detail.xpath('.//h3[text()="岗位描述"]/following-sibling::p/text()').extract()
                if description_list is not None:
                    description = ""
                    for i in description_list:
                        description += i.strip()
                    item["description"] = description
                else:
                    item["description"] = None

                # 岗位要求
                requirement_list = position_detail.xpath('.//h3[text()="岗位要求"]/following-sibling::p/text()').extract()
                if requirement_list is not None:
                    requirement = ""
                    for i in requirement_list:
                        requirement += i.strip()
                    item["requirement"] = requirement
                else:
                    item["requirement"] = None

                yield item

        next_url = response.xpath('//div[@class="m-page"]/a[text()=">"]/@href').extract_first()
        if next_url != "javascript:void(0)":
            next_url = response.urljoin(next_url)
            yield scrapy.Request(
                url = next_url,
                callback = self.parse
            )
