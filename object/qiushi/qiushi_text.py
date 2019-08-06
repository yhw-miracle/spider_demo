# -*- coding: utf-8 -*-
# @Time: 2019/8/6 20:36
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: qiushi_text.py
# @Software: PyCharm

"""
爬取糗事百科中文字内容

url: https://www.qiushibaike.com/text/
文字内容：//div[contains(@class, "article")]//div[@class="content"]/span
下一页链接：//span[@class="next"]/parent::a/@href
"""

import requests
from lxml import etree


class QiuShi(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }

    def get_data(self, url):
        """
        请求数据
        :param url: 请求的 url
        :return: 响应数据
        """
        response = requests.get(url, headers = self.headers)
        return response.content.decode("utf-8")

    @staticmethod
    def parse_data(data):
        """
        解析数据
        :param data: 待解析的数据
        :return: 解析后的数据和下一页链接
        """
        etree_to_result = etree.HTML(data)
        article_data = etree_to_result.xpath('//div[contains(@class, "article")]//div[@class="content"]/span/text()')

        next_url = etree_to_result.xpath('//span[@class="next"]/../@href')

        if len(article_data) == 0:
            article_data = None

        if len(next_url) == 0:
            next_url = None
        else:
            next_url = "https://www.qiushibaike.com" + next_url[0]

        return article_data, next_url

    @staticmethod
    def save_data(f = None, t = "temp.md"):
        """
        保存数据
        :param f: 数据源，即数据从哪儿来
        :param t: 数据归宿，即数据到哪儿去
        :return: None
        """
        with open(t, "a", encoding = "utf-8") as file:
            for i in f:
                file.write(i)
                file.write("___")

    def run(self):
        """
        启动爬虫
        :return: None
        """
        next_url = "https://www.qiushibaike.com/text/"

        while True:
            if next_url is None:
                break

            response_data = self.get_data(next_url)

            article_data, next_url = self.parse_data(response_data)

            if article_data:
                self.save_data(article_data, "article.md")


if __name__ == '__main__':
    QiuShi().run()
