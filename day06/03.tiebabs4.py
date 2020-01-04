# !/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
author: HuangWei
"""
import requests
import json
from bs4 import BeautifulSoup
from lxml import etree


url = 'https://tieba.baidu.com/mo/q/m?kw=%E7%BE%8E%E9%A3%9F&pn=0&lp=5024&forum_recommend=1&lm=0&cid=0&has_url_param=0&pn=30&is_ajax=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'
}
requests.packages.urllib3.disable_warnings()
response = requests.get(url, headers=headers, verify=False)
data = response.content.decode()
data = json.loads(data)['data']['content']
# print(type(data))
# print(data)
soup = BeautifulSoup(data, 'lxml')
# print(soup.prettify())
# print(type(soup.prettify()))
# with open('03.html', 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())
l = soup.select('.j_common')
print(len(l))
for i in l:
    # print(i)
    # print(type(str(i)))
    html_str = str(i)
    html_str1 = etree.HTML(html_str)
    span = html_str1.xpath('//span/text()')[0]
    print(span)
