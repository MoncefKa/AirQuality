import scrapy


class AirqualitySpider(scrapy.Spider):
    name = "airquality"
    allowed_domains = ["www.iqair.com"]
    start_urls = ["https://www.iqair.com/world-most-polluted-countries"]

    def parse(self, response):
        pass
