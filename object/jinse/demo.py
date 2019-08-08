# -*- coding: utf-8 -*-
# @Time: 2019/8/8 20:20
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo.py
# @Software: PyCharm
import time


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
