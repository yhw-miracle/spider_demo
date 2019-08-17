# -*- coding: utf-8 -*-
# @Time: 2019/8/17 20:37
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo.py
# @Software: PyCharm
import requests
import re


if __name__ == '__main__':
    url = "https://fanyi.baidu.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Referer": "https://fanyi.baidu.com/"
    }
    response = requests.get(url = url, headers = headers)

    result = re.search(r"token: '(.*)'", response.content.decode("utf-8"))
    print(result[1])
