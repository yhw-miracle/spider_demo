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
        response = requests.get(url, headers = self.headers)
        return response.content

    def parser_data(self, data):
        """
        解析数据
        :param data:
        :return:
        """
        post_data = json.loads(data)["msg"]
        if post_data == "":
            return None

        etree_to_result = etree.HTML(post_data)
        post_list_div = etree_to_result.xpath('//div[contains(@class, "post-list")]')

        post_list = list()
        for post in post_list_div:
            title_temp = post.xpath('.//a[@rel]/text()')
            if len(title_temp) > 0:
                title = title_temp
            else:
                continue

            time_temp = post.xpath('.//time/@datetime')
            time = title_temp if len(time_temp) > 0 else None

            link_temp = post.xpath('.//a[@class="link-block"]/@href')
            link = link_temp if len(link_temp) > 0 else None

            image_src_temp = post.xpath('.//div[contains(@class,"preview")]/@style')

            # (http|https)://.*.jpg

            image_src = re.search(r'(http|https)://.*.jpg', image_src_temp[0])[0] if len(image_src_temp) > 0 else None

            # if len(image_src_temp) > 0:
            #     image_src = re.search(r'http://.*.jpg', image_src_temp[0])[0]
            # else:
            #     image_src = None

            post_list.append({
                "title": title,
                "time": time,
                "link": link,
                "image_src": image_src
            })

        return post_list

    def save_data(self, f = None, t = None):
        """
        存储数据
        :param f:
        :param t:
        :return:
        """
        if "meizitu" not in os.listdir("."):
            os.makedirs("meizitu")

        if "images" not in os.listdir("./meizitu"):
            os.makedirs("./meizitu/images")

        t = "./meizitu/" + "data.json"
        for i in f:
            with open(t, "a", encoding = "utf-8") as file:
                file.write(json.dumps(i, ensure_ascii = False) + "\n")
            if i.get("image_src"):
                print(i.get("image_src"))
                print("图片下载中...")
                # 获取图片名
                image_name = i.get("image_src").split("/")[-1]
                with open("./meizitu/images/" + image_name, "wb") as file:
                    file.write(self.download_image(i.get("image_src")))

    def run(self):
        """
        启动爬虫函数
        :return:
        """


if __name__ == '__main__':
    MeiziSpiser().run()
