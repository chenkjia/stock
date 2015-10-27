# -*- coding: utf-8 -*-
import json
class stockPipeline(object):
  def __init__(self):
    self.file = open('stock.txt',mode='wb')
  def process_item(self, item, spider):
    self.file.write(item['news_title'].encode("GBK"))
    self.file.write("\n")
    self.file.write(item['news_date'].encode("GBK"))
    self.file.write("\n")
    self.file.write(item['news_url'].encode("GBK"))
    self.file.write("\n")
    return item
