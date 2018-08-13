# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from __future__ import absolute_import
from scrapy.utils.serialize import ScrapyJSONEncoder
from scrapy.exceptions import DropItem
from datetime import datetime
import sys
import os
import django
import json

encoder = ScrapyJSONEncoder()

# sys.path.append(os.path.join(os.path.dirname(os.path.dirname(
#     os.path.abspath(__file__))),
#     '..'))
# os.environ['DJANGO_SETTINGS_MODULE'] = 'habr.settings'
# django.setup()

class HabrFilterPipeline(object):
    def process_item(self, item, spider):
        from article.models import Period
        period = Period.objects.get(pk=1)

        period_begin_H = period.begin_time.split(':')[0]
        period_begin_M = period.begin_time.split(':')[1]
        period_end_H = period.end_time.split(':')[0]
        period_end_M = period.end_time.split(':')[1]

        post_time =  item['date'].split('T')[1][:5]
        post_H = post_time.split(':')[0]
        post_M = post_time.split(':')[1]

        if period_begin_H <= post_H <= period_end_H:
            return item
        else:
            raise DropItem('Not into period: %s' % item)


class HabrStorePipeline(object):
    def process_item(self, item, spider):
        from article.tasks import add_item
        add_item.delay(encoder.encode(item))
        return item
