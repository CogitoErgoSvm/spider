# !/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@Author   : HuangWei
@time     : 2019/12/27 11:07
@File     : 05.douban.py
@Software : PyCharm
"""
import requests
from lxml import etree
import time
import threading


class DBspider(object):
    def __init__(self):
        self.base_url = 'https://movie.douban.com/top250'
        self.params = {
            'start': 0,
            'filter': ''
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }

    def parse_request(self, url, params):
        response = requests.get(url, params=params, headers=self.headers)
        data = response.content.decode()
        self.parse_data(data)

    def parse_data(self, data):
        # print(data)
        html_str = etree.HTML(data)
        movies_name = html_str.xpath('//div[@id="content"]/div/div/ol/li/div/div[2]/div/a/span[1]/text()')
        print(movies_name)

    def run(self):
        starttime = time.time()
        thread_list = []
        for i in range(0, 250, 25):
            self.params['start'] = i
            print(self.params)
            # self.parse_request(self.base_url, params=self.params)
            threads = threading.Thread(target=self.parse_request, args=(self.base_url, self.params))
            threads.start()
            thread_list.append(threads)

        for j in thread_list:
            j.join()

        endtime = time.time()
        t = endtime - starttime
        print(t)


if __name__ == '__main__':
    dbs = DBspider()
    dbs.run()