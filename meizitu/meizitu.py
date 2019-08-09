# -*- coding: utf-8 -*-
# @Time: 2019/8/9 22:56
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: meizitu.py
# @Software: PyCharm
import requests
from lxml import etree
import json
import re
import os
import time


class MeiziSpiser(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "origin": "https://www.jdlingyu.mobi"
        }

        self.base_url = "https://www.jdlingyu.mobi/wp-admin/admin-ajax.php?action=zrz_load_more_posts"

    def request_data(self, url, data = None):
        """
        请求数据
        :param url:
        :param data:
        :return:
        """
        response = requests.post(url, headers = self.headers, data = data)
        return response.content.decode("utf-8")

    def download_image(self, url):
        """
        下载图片
        :param url:
        :return:
        """

    def parser_data(self, data):
        """
        解析数据
        :param data:
        :return:
        """

    def save_data(self, f = None, t = None):
        """
        存储数据
        :param f:
        :param t:
        :return:
        """

    def run(self):
        """
        启动爬虫函数
        :return:
        """


if __name__ == '__main__':
    MeiziSpiser().run()
