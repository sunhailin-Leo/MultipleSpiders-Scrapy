# -*- coding: UTF-8 -*-
"""
Created on 2017年11月8日
@author: Leo
"""

import scrapy


class MySpider1(scrapy.Spider):
    name = "spider-1"
    start_urls = ["http://www.gzcc.cn"]

    def parse(self, response):
        filename = "./multiple_spiders/test-1.txt"
        with open(filename, 'wb') as f:
            f.write(response.body)


class MySpider2(scrapy.Spider):
    name = "spider-2"
    start_urls = ["http://jwxw.gzcc.cn"]

    def parse(self, response):
        filename = "./multiple_spiders/test-2.txt"
        with open(filename, 'wb') as f:
            f.write(response.body)



