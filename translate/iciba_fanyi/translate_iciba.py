# -*- coding: utf-8 -*-
# @Time: 2019/8/4 11:53
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: translate_iciba.py
# @Software: PyCharm

"""
url: post http://fy.iciba.com/ajax.php?a=fy
Form Data: &f=auto&t=auto&w=我是中国人
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36
Referer: http://fy.iciba.com/
"""

import requests
import json


class ICiBa(object):
    """
    金山翻译
    """
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Referer": "http://fy.iciba.com/"
        }

    def translate(self, translate_url, data):
        """
        请求翻译
        :param translate_url:
        :param data:
        :return:
        """
        translate_data = {
            "f": "auto",
            "t": "auto",
            "w": data
        }

        translate_result = requests.post(translate_url, headers = self.headers, data = translate_data)

        return translate_result.content.decode("utf-8")

    def parse_data(self, data):
        # print(json.loads(data))
        # print(json.loads(data)["content"]["out"])

        return json.loads(data)["content"]["out"]

    def run(self):
        # translate url ===> http://fy.iciba.com/ajax.php?a=fy
        translate_url = "http://fy.iciba.com/ajax.php?a=fy"
        while True:
            data = input("你想翻译什么？")
            if data == "q":
                break

            translate_response = self.translate(translate_url, data)

            result = self.parse_data(translate_response)

            print(data, "--->", result)


if __name__ == '__main__':
    ICiBa().run()
