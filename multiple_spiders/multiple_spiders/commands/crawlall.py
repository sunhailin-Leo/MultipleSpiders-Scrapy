# -*- coding: utf-8 -*-
# encoding=UTF-8
'''''
Created on 2014年11月5日
@author: songs
'''
from scrapy.commands import ScrapyCommand
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

from multiple_spiders.spiders.multiple import MySpider1, MySpider2


class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return 'Runs all of the spiders'

    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)

    def process_options(self, args, opts):
        ScrapyCommand.process_options(self, args, opts)

    def run(self, args, opts):
        settings = get_project_settings()
        one = MySpider1()
        two = MySpider2()
        process = CrawlerProcess(settings)
        process.crawl(one)
        process.crawl(two)
        process.start()