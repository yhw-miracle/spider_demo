# -*- coding: utf-8 -*-
# @Time: 2019/8/7 19:59
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: guokr.py
# @Software: PyCharm

"""
url： GET https://www.guokr.com/ask/highlight
问答list：//ul[@class="ask-list-cp"]/li
下一页： https://www.guokr.com + //a[text()="下一页"]/@href


title: //ul[@class="ask-list-cp"]/li//h2/a/text()
title_url: //ul[@class="ask-list-cp"]/li//h2/a/@href
summary: //ul[@class="ask-list-cp"]/li//p[contains(@class, "summary")]/text()
tag: //ul[@class="ask-list-cp"]/li//p[@class="tags"]/a/text()
focus_nums: //ul[@class="ask-list-cp"]/li//p[contains(@class,"focus-nums")]/span/text()
answer_nums: //ul[@class="ask-list-cp"]/li//p[contains(@class,"answer-nums")]/span/text()

构造数据：
{
    "from": "guokr",
    "data": [
        {
            "title": "",
            "title_url": "",
            "summary": "",
            "tag": ["",],
            "focus_nums": "",
            "answer_nums": ""
        },
    ]
}
"""
import requests
from lxml import etree
import json
import time


class Guokrspider(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
        self.base_url = "https://www.guokr.com/ask/highlight"

    def request_data(self, url):
        """

        :param url:
        :return:
        """
        resposne = requests.get(url, headers = self.headers)
        return resposne.content.decode("utf-8")

    def parser_data(self, data, page_num):
        """

        :param data:
        :param page_num:
        :return:
        """
        etree_to_result = etree.HTML(data)
        detail_list = etree_to_result.xpath('//ul[@class="ask-list-cp"]/li')

        detail_page = list()
        if len(detail_list) > 0:
            for index, detail in enumerate(detail_list):
                print(">>>正在爬取第 {} 页中第 {} 个数据...".format(page_num, index + 1))
                detail_data = dict()

                title = detail.xpath('.//h2/a/text()')
                title_url = detail.xpath('.//h2/a/@href')
                summary = detail.xpath('.//p[contains(@class, "summary")]/text()')
                tag = detail.xpath('.//p[@class="tags"]/a/text()')
                focus_nums = detail.xpath('.//p[contains(@class,"focus-nums")]/span/text()')
                answer_nums = detail.xpath('.//p[contains(@class,"answer-nums")]/span/text()')

                detail_data["title"] = title[0] if len(title) > 0 else None
                detail_data["title_url"] = title_url[0] if len(title_url) > 0 else None
                detail_data["summary"] = summary[0] if len(summary) > 0 else None
                detail_data["tag"] = tag if len(tag) > 0 else None
                detail_data["focus_nums"] = focus_nums[0] if len(focus_nums) > 0 else None
                detail_data["answer_nums"] = answer_nums[0] if len(answer_nums) > 0 else None

                detail_page.append(detail_data)

        next_url = etree_to_result.xpath('//a[text()="下一页"]/@href')

        next_url = "https://www.guokr.com" + next_url[0] if len(next_url) > 0 else None

        return detail_page, next_url

    def save_data(self, f = None, t = "temp.md"):
        """

        :param data:
        :return:
        """

    def run(self):
        """

        :return:
        """


if __name__ == '__main__':
    Guokrspider().run()