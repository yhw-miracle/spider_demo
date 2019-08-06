# -*- coding: utf-8 -*-
# @Time: 2019/8/4 9:46
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: login_github.py
# @Software: PyCharm
import requests
import re
import os
from dotenv import load_dotenv
load_dotenv()

"""
commit=Sign+in&utf8=%E2%9C%93&authenticity_token=kU6Pm3y86HJ1M%2FSTXNcnXkix3Hkg7uGzY1vZggV2%2FL7u8e4xaA1DiymIsovmOUMFLf9j3K1jpNBaTskC4iiZLQ%3D%3D&login=***&password=***&webauthn-support=supported

commit: Sign in
utf8: ✓
authenticity_token: kU6Pm3y86HJ1M/STXNcnXkix3Hkg7uGzY1vZggV2/L7u8e4xaA1DiymIsovmOUMFLf9j3K1jpNBaTskC4iiZLQ==
login: ***
password: ***
webauthn-support:
"""


class LoginGithub(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

        self.session = requests.session()

    def get_login_authentication(self, login_url):
        """
        获取登录授权
        :param login_url:
        :return:
        """
        login_response = self.session.get(login_url, headers = self.headers)

        authenticity_token = re.search('<input type="hidden" name="authenticity_token" value="(.*)" />', login_response.text).group(1)

        # print(authenticity_token)

        return authenticity_token

    def start_login(self, login_post_url, profile_url,authenticity_token):
        """
        开始登录，获取个人中心页面
        :param login_post_url:
        :param profile_url:
        :param authenticity_token:
        :return:
        """

        login_data = {
            "commit": "Sign in",
            "utf8": "✓",
            "authenticity_token": authenticity_token,
            "login": self.username,
            "password": self.password,
            "webauthn-support": "supporte"
        }

        self.session.post(login_post_url, headers = self.headers, data = login_data)

        profile_response = self.session.get(profile_url, headers = self.headers)

        return profile_response.content.decode("utf-8")

    def save_data(self, f = None, t = None):
        """
        保存个人中心数据
        :param f:
        :param t:
        :param profile_data:
        :return:
        """
        with open(t, "w", encoding = "utf-8") as file:
            file.write(f)

    def run(self):
        # login url
        login_url = "https://github.com/login"
        authenticity_token = self.get_login_authentication(login_url)

         # 登录请求
        login_post_url = "https://github.com/session"
        # 个人中心
        profile_url = "https://github.com/yhw-miracle"
        profile_data = self.start_login(login_post_url, profile_url, authenticity_token)

        # 保存数据
        self.save_data(profile_data, "github_yhw-miracle.html")


if __name__ == '__main__':
    LoginGithub(os.environ.get("github_username"), os.environ.get("github_password")).run()
