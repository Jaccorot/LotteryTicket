# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class LotteryticketItem(scrapy.Item):
    title = Field()
    red1 = Field()
    red2 = Field()
    red3 = Field()
    red4 = Field()
    red5 = Field()
    red6 = Field()
    blue = Field()
    created_at = Field()