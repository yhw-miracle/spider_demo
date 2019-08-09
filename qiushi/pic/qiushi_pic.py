# -*- coding: utf-8 -*-
# @Time: 2019/8/6 21:05
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: qiushi_pic.py
# @Software: PyCharm

"""
爬取糗事百科中糗图
url: https://www.qiushibaike.com/pic/

articel_div: //div[contains(@class, "article")]

**需要留心与下面具体信息数量是否相同**

描述信息: //div[contains(@class, "article")]//div[@class="content"]/span/text()

图片: //div[contains(@class, "article")]//div[@class="thumb"]//img/@src

下一页链接: //ul[@class="pagination"]//span[@class="next"]/parent::a/@href

"""
import requests
from lxml import etree
import re


class QiuShiPic(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }

    def get_data(self, url):
        """
        请求数据
        :param url: 请求 url
        :return: 响应数据
        """
        response = requests.get(url, headers = self.headers)
        return response.content.decode("utf-8")

    def get_image_data(self, url):
        """
        请求图片数据
        :param url: 图片 url
        :return: 图片数据
        """
        response = requests.get(url, headers = self.headers)
        return response.content

    @staticmethod
    def parse_data(data):
        """
        解析数据
        :param data: 待解析的数据
        :return: 图片信息和下一页链接
        """
        etree_to_result = etree.HTML(data)
        article_data = etree_to_result.xpath('//div[contains(@class, "article")]')

        # 构造解析后的数据
        pic_data = list()

        if len(article_data) > 0:
            for i in article_data:
                description = i.xpath('.//div[@class="content"]/span/text()')
                if len(description) > 0:
                    description = description[0]

                    image_src = i.xpath('.//div[@class="thumb"]//img/@src')
                    if len(image_src) > 0:
                        image_src = image_src[0]

                        pic_data.append({
                            "description": description,
                            "image_url": "https:" + image_src
                        })

        if len(pic_data) == 0:
            pic_data = None

        next_url = etree_to_result.xpath('//ul[@class="pagination"]//span[@class="next"]/parent::a/@href')

        if len(next_url) == 0:
            next_url = None
        else:
            next_url = "https://www.qiushibaike.com" + next_url[0]

        return pic_data, next_url

    def save_data(self, f = None, t = "temp.md"):
        """
        保存数据
        :param f: 数据从哪儿来
        :param t: 数据到哪儿去
        :return: None
        """
        with open(t, "a", encoding = "utf-8") as file:
            for i in f:
                file.write(i.get("description") + "\n")

                image_url = i.get("image_url")
                image_name = re.search(r'medium/(.*.jpg)', image_url).group(1)
                with open("./data/pic/" + image_name, "wb") as image_file:
                    image_file.write(self.get_image_data(image_url))
                file.write("![{0}]({1})".format(image_name, "./pic/" + image_name) + "\n")
                file.write("___" + "\n")
                file.write("![{0}]({1})".format(image_name, image_url) + "\n")
                file.write("___" + "\n\n\n")

    def run(self):
        """
        运行爬虫
        :return: None
        """
        next_url = "https://www.qiushibaike.com/pic/"

        while True:
            if next_url is None:
                break

            response_data = self.get_data(next_url)

            pic_data, next_url = self.parse_data(response_data)

            if pic_data:
                self.save_data(pic_data, "./data/pic.md")


if __name__ == '__main__':
    QiuShiPic().run()
