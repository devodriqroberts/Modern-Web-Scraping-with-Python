import scrapy


class FrontPageDealsSpider(scrapy.Spider):
    name = 'front_page_deals'
    allowed_domains = ['slickdeals.net']

    def start_requests(self):
        yield scrapy.Request(url='https://slickdeals.net/', callback=self.parse, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'})

    def parse(self, response):
        for product in response.xpath("//ul[@class='dealTiles gridDeals dealTileGridOverrides']/li[contains(@id, 'DealCard')]"):
            yield {
                "title": product.xpath(".//a[@class='bp-c-card_title bp-c-link']/text()").get(),
                "url": response.urljoin(product.xpath(".//a[@class='bp-c-card_title bp-c-link']/@href").get()),
                "discounted_price": product.xpath(".//span[@class='bp-p-dealCard_price']/text()").get(),
                "original_price": product.xpath(".//span[@class='bp-p-dealCard_originalPrice']/text()").get()

            }

        # Pagination - Scrape next pages
        next_page = response.xpath("//div[@class='pagination buttongroup']//a[@class='button']//@href").get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'})
