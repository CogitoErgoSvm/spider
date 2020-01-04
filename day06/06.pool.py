# !/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@Author   : HuangWei
@time     : 2019/12/28 18:54
@File     : 06.pool.py
@Software : PyCharm
"""
# import threading
import gevent
# from multiprocessing.dummy import Pool
from gevent import monkey
monkey.patch_all()
import requests
from lxml import etree
import time

monkey.patch_all()


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
        time.sleep(1)
        response = requests.get(url, params=params, headers=self.headers, verify=False)
        data = response.content.decode()
        self.parse_data(data)

    def parse_data(self, data):
        # print(data)
        html_str = etree.HTML(data)
        movies_name = html_str.xpath('//div[@id="content"]/div/div/ol/li/div/div[2]/div/a/span[1]/text()')
        print(movies_name)

    def run(self):
        starttime = time.time()
        gevent_list = []
        for i in range(0, 250, 25):
            self.params['start'] = i
            print(self.params)
            # self.parse_request(self.base_url, params=self.params)
            # gevents = gevent.spawn(self.parse_request, (self.base_url, self.params))
            gevents = gevent.spawn(self.parse_request, url=self.base_url, params=self.params)
            gevent_list.append(gevents)

        gevent.joinall(gevent_list)

        for j in gevent_list:
            print(j)

        endtime = time.time()
        t = endtime - starttime
        print(t)


if __name__ == '__main__':
    dbs = DBspider()
    dbs.run()