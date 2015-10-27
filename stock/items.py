# -*- coding: utf-8 -*-

import scrapy


class stockItem(scrapy.Item): #stockItem 为自动生成的类名
    news_title = scrapy.Field() #南邮新闻标题
    news_date = scrapy.Field()     #南邮新闻时间
    news_url = scrapy.Field()   #南邮新闻的详细链接
