# -*- coding: utf-8 -*-
# @Time: 2019/8/22 10:05
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: igetget_spider.py
# @Software: PyCharm
import requests


if __name__ == '__main__':
    url_login = "https://entree.igetget.com/ebook2/v1/ranklist/list?count=20&requestType=total_rank&max_id=0"
    url_no_login = "https://entree.igetget.com/ebook2/v1/ebook/list"
    headers = {
        "Xi-App-Key": "android-7.0.0",
        "Xi-Uid": "216919221",
        "Xi-Thumb": "m",
        "Xi-Dt": "phone",
        "Xi-Ov": "6.0",
        "Xi-Net": "WIFI",
        "Xi-Os": "ANDROID",
        "Xi-D": "7b6bc8d99f0cbc76",
        "Xi-Dv": "vivo Y67",
        "Xi-T": "json",
        "Xi-Chil": "0",
        "Xi-V": "2",
        "Xi-Av": "7.0.0",
        "Xi-Scr": "2.0",
        "Xi-Adv": "1",
        "Xi-Seid": "e9c6eb86caf3579ba07c1cda77a797fa",
        "G-Auth-Sign": "6c48a7363b8c77f81189d106d71879dd425a78ab",
        "G-Auth-Nonce": "6b9fe18ff6c822fc6835986bd0f7ec47",
        "G-Auth-Ts": "1566440330",
        "G-Auth-Appid": "463ceba202a9f6f9ac4cd98d0f2f2876204ea85c",
        "G-Auth-Token": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJpZ2V0Z2V0LmNvbSIsImV4cCI6MTU2OTAzMjMxMSwiaWF0IjoxNTY2NDQwMzExLCJpc3MiOiJEREdXIEpXVCBNSURETEVXQVJFIiwibmJmIjoxNTY2NDQwMzExLCJzdWIiOiIyMTY5MTkyMjEifQ.fomGpBMkoXZJOTPaKCRlvyMLuiFHR8tXTlemflZ9kxV05CFiJId9TqB69pgp-KeY69A81QF7rpXsDt1Pw5Hi4w",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "521",
        "Host": "entree.igetget.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.12.1",
    }

    form_data = {
        "since_id": 0,
        "count": 20,
        "sort": "sevenday",
        "h": {"u":"216919221","thumb":"m","dt":"phone","ov":"6.0","net":"WIFI","os":"ANDROID","d":"7b6bc8d99f0cbc76","dv":"vivo Y67","t":"json","chil":"0","v":"2","av":"7.0.0","scr":"2.0","adv":"1","ts":"1566440330","s":"fe7897beb0eb6db1","seid":"e9c6eb86caf3579ba07c1cda77a797fa"},
        "max_id": 0
    }

    response = requests.post(url = url_no_login, headers = headers, verify = False, data = form_data)

    print(response)

