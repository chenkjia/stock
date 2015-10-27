# -*- coding: utf-8 -*-
BOT_NAME = 'stock'

SPIDER_MODULES = ['stock.spiders']
NEWSPIDER_MODULE = 'stock.spiders'


ITEM_PIPELINES = {
    'stock.pipelines.stockPipeline':1,
}
