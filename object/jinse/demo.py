# -*- coding: utf-8 -*-
# @Time: 2019/8/8 20:20
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo.py
# @Software: PyCharm
import time
import json


if __name__ == '__main__':
    # 将时间戳格式化
    # print(time.ctime(1565227826), type(time.ctime(1565227826)))
    # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1565227826)))

    # -----------------------------------------------------------------------
    # 字典操作
    d = {"1": {"2": 3}}
    print(d.get("1").get("2"))

    d = {"status_code": 500}
    print("status_code" in d.keys())

    # -----------------------------------------------------------------------
    # json 方法使用
    # d = {
    #     "id": 495051,
    #     "extra": {
    #         "child_id": 423605,
    #     }
    # }
    # with open("demo.json", "a", encoding = "utf-8") as file:
    #     json.dump(d, file, ensure_ascii = False, indent = 4)

    # -----------------------------------------------------------------------
    # print 输出重定向
    with open("temp.log", "a", encoding = "utf-8") as file:
        print("111", file = file)
