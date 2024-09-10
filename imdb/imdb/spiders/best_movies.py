import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    user_agent = "'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'"

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/chart/top/', headers={'User-Agent': self.user_agent})

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//table[@class='chart full-width']//tbody[@class='lister-list']//tr//td[@class='titleColumn']//a"), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"), process_request='set_user_agent'),
    )

    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'title': response.xpath("//h1[contains(@class, 'TitleHeader__TitleText')]//text()").get(),
            'year': response.xpath("(//div[contains(@class, 'TitleBlock__TitleMetaDataContainer')]//li[@role='presentation']//text())[1]").get(),
            'film_rating': response.xpath("(//div[contains(@class, 'TitleBlock__TitleMetaDataContainer')]//li[@role='presentation']//text())[3]").get(),
            'duration': response.xpath("(//div[contains(@class, 'TitleBlock__TitleMetaDataContainer')]//li[@role='presentation']//text())[5]").get(),
            'genre': response.xpath("//a[contains(@class, 'GenresAndPlot')]//span//text()").get(),
            'rating': response.xpath("//div[contains(@class, 'TitleBlock__Container')]//span[contains(@class, 'AggregateRatingButton')]//text()").get(),
            'movie_url': response.url
        }
