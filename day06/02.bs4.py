# !/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
author: HuangWei
"""
from bs4 import BeautifulSoup


html = """
<html><head><title>我是标题</title></head>
<body>
<p class="title" name="dromouse"><b>我是标签</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""


soup = BeautifulSoup(html, "lxml")
# print(soup.prettify())
# 标签提取
# l = soup.find_all('a')[1].get_text() # 获取a标签第二个，并获取值
# l = soup.find_all('a')
# l = soup.find_all(id="link2")[0].get_text()
l = soup.find_all(class_="sister")
# l = soup.find_all(text=['Lacie', 'Tillie'])

# 选择器
# l = soup.select('a[id="link1"]')
# l = soup.select('#link1')


print(l)

