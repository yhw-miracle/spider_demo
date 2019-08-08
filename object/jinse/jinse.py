# -*- coding: utf-8 -*-
# @Time: 2019/8/8 8:37
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: jinse.py
# @Software: PyCharm
import time
import requests
import json


class JinseSpider(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }

        self.base_url = "https://api.jinse.com/v6/information/list?catelogue_key={}&limit=50&information_id=0&flag=down&version=9.9.9"

    def request_data(self, url):
        """
        请求数据
        :param url:
        :return:
        """

    def parser_data(self, data, data_type):
        """
        解析数据
        :param data:
        :param data_type:
        :return:
        """

    def save_data(self, f = None, t = "temp.md"):
        """
        保存数据
        :param f:
        :param t:
        :return:
        """

    def run(self):
        """
        运行爬虫
        :return:
        """


if __name__ == '__main__':
    JinseSpider().run()
