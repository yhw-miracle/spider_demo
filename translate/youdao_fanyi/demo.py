# -*- coding: utf-8 -*-
# @Time: 2019/8/10 22:21
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo.py
# @Software: PyCharm
import hashlib
import time


if __name__ == '__main__':
    # 练习 hashlib 模块
    # md5 = hashlib.md5()
    # md5.update("7e3150ecbdf9de52dc355751b074cf60".encode("utf-8"))
    #
    # print(md5.hexdigest())
    #
    # # sha1 = hashlib.sha1()
    # md51 = hashlib.md5()
    # md51.update("7e3150ecbdf9de52dc355751b074cf60".encode("utf-8"))
    # print(md51.hexdigest())
    #
    # print(md5.hexdigest() == md51.hexdigest())

    # ----------------------------------------------------------------
    # 练习 time 模块
    print(time.time() * 1000)   # 13 位整数
