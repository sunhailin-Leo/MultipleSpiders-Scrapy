# 并行Scrapy爬虫
### Parallel Processing Spiders On Scrapy

---

<h3 id="Q&A">问题反馈</h3>
在使用中有任何问题，可以反馈给我，以下联系方式跟我交流

* Author: Leo
* Wechat: Leo-sunhailin 
* E-mail: 379978424@qq.com 

---

<h3 id="Title">题目</h3>

1. 题目或许应该叫: Multiple Spiders in the same process.  
2. 官方文档的解释就是: 默认情况下Scrapy支持一个爬虫在多线程的情况下进行爬取，但是实际上也支持多个爬虫运行在每一个线程上.(官方也补充了一个internal API，实际上就是Crawl(爬虫)的核心启动接口)
3. 有空的我可以写写Scrapy的技巧，如果遇到的话哈哈~有前提的.

---

<h3 id="Example">示例</h3>

* 网上其实有很多参照官网给的例子跑的commands代码，但是多少都一些问题，你不信可以跑一下，很多都是能跑成功但是有报错。
* 其实讲回上面这点，官方也是很奇葩的，给了怎么并发爬虫，不告诉别人怎么运行，直接只是一个scrapy crawl不带参数的，这样也能跑，但是也有报错提示的。
* 正确的写法和不会报错的写法请往下看~


1. 创建一个Scrapy的项目. 对！就是一个普通项目，并没有什么特别的模板.

```Python
scrapy startproject multiple_spiders
```

2. 生成的文件结构是这样的:

* multiple_spiders
    * multiple_spiders
        * commands (一开始没有的，后面创建)
            * <双下划线>init<双下划线>.py
            * crawlall.py
        * spiders (核心代码)
            * <双下划线>init<双下划线>.py
            * multiple.py
        * <双下划线>init<双下划线>.py
        * items.py
        * middlewares.py
        * pipelines.py
        * settings.py
    * scrapy.cfg

3. spiders/multiple.py的代码:

```Python
# -*- coding: UTF-8 -*-
"""
Created on 2017年11月8日
@author: Leo
"""

import scrapy


# 测试代码，功能是把网址的源代码保存到txt中
class MySpider1(scrapy.Spider):
    name = "spider-1"
    start_urls = ["<爬取的地址1>"]

    def parse(self, response):
        filename = "./multiple_spiders/test-1.txt"
        with open(filename, 'wb') as f:
            f.write(response.body)


# 测试代码，功能是把网址的源代码保存到txt中
class MySpider2(scrapy.Spider):
    name = "spider-2"
    start_urls = ["<爬取的地址2>n"]

    def parse(self, response):
        filename = "./multiple_spiders/test-2.txt"
        with open(filename, 'wb') as f:
            f.write(response.body)
```

4. 创建commands文件夹，以及文件夹下的__init__.py文件
(init.py里面不用写东西)

创建crawlall.py<名字可以自定义>
```Python
# -*- coding: utf-8 -*-
"""
Created on 2017年11月8日
@author: Leo
"""

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
```

5. settings.py中加一入一个代码:

```Python
COMMANDS_MODULE = 'multiple_spiders.commands'
```

6. 最后就可以运行了

```Python
scrapy crawlall<名字和你commands文件夹的下的py文件名字对应即可>
```

7. 至于不想同时启动两个爬虫，或者同时启动三个，或者有三个爬虫同时启动其中2个，过一段时间关闭其中一个再开启另外一个的这类需求。。动动脑子就好了。
