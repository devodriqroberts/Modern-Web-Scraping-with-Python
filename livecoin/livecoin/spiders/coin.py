import scrapy
from scrapy_splash import SplashRequest

class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['www.web.archive.org/web/20200116052415/https://www.livecoin.net/en']

    script = """
        function main(splash, args)
            splash.private_mode_enabled = false
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(1))
            rur_tab = assert(splash:select_all(".filterPanelItem__2z5Gb"))
            rur_tab[5]:mouse_click()
            assert(splash:wait(1))
            splash:set_viewport_full()
            return splash:html()
        end
    """

    def start_requests(self):
        yield SplashRequest(url="https://www.web.archive.org/web/20200116052415/https://www.livecoin.net/en", callback=self.parse, endpoint="execute", args={"lua_source": self.script})

    def parse(self, response):
        for currency in response.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow__3Etis )]"):
            yield {
                'currency_pair': currency.xpath(".//div[1]/div/text()").get(),
                'volume(24h': currency.xpath(".//div[2]/span/text()").get()
            }
