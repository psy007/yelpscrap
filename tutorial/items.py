# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
#from scrapy.loader import ItemLoader
from scrapy.item import Item, Field
#from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import TakeFirst


class Yelp(Item):
    handyman_name = Field()
    handyman_address = Field()
    handyman_contact = Field()

'''
class YelpLoader(ItemLoader):
    default_item_class = Yelp
    default_output_processor = TakeFirst()
'''
