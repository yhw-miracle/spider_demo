# -*- coding: utf-8 -*-
# @Time: 2019/8/9 22:56
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo.py
# @Software: PyCharm


if __name__ == '__main__':
    # 获取图片链接中图片名称
    str1 = "http://quamsm.cn/images/2019/08/04/A76056adfly1g5grovihn0j22pa41u4qx.jpg"
    print(str1.split("/")[-1])
