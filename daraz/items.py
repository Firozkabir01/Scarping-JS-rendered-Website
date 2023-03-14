# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DarazItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    disc_price = scrapy.Field()
    discount = scrapy.Field()
    original_price = scrapy.Field()
    rating = scrapy.Field()
    review = scrapy.Field()
    brand = scrapy.Field()
    std_deliver_fee = scrapy.Field()
    return_policy = scrapy.Field()
