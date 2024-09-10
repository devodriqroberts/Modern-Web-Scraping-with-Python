import scrapy
from math import ceil
import re
from ..items import CandlesScraperItem

class YankeeCandleSpider(scrapy.Spider):

    # Name of spider
    name = "YankeeCandle"
    BASE_URL = "https://www.yankeecandle.com"

    # Results Per Page
    rpp = 48
    total_results = 590
    num_pages = ceil(590 / 48)

    start_urls = [f"https://www.yankeecandle.com/browse/candles/shop-all-candles/_/N-cnp?No=0&Nrpp=48&view=grid"]

    def parse(self, response):
        
        item_links = response.css("div.product_image a::attr(href)").extract()
        
        for link in item_links:
            abs_url = self.BASE_URL + link
            yield scrapy.Request(abs_url, self.parse_item_attr)

    def parse_item_attr(self, response):
        item = CandlesScraperItem()

        item["product_brand"] = self.name
        item["product_link"] = response.url
        item["product_heading"] = response.css("div.product-heading h1::text").extract_first()
        item["product_description"] = response.css("div.descriptionContainer p::text").extract_first()
        item["product_id"] = re.search("\d+", response.css("div.numbr-frgnce p::text").extract_first()).group(0)
        item["product_price"] = response.css("p.origPrice span::text").extract_first()

        yield item

        next_page = f"https://www.yankeecandle.com/browse/candles/shop-all-candles/_/N-cnp?No={YankeeCandleSpider.rpp}&Nrpp=48&view=grid"
        if YankeeCandleSpider.rpp <= 624:
            YankeeCandleSpider.rpp += 48
            yield response.follow(next_page, callback=self.parse)

