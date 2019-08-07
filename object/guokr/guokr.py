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
        pass

    def request_data(self, url):
        """

        :param url:
        :return:
        """

    def parser_data(self, data, page_num):
        """

        :param data:
        :param page_num:
        :return:
        """

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