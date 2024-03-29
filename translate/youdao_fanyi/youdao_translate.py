# -*- coding: utf-8 -*-
# @Time: 2019/8/10 22:20
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: youdao_translate.py
# @Software: PyCharm
import hashlib
import requests
import time
import random
import json


class YoudaoTranslate(object):
    def __init__(self):
        self.headers = {
            "Cookie": "OUTFOX_SEARCH_USER_ID=-1473530863@10.168.8.64; JSESSIONID=aaar3zlxnbn4jfaTFw7Xw; OUTFOX_SEARCH_USER_ID_NCOO=1472877600.7083225; ___rl__test__cookies=1565437688138",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
        }

        self.translate_url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

        self.form_data = {
            "i": None,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": None,
            "sign": None,
            "ts": None,
            "bv": "7e3150ecbdf9de52dc355751b074cf60",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME"
        }

    def generate_ts_salt_sign(self, word):
        """
        生成 ts、salt、sign 参数
        :return:
        """
        ts = str(int(time.time() * 1000))

        salt = ts + str(random.randint(0, 9))

        md5_object = hashlib.md5()
        md5_object.update(("fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj").encode())
        sign = md5_object.hexdigest()
        return ts, salt, sign

    def request_data(self, url, data):
        """
        发送翻译请求
        :param url:
        :param words:
        :return:
        """
        response_data = requests.post(url, headers = self.headers, data = data)
        return response_data.content.decode("utf-8")

    def parse_data(self, data):
        """
        解析数据
        :param data:
        :return:
        """
        if data:
            data_dict = json.loads(data)
            language_type = data_dict.get("type").split("2")
            print(language_type[0] + ":" + language_type[1])
            result = data_dict.get("translateResult")
            for i in result:
                print(i[0].get("src") + "<--->" + i[0].get("tgt"))

    def run(self, translating_str):
        """
        启动爬虫
        :param translating_str:
        :return:
        """
        word = translating_str
        ts, salt, sign = self.generate_ts_salt_sign(word)
        self.form_data["i"] = word
        self.form_data["ts"] = ts
        self.form_data["salt"] = salt
        self.form_data["sign"] = sign
        # print(self.form_data)

        translate_result = self.request_data(self.translate_url, self.form_data)
        # print(translate_result)

        self.parse_data(translate_result)


if __name__ == '__main__':
    while True:
        input_str = input("你想翻译什么(输入 q 退出。):")
        if input_str == "q":
            break
        YoudaoTranslate().run(input_str)
