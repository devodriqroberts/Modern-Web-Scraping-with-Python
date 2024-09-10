import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['web.archive.org']
    start_urls = ['https://web.archive.org/web/20110207093218/http://www.tinydeal.com/specials.html']

    def parse(self, response):
        pass
