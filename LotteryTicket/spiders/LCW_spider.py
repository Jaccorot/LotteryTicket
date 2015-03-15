# -*- coding: utf-8 -*
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from LotteryTicket.items import LotteryticketItem
import re


class LCWSpider(CrawlSpider):
    name = "lcw"

    allowed_domains = ["17500.cn"]

    start_urls = [
        "http://www.17500.cn/ssq/all.php"
    ]

    rules = [
        Rule(SgmlLinkExtractor(allow=('/ssq/details.php\?issue=(\d{7})',)), callback='parse_page')
    ]

    @staticmethod
    def parse_page(response):
        hxs = HtmlXPathSelector(response)
        item = LotteryticketItem()
        # 期数
        title = hxs.select('//html/body/center/center/table/tr/td/table[1]/tr[2]/td[1]/text()').extract()[0]
        item['title'] = filter(str.isdigit, ("".join(title.split()).encode("utf-8")))
        # 红色球区
        red1 = hxs.select('//html/body/center/center/table/tr/td/table[2]/tbody/tr[2]/td[1]/font/text()').extract()[0]
        item['red1'] = filter(str.isdigit, ("".join(red1.split()).encode("utf-8")))
        red2 = hxs.select('//html/body/center/center/table/tr/td/table[2]/tbody/tr[2]/td[2]/font/text()').extract()[0]
        item['red2'] = filter(str.isdigit, ("".join(red2.split()).encode("utf-8")))
        red3 = hxs.select('//html/body/center/center/table/tr/td/table[2]/tbody/tr[2]/td[3]/font/text()').extract()[0]
        item['red3'] = filter(str.isdigit, ("".join(red3.split()).encode("utf-8")))
        red4 = hxs.select('//html/body/center/center/table/tr/td/table[2]/tbody/tr[2]/td[4]/font/text()').extract()[0]
        item['red4'] = filter(str.isdigit, ("".join(red4.split()).encode("utf-8")))
        red5 = hxs.select('//html/body/center/center/table/tr/td/table[2]/tbody/tr[2]/td[5]/font/text()').extract()[0]
        item['red5'] = filter(str.isdigit, ("".join(red5.split()).encode("utf-8")))
        red6 = hxs.select('//html/body/center/center/table/tr/td/table[2]/tbody/tr[2]/td[6]/font/text()').extract()[0]
        item['red6'] = filter(str.isdigit, ("".join(red6.split()).encode("utf-8")))
        # 蓝色球区
        blue = hxs.select('//html/body/center/center/table/tr/td/table[2]/tbody/tr[2]/td[7]/font/text()').extract()[0]
        item['blue'] = filter(str.isdigit, ("".join(blue.split()).encode("utf-8")))
        # 开奖时间
        created_at = hxs.select('//html/body/center/center/table/tr/td/table[1]/tr[2]/td[2]/text()').extract()[0]
        item['created_at'] = ("".join(created_at.split()).encode("utf-8"))[0:10]

        return item
