# -*- coding: utf-8 -*-
# @Time: 2019/8/8 8:37
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: jinse.py
# @Software: PyCharm
import time
import requests
import json
import os


class JinseSpider(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }

        # 基本 url，需拼接 data_type
        self.base_url = "https://api.jinse.com/v6/information/list?catelogue_key={}&limit=50&information_id=0&flag=down&version=9.9.9"

        # 不同分类
        self.data_type = ["hot", "news", "zhengce", "TOR", "personage", "fenxishishuo", "capitalmarket", "tech", "baike"]

        # 以爬取 url
        self.old_urls = set()

        # 未爬取 url
        self.new_urls = set()

    def request_data(self, url):
        """
        请求数据
        :param url:
        :return:
        """
        response = requests.get(url, headers = self.headers)
        return response.content.decode("utf-8")

    def parser_data(self, data, data_type):
        """
        解析数据
        :param data:
        :param data_type:
        :return:
        """
        news_data = list()
        next_url = None

        if data:
            data_to_dict = json.loads(data)

            if "status_code" in data_to_dict.keys() and data_to_dict["status_code"] == 500:
                next_url = None
            else:
                buttom_id = data_to_dict.get("bottom_id")
                next_url = "https://api.jinse.com/v6/information/list?catelogue_key={}&limit=50&information_id={}&flag=down&version=9.9.9".format(
                    data_type, buttom_id)

                data_list = data_to_dict.get("list")

                for i in data_list:
                    title = i.get("title")

                    i_extra = i.get("extra")

                    author = i_extra.get("author")

                    author_avator = i_extra.get("author_avatar")

                    author_level = i_extra.get("author_level")

                    published_timestamp = i_extra.get("published_at")
                    published_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(published_timestamp))

                    read_number = i_extra.get("read_number")

                    summary = i_extra.get("summary")

                    topic_m_url = i_extra.get("topic_url")
                    topic_url = topic_m_url.replace("m.", "") if topic_m_url else None

                    top_image_temp = i_extra.get("thumbnail_pic")
                    top_image = top_image_temp if top_image_temp else None

                    source_temp = i_extra.get("source")
                    source = source_temp if source_temp else None

                    news_data.append({
                        "title": title,
                        "author": author,
                        "author_avater": author_avator,
                        "author_level": author_level,
                        "published_time": published_time,
                        "read_number": read_number,
                        "summary": summary,
                        "topic_url": topic_url,
                        "top_image": top_image,
                        "source": source
                    })

        return news_data, next_url

    def save_data(self, f = None, t = "temp.md"):
        """
        保存数据
        :param f:
        :param t:
        :return:
        """
        for i in f:
            with open(t, "a", encoding = "utf-8") as file:
                json.dump(i, fp = file, ensure_ascii = False, indent = 4)
                file.write("\n")

    def run(self):
        """
        运行爬虫
        :return:
        """
        if "jinse_data" not in os.listdir("."):
            os.makedirs("jinse_data")

        if "data" not in os.listdir("./jinse_data/"):
            os.makedirs("./jinse_data/data")

        for i in self.data_type:
            page_num = 1

            print(i)
            requesting_url = self.base_url
            requesting_url = requesting_url.format(i)
            self.new_urls.add(requesting_url)

            while True:
                with open("jinse_data/jinse.log", "a", encoding = "utf-8") as file:
                    print(len(self.new_urls), len(self.old_urls), file = file)
                    print(self.new_urls, file = file)
                    print(self.old_urls, file = file)

                if requesting_url is None or len(self.new_urls) == 0:
                    break

                with open("jinse_data/jinse.log", "a", encoding = "utf-8") as file:
                    print("正在爬取 {} 第 {} 页数据...(from {})".format(i, page_num, requesting_url), file = file)

                print("正在爬取 {} 第 {} 页数据...(from {})".format(i, page_num, requesting_url))

                if requesting_url in self.new_urls and requesting_url not in self.old_urls:
                    response_data = self.request_data(requesting_url)

                    news_data, next_url = self.parser_data(response_data, i)
                    if next_url not in self.old_urls and next_url not in self.new_urls:
                        self.new_urls.add(next_url)

                    self.save_data(f = news_data, t = "jinse_data/data/" + i + ".json")

                    self.new_urls.remove(requesting_url)
                    self.old_urls.add(requesting_url)
                    requesting_url = next_url

                    page_num += 1
                    time.sleep(1)

            self.save_url(i)

    def save_url(self, t = None):
        """
        保存以爬取链接
        :param t:
        :return:
        """
        for i in self.old_urls:
            print(i)
            with open("jinse_data/data/" + t + "_old_urls.md", "a", encoding = "utf-8") as file:
                file.write("* [{}]({})".format(i, i) + "\n")


if __name__ == '__main__':
    JinseSpider().run()
