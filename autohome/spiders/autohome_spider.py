# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from autohome.items import AutohomeItem

class AutohomeSpiderSpider(CrawlSpider):
    name = 'autohome_spider'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/photolist/series/672/p1/']

    rules = (
        Rule(LinkExtractor(allow=r'.+672\/p.+'),callback='parse_item',follow=True),
    )

    def parse_item(self, response):
        image_urls1 = response.xpath('//ul[@id="imgList"]//li/a/img/@src').getall()
        image_urls2 = response.xpath('//ul[@id="imgList"]//li/a/img/@src2').getall()
        image_urls = image_urls1[:30] + image_urls2
        image_urls = list(map(lambda x:'https:'+x.replace('240x180_0','1024x0_1'),image_urls))
        title = response.xpath('//ul[@id="imgList"]//li/a/img/@alt').get()
        item = AutohomeItem(image_urls=image_urls,title=title)
        return item
