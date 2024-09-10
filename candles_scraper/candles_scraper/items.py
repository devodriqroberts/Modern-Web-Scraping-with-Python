# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CandlesScraperItem(scrapy.Item):
    # define the fields for your item here like:
    product_brand = scrapy.Field()
    product_link = scrapy.Field()
    product_heading = scrapy.Field()
    product_description= scrapy.Field()
    product_id = scrapy.Field()
    product_price = scrapy.Field()
