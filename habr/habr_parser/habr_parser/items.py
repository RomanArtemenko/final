# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HabrItem(scrapy.Item):
    avatar = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    keywords = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()
