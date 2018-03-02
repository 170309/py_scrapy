# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    
    pass

class DmozItem(scrapy.Item):
	catogery = scrapy.Field()
	cid = scrapy.Field()
	company = scrapy.Field()
	income = scrapy.Field()
	
# class DoubanMovieItem(scrapy.Item):
	# id = scrapy.Field()
	# company = scrapy.Field()
	# income = scrapy.Field()

		