# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DomeScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    img = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
    category = scrapy.Field()
    pass

class DeliveryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    img = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    category = scrapy.Field()
    pass
