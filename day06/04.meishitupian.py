# !/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@Author   : HuangWei
@time     : 2019/12/23 20:36
@File     : 04.meishitupian.py
@Software : PyCharm
"""
import requests
import re
from lxml import etree
from bs4 import BeautifulSoup


class FoodTB(object):
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f'
        self.params = {
            'kw': '美食',
            'pn': 0
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }

    def parse_request(self, url, params):
        response = requests.get(url, params=params, headers=self.headers)
        return response.content.decode()

    def parse_data(self, data):
        renigx = re.compile('id="pagelet_html_frs-list/pagelet/thread_list" style="display:none;"><!--(.*?)<div class="thread_list_bottom clearfix">', re.S)
        result = renigx.findall(data)
        # print(result)
        html_str = etree.HTML(str(result))
        link = html_str.xpath('//ul[@id="thread_list"]/li/div/div[2]/div/div[1]/a/@href')
        detail_link = []
        for i in link:
            detail_link.append(self.url + i)
        print(len(detail_link))
        print(len(link))
        print(detail_link)

    def run(self):
        data = self.parse_request(self.url, params=self.params)
        self.parse_data(data)


if __name__ == '__main__':
    ftb = FoodTB()
    ftb.run()
